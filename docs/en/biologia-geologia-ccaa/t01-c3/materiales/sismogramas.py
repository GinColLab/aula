# /// script
# requires-python = ">=3.12"
# dependencies = ["obspy>=1.4.1", "numpy>=2", "matplotlib>=3.8"]
# ///
"""La sombra del núcleo, con datos reales: los sismogramas de un gran terremoto profundo, ordenados por distancia.

Es el programa de la clase 3 de Biología, Geología y Ciencias Ambientales (GinCol Lab, «La sombra del núcleo») y
el de su ficha docente, para repetir la actividad con cualquier gran terremoto profundo:

    uv run --script sismogramas.py                # Fiyi, 19/08/2018 (us1000gcii): la sección y la tabla
    uv run --script sismogramas.py us20002ki3     # otro terremoto, por su código del USGS (aquí, islas Bonin, 2015)

Sirven los terremotos profundos (más de 300 km) de magnitud 7 o más: así la onda P sale limpia. Sin `uv`, basta con
`pip install obspy matplotlib` y `python sismogramas.py`.

Qué hace, paso a paso:
1. Pide al USGS el origen del terremoto: hora, lugar y profundidad.
2. Pide a EarthScope las estaciones de banda ancha de las redes mundiales abiertas (REDES), con su sismómetro
   vertical (BHZ), y la distancia de cada una al epicentro, en grados (un grado son unos 111 km de superficie).
3. Parte las distancias en franjas de 1,5° y baja hasta cuatro registros por franja; de cada franja se queda con el
   más limpio: el que más destaca, tras el terremoto, sobre el ruido de los dos minutos anteriores.
4. Quita la respuesta del aparato (pasa de cuentas a velocidad del suelo), filtra entre 0,5 y 2 Hz, las vibraciones
   de entre medio segundo y dos segundos, que es donde mejor se ve la onda P, y escala cada registro a su propio
   máximo, para que se vean todos.
5. En cada registro mide la onda P directa: lo que se mueve el suelo en los 25 s siguientes a la hora a la que
   debería llegar (modelo iasp91) frente al ruido de antes del terremoto. Si no pasa de 6 veces el ruido, la P directa
   «no se distingue».

Salidas, en la carpeta `salida-<código>/` junto al programa: la sección en PNG (para imprimir) y la tabla de
llegadas en CSV. Con el terremoto de Fiyi, en la clase, van a `materiales/` (lo que ofrece la ficha docente), y los
datos que dibuja la pizarra, a `medios/`.

Los datos de las redes mundiales se distribuyen con licencia abierta (CC BY 4.0) desde el archivo NSF NGF que opera
EarthScope Consortium (antes, NSF SAGE): se citan la red y su DOI. Lo que se baja se guarda en datos/descargas/ y no se vuelve a pedir.
"""

import csv
import json
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from obspy import UTCDateTime, read, read_inventory, Stream
from obspy.clients.fdsn import Client
from obspy.geodetics import gps2dist_azimuth, locations2degrees
from obspy.taup import TauPyModel

AQUI = Path(__file__).resolve().parent
# En el laboratorio, lo bajado va a datos/descargas/ de la fábrica; copiado suelto (desde la ficha docente), junto al
# programa, en descargas/.
_FABRICA = AQUI.parents[1] if len(AQUI.parents) > 1 else AQUI
DESCARGAS = (_FABRICA / "datos" / "descargas" / "sismogramas") if (_FABRICA / "fabrica").exists() else AQUI / "descargas"
REDES = ["IU", "II", "G", "GE", "AU", "MN", "IC", "GT"]  # las redes mundiales abiertas, en orden de preferencia
FRANJA = 1.5  # grados
POR_FRANJA = 4
FILTRO = (0.5, 2.0)  # Hz
UMBRAL_P = 6.0  # la P directa se ve si su movimiento pasa de 6 veces el ruido
P_HASTA = 96.0  # grados: hasta aquí llega la P directa desde un foco a 600 km (iasp91; con uno superficial, 98)
# Estaciones que no se usan, con su porqué (si su franja tiene otra, entra la siguiente):
DUDOSAS = {"GE.SNAA": "su P mide unas 40 veces más que la de sus vecinas, con unos metadatos normales: probable error "
                      "en la respuesta del aparato (verificación del 08/10/2026)"}
ANTES, DESPUES = 120, 1800  # s alrededor del origen
COLUMNAS = 1400  # la pizarra dibuja cada registro con un mínimo y un máximo por columna
MODELO = TauPyModel("iasp91")


def cliente() -> Client:
    try:
        return Client("EARTHSCOPE")
    except ValueError:  # ObsPy antiguo
        return Client("IRIS")


# Los terremotos de la clase, tal como los da el catálogo del USGS (consultado el 08/10/2026): así la clase no depende
# de que el servicio responda. Cualquier otro se pide al USGS por su código.
CONOCIDOS = {
    "us1000gcii": ("2018 Fiji Earthquake", "2018-08-19T00:19:40.670000Z", -18.1125, -178.153, 600.0, 8.2, "mww"),
    "us7000dflf": ("2021 Kermadec Islands, New Zealand Earthquake", "2021-03-04T19:28:33.178000Z", -29.7228,
                   -177.2794, 28.93, 8.1, "mww"),
    "ojotsk-2013": ("2013 Sea of Okhotsk Earthquake", "2013-05-24T05:44:48.980000Z", 54.892, 153.221, 598.1, 8.3,
                    "mww"),
    "mindanao-2010": ("61 km W of Bantogon, Philippines", "2010-07-23T22:51:11.840000Z", 6.497, 123.48, 578.0, 7.6,
                      "mwc"),
}


def origen(codigo: str) -> dict:
    if codigo in CONOCIDOS:
        nombre, hora, lat, lon, prof, mag, tipo = CONOCIDOS[codigo]
        return {"codigo": codigo, "nombre": nombre, "hora": hora, "lat": lat, "lon": lon, "profundidad_km": prof,
                "magnitud": mag, "tipo_magnitud": tipo}
    o = Client("USGS").get_events(eventid=codigo)[0]
    p, m = o.preferred_origin(), o.preferred_magnitude()
    nombre = o.event_descriptions[0].text if o.event_descriptions else codigo
    return {"codigo": codigo, "nombre": nombre, "hora": str(p.time), "lat": p.latitude, "lon": p.longitude,
            "profundidad_km": p.depth / 1000, "magnitud": m.mag, "tipo_magnitud": m.magnitude_type}


def llegadas(prof: float, dist: float) -> dict:
    """Hora teórica (s tras el terremoto) de cada fase en el modelo iasp91; la primera de cada nombre."""
    t = {}
    # «p» y «s», en minúscula, son las que suben directas desde un foco profundo hasta las estaciones cercanas
    for a in MODELO.get_travel_times(prof, dist, ["p", "P", "Pdiff", "PKIKP", "PKiKP", "PKP", "PP", "s", "S", "SS"]):
        t.setdefault(a.name, a.time)
    return t


def bajar_seccion(ev: dict, es: Client) -> tuple[list, object]:
    carpeta = DESCARGAS / ev["codigo"]
    carpeta.mkdir(parents=True, exist_ok=True)
    t0 = UTCDateTime(ev["hora"])
    fich = carpeta / "inventario.xml"
    if fich.exists():
        inv = read_inventory(str(fich))
    else:
        inv = es.get_stations(network=",".join(REDES), channel="BHZ", starttime=t0, endtime=t0 + DESPUES,
                              level="response")
        inv.write(str(fich), format="STATIONXML")
    franjas = {}
    estaciones = sorted(((n.code, s.code, s.latitude, s.longitude, locations2degrees(ev["lat"], ev["lon"], s.latitude,
                                                                                       s.longitude), s.site.name)
                         for n in inv for s in n), key=lambda e: REDES.index(e[0]))
    for e in estaciones:
        franjas.setdefault(int(e[4] // FRANJA), []).append(e)
    pedir = [e for f in franjas.values() for e in f[:POR_FRANJA]]
    faltan = [e for e in pedir if not (carpeta / f"{e[0]}.{e[1]}.mseed").exists()
              and not (carpeta / f"{e[0]}.{e[1]}.vacio").exists()]
    for i in range(0, len(faltan), 40):
        lote = faltan[i:i + 40]
        try:
            st = es.get_waveforms_bulk([(n, s, "*", "BHZ", t0 - ANTES, t0 + DESPUES) for n, s, *_ in lote])
        except Exception as ex:  # noqa: BLE001 — un lote fallido no para el resto
            print("lote sin datos:", ex)
            st = Stream()
        for n, s, *_ in lote:
            sub = st.select(network=n, station=s)
            if len(sub):
                sub.write(str(carpeta / f"{n}.{s}.mseed"), format="MSEED")
            else:
                (carpeta / f"{n}.{s}.vacio").touch()
        print(f"bajados {i + len(lote)} de {len(faltan)}", flush=True)
    return pedir, inv


def preparar(fich: Path, inv, t0: UTCDateTime, filtro=FILTRO, comp: str | None = None):
    """Un registro limpio: sin huecos, en velocidad del suelo (m/s), filtrado. None si no sirve."""
    st = read(str(fich))
    locs = sorted({tr.stats.location for tr in st})
    st = st.select(location="00" if "00" in locs else locs[0])
    if comp:
        st = st.select(component=comp)
    st.merge(fill_value=None)
    tr = st[0]
    if np.ma.isMaskedArray(tr.data) and tr.data.mask.any():
        return None
    if tr.stats.starttime > t0 - ANTES + 20 or tr.stats.endtime < t0 + DESPUES - 100:
        return None
    try:
        tr.remove_sensitivity(inv)
    except Exception:  # noqa: BLE001 — sin respuesta conocida, no se usa
        return None
    tr.detrend("demean"); tr.detrend("linear"); tr.taper(0.02)
    tr.filter("bandpass", freqmin=filtro[0], freqmax=filtro[1], corners=4, zerophase=True)
    tr.trim(t0 - ANTES + 10, t0 + DESPUES - 10)
    t = np.arange(tr.stats.npts) / tr.stats.sampling_rate + (tr.stats.starttime - t0)
    return t, tr.data.astype(float)


def columnas(t: np.ndarray, x: np.ndarray, t_ini: float, t_fin: float, n: int = COLUMNAS) -> np.ndarray:
    """Mínimo y máximo de cada columna de tiempo: así una línea de pizarra conserva cada pico del registro."""
    bordes = np.linspace(t_ini, t_fin, n + 1)
    idx = np.searchsorted(t, bordes)
    mm = np.zeros((n, 2))
    for i in range(n):
        tramo = x[idx[i]:max(idx[i + 1], idx[i] + 1)]
        mm[i] = (tramo.min(), tramo.max()) if len(tramo) else (0, 0)
    return mm


def seccion(ev: dict) -> list[dict]:
    es = cliente()
    t0 = UTCDateTime(ev["hora"])
    pedir, inv = bajar_seccion(ev, es)
    carpeta = DESCARGAS / ev["codigo"]
    registros = []
    for red, est, lat, lon, dist, sitio in pedir:
        fich = carpeta / f"{red}.{est}.mseed"
        if not fich.exists() or f"{red}.{est}" in DUDOSAS:
            continue
        r = preparar(fich, inv, t0)
        if r is None:
            continue
        t, x = r
        teo = llegadas(ev["profundidad_km"], dist)
        primera = min(teo.values())
        ruido = np.sqrt(np.mean(x[t < -5] ** 2))
        despues = t > primera - 5
        limpieza = np.abs(x[despues]).max() / ruido
        tp = r_p(teo)
        ventana = (t > tp - 3) & (t < tp + 25) if tp else np.zeros_like(t, bool)
        p_ruido = np.abs(x[ventana]).max() / ruido if tp else 0.0
        registros.append({"red": red, "estacion": est, "sitio": sitio, "lat": lat, "lon": lon, "dist": dist,
                          "limpieza": limpieza, "p_ruido": p_ruido, "teoricas": teo, "t": t, "x": x,
                          "maximo": np.abs(x[despues]).max()})
    # De cada franja, el registro más limpio: hasta donde llega la P directa, el de la P más clara (si no, se colaba
    # alguno de puro ruido con una sacudida tardía, como el de Tarawa a 21°); más allá, el que más destaca del ruido.
    mejores = {}
    for r in registros:
        b = int(r["dist"] // FRANJA)
        nota = r["p_ruido"] if r["dist"] < P_HASTA else r["limpieza"]
        if r["limpieza"] > 5 and nota > mejores.get(b, (0, None))[0]:
            mejores[b] = (nota, r)
    elegidos = sorted((r for _, r in mejores.values()), key=lambda r: r["dist"])
    # Antes de 96° la P directa tiene que verse: si el mejor registro de una franja no la enseña, es que esa estación
    # tenía demasiado ruido ese día, y la franja se queda vacía antes que dibujar un hueco falso en la curva.
    ruidosos = [r for r in elegidos if r["dist"] < P_HASTA and r["p_ruido"] <= UMBRAL_P]
    for r in ruidosos:
        print(f"fuera, por ruido: {r['red']}.{r['estacion']} a {r['dist']:.1f}° (la P no pasa de {r['p_ruido']:.1f} veces "
              "el ruido)")
    elegidos = [r for r in elegidos if r not in ruidosos]
    for r in elegidos:
        # La P directa (la que sube del foco, «p», o la P) sólo existe hasta unos 96° con este foco; más allá, a esa
        # hora llega la que rodea el núcleo (Pdiff), que se mide aparte y nunca se llama P directa.
        directa = "p" in r["teoricas"] or "P" in r["teoricas"]
        r["p_directa"] = bool(directa and r["p_ruido"] > UMBRAL_P)
        r["llegada_p"] = medir(r, r_p(r["teoricas"])) if r["p_directa"] else None
        r["rodea"] = not directa and "Pdiff" in r["teoricas"]
        # las ondas que cruzan el núcleo (PKIKP, y desde unos 143°, PKP): su fuerza y su hora, medidas igual
        tk = r["teoricas"].get("PKIKP") or r["teoricas"].get("PKP")
        t, x = r["t"], r["x"]
        ruido = np.sqrt(np.mean(x[t < -5] ** 2))
        if tk:
            v = (t > tk - 3) & (t < tk + 25)
            r["nucleo_um_s"] = float(np.abs(x[v]).max() * 1e6)
            r["nucleo_ruido"] = float(np.abs(x[v]).max() / ruido)
            r["llegada_nucleo"] = medir(r, tk) if r["nucleo_ruido"] > UMBRAL_P else None
        else:
            r["nucleo_um_s"] = r["nucleo_ruido"] = r["llegada_nucleo"] = None
        tp = r_p(r["teoricas"])
        r["p_um_s"] = float(np.abs(x[(t > tp - 3) & (t < tp + 25)]).max() * 1e6) if tp else None
        # lo que pesa cada onda en su propio registro (1, la mayor), que es lo que se ve en la sección
        r["p_rel"] = r["p_um_s"] / (r["maximo"] * 1e6) if tp else 0.0
        r["nucleo_rel"] = r["nucleo_um_s"] / (r["maximo"] * 1e6) if tk else 0.0
        r["t_p"], r["t_nucleo"] = tp, tk
    return elegidos


def r_p(teo: dict) -> float | None:
    """La hora de la onda P directa: cerca, la que sube desde el foco (p); después, la P; y desde unos 96°, la que
    rodea el núcleo (Pdiff)."""
    return teo.get("p", teo.get("P", teo.get("Pdiff")))


def medir(r: dict, tp: float) -> float | None:
    """La hora de llegada de una onda, medida: el primer momento, a menos de 15 s de su hora teórica, en que el suelo
    se mueve más de 4 veces el ruido de antes del terremoto."""
    t, x = r["t"], r["x"]
    ruido = np.sqrt(np.mean(x[t < -5] ** 2))
    v = (t > tp - 15) & (t < tp + 15)
    fuera = np.nonzero(np.abs(x[v]) > 4 * ruido)[0]
    return float(t[v][fuera[0]]) if len(fuera) else None


def dibujar(ev: dict, elegidos: list[dict], destino: Path) -> None:
    fig, ax = plt.subplots(figsize=(11, 15))
    for r in elegidos:
        y = r["x"] / r["maximo"] * 1.3
        paso = max(1, len(y) // 8000)
        ax.plot(r["t"][::paso] / 60, r["dist"] + y[::paso], lw=0.35, color="k")
    ax.set_xlim(0, 25); ax.set_ylim(0, 181)
    ax.set_xticks(range(0, 26, 1), minor=True); ax.set_yticks(range(0, 181, 10), minor=True)
    ax.grid(which="both", color="0.85", linewidth=0.4); ax.set_axisbelow(True)
    ax.set_xlabel("Minutos después del terremoto"); ax.set_ylabel("Distancia al epicentro (grados)")
    coma = lambda v: f"{v}".replace(".", ",")
    ax.set_title(f"{ev['nombre']} · {ev['hora'][:16].replace('T', ' ')} UTC · {ev['profundidad_km']:.0f} km · "
                 f"magnitud {coma(round(ev['magnitud'], 1))}\n{len(elegidos)} registros verticales, filtro de "
                 f"{coma(FILTRO[0])} a {coma(FILTRO[1])} Hz,"
                 " cada uno a su escala · Datos: NSF NGF (EarthScope), CC BY 4.0, redes " + ", ".join(sorted({r['red'] for r in elegidos})),
                 fontsize=9)
    fig.savefig(destino, dpi=150, bbox_inches="tight")
    plt.close(fig)


def tabla(elegidos: list[dict], destino: Path) -> None:
    with open(destino, "w", newline="", encoding="utf-8-sig") as f:  # «;» y coma decimal, como la abre una hoja en español
        w = csv.writer(f, delimiter=";")
        w.writerow(["red", "estacion", "lugar", "distancia_grados", "distancia_km", "onda_P_directa",
                    "llegada_P_minutos", "fuerza_P_um_s", "a_la_hora_de_la_P_si_no_hay_P_directa_um_s",
                    "onda_que_cruza_el_nucleo_um_s", "llegada_onda_del_nucleo_minutos"])
        for r in elegidos:
            w.writerow([r["red"], r["estacion"], r["sitio"], f"{r['dist']:.1f}".replace(".", ","), round(r["dist"] * 111.19),
                        "sí" if r["p_directa"] else ("no llega (más allá de 96°)" if r["dist"] >= P_HASTA
                                                     else "no se distingue"),
                        f"{r['llegada_p'] / 60:.2f}".replace(".", ",") if r["llegada_p"] else "",
                        f"{r['p_um_s']:.2f}".replace(".", ",") if r["p_directa"] and r["p_um_s"] else "",
                        f"{r['p_um_s']:.2f}".replace(".", ",") if r["rodea"] and r["p_um_s"] else "",
                        f"{r['nucleo_um_s']:.2f}".replace(".", ",") if r["nucleo_um_s"] else "",
                        f"{r['llegada_nucleo'] / 60:.2f}".replace(".", ",") if r.get("llegada_nucleo") else ""])


def guardar_pizarra(ev: dict, elegidos: list[dict]) -> None:
    """Lo que dibuja la pizarra: cada registro en columnas (mínimo y máximo), de 0 a 25 minutos, y las curvas teóricas."""
    medios = AQUI / "medios"
    medios.mkdir(exist_ok=True)
    t_ini, t_fin = 0.0, 1500.0
    mm = np.stack([columnas(r["t"], r["x"] / r["maximo"], t_ini, t_fin) for r in elegidos]).astype(np.float16)
    dist = np.arange(0, 180.5, 0.5)
    curvas = {f: np.array([llegadas(ev["profundidad_km"], d).get(f, np.nan) for d in dist]) for f in
              ("p", "P", "Pdiff", "PKIKP", "PKP", "PP", "S")}
    np.savez_compressed(medios / "seccion-fiyi.npz", columnas=mm, t_ini=t_ini, t_fin=t_fin,
                        dist=np.array([r["dist"] for r in elegidos]), curva_dist=dist, **{f"curva_{k}": v for k, v in
                                                                                          curvas.items()})
    estaciones = [{k: (round(v, 3) if isinstance(v, float) else v) for k, v in r.items()
                   if k in ("red", "estacion", "sitio", "lat", "lon", "dist", "p_ruido", "p_directa", "llegada_p", "p_um_s",
                            "nucleo_um_s", "nucleo_ruido", "llegada_nucleo", "p_rel", "nucleo_rel", "t_p",
                            "t_nucleo", "rodea")}
                  for r in elegidos]
    (medios / "seccion-fiyi.json").write_text(json.dumps({"evento": ev, "filtro_hz": FILTRO, "umbral_p": UMBRAL_P,
                                                          "estaciones": estaciones}, ensure_ascii=False, indent=1))


# ---- Los registros sueltos de la clase: Hawái (P y S), Australia (profundo frente a superficial) y Toledo (el control)

SUELTOS = {
    "ojotsk": "ojotsk-2013",      # mar de Ojotsk, 24/05/2013, 598 km, M8,3
    "mindanao": "mindanao-2010",  # Mindanao (Filipinas), 23/07/2010, 22:51 UTC, 578 km, M7,6 (el segundo de los tres)
    "kermadec": "us7000dflf",     # islas Kermadec, 04/03/2021, 29 km, M8,1
}


def suelto(es: Client, ev: dict, red: str, est: str, canales: str, filtro: tuple, duracion: float,
           comps: tuple = ("Z",)) -> dict:
    t0 = UTCDateTime(ev["hora"])
    fich = DESCARGAS / "sueltos" / f"{ev['codigo']}.{red}.{est}.{canales.replace('?', '_')}.mseed"
    fich.parent.mkdir(parents=True, exist_ok=True)
    if not fich.exists():
        es.get_waveforms(red, est, "00", canales, t0 - ANTES, t0 + DESPUES + 1200).write(str(fich), format="MSEED")
    inv = es.get_stations(network=red, station=est, location="00", channel=canales, level="response",
                          starttime=t0, endtime=t0 + 10)
    s = inv[0][0]
    dist = locations2degrees(ev["lat"], ev["lon"], s.latitude, s.longitude)
    st = read(str(fich)).select(location="00")
    st.merge(); st.detrend("demean"); st.taper(0.02); st.remove_sensitivity(inv)
    if "T" in comps:
        st.rotate("->ZNE", inventory=inv)
        st.rotate("NE->RT", back_azimuth=gps2dist_azimuth(s.latitude, s.longitude, ev["lat"], ev["lon"])[1])
    st.filter("bandpass", freqmin=filtro[0], freqmax=filtro[1], corners=4, zerophase=True)
    salida = {"evento": ev, "red": red, "estacion": est, "sitio": s.site.name, "lat": s.latitude, "lon": s.longitude,
              "dist": round(dist, 2), "filtro_hz": filtro, "teoricas": llegadas(ev["profundidad_km"], dist),
              "t_fin": duracion, "componentes": {}}
    for c in comps:
        tr = st.select(component=c)[0]
        t = np.arange(tr.stats.npts) / tr.stats.sampling_rate + (tr.stats.starttime - t0)
        mm = columnas(t, tr.data * 1e6, 0.0, duracion, 1000)  # en micras por segundo
        salida["componentes"][c] = {"min": np.round(mm[:, 0], 3).tolist(), "max": np.round(mm[:, 1], 3).tolist(),
                                    "pico_um_s": round(float(np.abs(mm).max()), 3)}
    return salida


def sonido(es: Client, fiyi: dict, red: str = "IU", est: str = "POHA", acelerar: int = 250, agudo: int = 16,
           banda: tuple = (0.03, 0.5), minutos: float = 18.0) -> Path:
    """El registro de lado (transversal) de una estación, hecho sonido: el mismo que se ve en la pizarra (la misma banda,
    de 0,03 a 0,5 vibraciones por segundo), con 18 minutos de Hawái acelerados `acelerar` veces, que caben en 4,3 s.
    Acelerado sin más, todo quedaría entre 7 y 125 Hz, demasiado grave para oírse, sobre todo la S, la más lenta; por
    eso se sube además `agudo` veces de tono (cuatro octavas) sin cambiar su duración, con el filtro rubberband de
    ffmpeg: la S suena hacia 400 Hz y la P, más aguda, hacia 1000–2000. Se usa el registro de lado porque ahí la S es
    mucho mayor que la P (7,6 veces en esa banda). Comprobado el 09/10/2026 con un modelo de sonoridad: la S suena el
    doble de fuerte que la P. Con la banda de 0,15 a 8 y sólo dos octavas, la P y la S sonaban igual de fuertes: el
    filtro se comía la S. Sólo se reescala entero, sin comprimir. Sólo en la fábrica: necesita ffmpeg con rubberband."""
    import subprocess
    from scipy.io import wavfile

    t0 = UTCDateTime(fiyi["hora"])
    fich = DESCARGAS / "sueltos" / f"{fiyi['codigo']}.{red}.{est}.BH_.mseed"
    inv = es.get_stations(network=red, station=est, location="00", channel="BH?", level="response",
                          starttime=t0, endtime=t0 + 10)
    s = inv[0][0]
    st = read(str(fich)).select(location="00")
    st.merge(); st.detrend("demean"); st.taper(0.02); st.remove_sensitivity(inv)
    st.rotate("->ZNE", inventory=inv)
    st.rotate("NE->RT", back_azimuth=gps2dist_azimuth(s.latitude, s.longitude, fiyi["lat"], fiyi["lon"])[1])
    tr = st.select(component="T")[0]
    tr.filter("bandpass", freqmin=banda[0], freqmax=banda[1], corners=4, zerophase=True)
    tr.trim(t0, t0 + minutos * 60)
    x = tr.data.astype(float)
    x = x / np.abs(x).max() * 0.9
    n_fade = int(0.02 * len(x))
    x[:n_fade] *= np.linspace(0, 1, n_fade)
    x[-n_fade:] *= np.linspace(1, 0, n_fade)
    frecuencia = int(round(tr.stats.sampling_rate * acelerar))
    destino = AQUI / "medios" / f"{est.lower()}-acelerado.wav"
    crudo = destino.with_name(destino.stem + "-sin-subir.wav")
    wavfile.write(str(crudo), frecuencia, (x * 32767).astype(np.int16))
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(crudo), "-af",
                    f"aresample=48000,rubberband=pitch={agudo}:transients=smooth", "-ar", "48000", "-ac", "1",
                    str(destino)], check=True)
    crudo.unlink()
    fs, y = wavfile.read(str(destino))
    y = y.astype(float) / np.abs(y).max() * 0.9 * 32767  # sólo se reescala entero: la S sigue siendo lo más fuerte
    wavfile.write(str(destino), fs, y.astype(np.int16))
    print(f"sonido: {destino.name}, {len(y) / fs:.2f} s (×{acelerar}, {agudo} veces más agudo)")
    return destino


def sueltos(fiyi: dict) -> None:
    es = cliente()
    ev = {k: origen(v) for k, v in SUELTOS.items()}
    ev["fiyi"] = fiyi
    datos = {
        "poha": suelto(es, fiyi, "IU", "POHA", "BH?", (0.03, 0.5), 1080, ("Z", "T")),
        # 0,05–1 Hz: deja ver las ondas superficiales (periodos de unos 20–30 s) sin el vaivén lento de las ondas que
        # rebotan entre la superficie y el foco profundo (verificación del 08/10/2026)
        "ctao_fiyi": suelto(es, fiyi, "IU", "CTAO", "BHZ", (0.05, 1.0), 2100),
        "ctao_kermadec": suelto(es, ev["kermadec"], "IU", "CTAO", "BHZ", (0.05, 1.0), 2100),
        "pab_ojotsk": suelto(es, ev["ojotsk"], "IU", "PAB", "BHZ", FILTRO, 1500),
        "pab_mindanao": suelto(es, ev["mindanao"], "IU", "PAB", "BHZ", FILTRO, 1500),
        "pab_fiyi": suelto(es, fiyi, "IU", "PAB", "BHZ", FILTRO, 1500),
    }
    (AQUI / "medios" / "registros.json").write_text(json.dumps(datos, ensure_ascii=False))
    sonido(es, fiyi)
    for k, d in datos.items():
        print(k, d["estacion"], f"{d['dist']}°", {c: v["pico_um_s"] for c, v in d["componentes"].items()},
              {f: round(v / 60, 2) for f, v in d["teoricas"].items()})


if __name__ == "__main__":
    codigo = sys.argv[1] if len(sys.argv) > 1 else "us1000gcii"
    ev = origen(codigo)
    print(ev)
    elegidos = seccion(ev)
    salida = AQUI / ("materiales" if len(sys.argv) == 1 and (AQUI / "guion.json").exists() else f"salida-{codigo}")
    salida.mkdir(exist_ok=True)
    dibujar(ev, elegidos, salida / "seccion.png")
    tabla(elegidos, salida / "llegadas.csv")
    vistas = [r["dist"] for r in elegidos if r["p_directa"]]
    print(f"{len(elegidos)} registros; la P directa, hasta {max(vistas):.1f}°; las que no la tienen clara antes de "
          f"{P_HASTA:.0f}°: {[round(r['dist'], 1) for r in elegidos if r['dist'] < P_HASTA and not r['p_directa']]}")
    if len(sys.argv) == 1 and (AQUI / "guion.json").exists():  # sólo en la fábrica: lo que dibuja la pizarra
        guardar_pizarra(ev, elegidos)
        sueltos(ev)

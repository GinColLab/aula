# /// script
# requires-python = ">=3.12"
# dependencies = ["obspy>=1.4.1", "numpy>=2"]
# ///
"""La onda S cruza el manto entero, con datos reales: los mismos 96 sismogramas de Fiyi (19/08/2018) de la clase 3, pero
mirando lo que se mueve de lado.

La sección de la clase 3 es del sismómetro vertical y filtrada entre 0,5 y 2 Hz, donde mejor se ve la P. La S se ve en el
movimiento de lado (la componente transversal: perpendicular a la línea que une el terremoto con la estación) y en
vibraciones largas, de 10 a 50 segundos. Por eso aquí se bajan las tres componentes de cada estación, se giran hacia el
terremoto y se filtran entre 0,02 y 0,1 Hz.

    uv run --script seccion_s.py

Deja `seccion-s-fiyi.npz` (cada registro, con un mínimo y un máximo por columna) y `seccion-s-fiyi.json`, junto a este
programa. Lo bajado se guarda en la carpeta `descargas/` y no se vuelve a pedir. Datos: redes IU, II, G, GE, AU, MN, IC y GT,
archivo NSF NGF de EarthScope Consortium, CC BY 4.0.
"""

import json
from pathlib import Path

import numpy as np
from obspy import UTCDateTime, read, read_inventory
from obspy.clients.fdsn import Client
from obspy.geodetics import gps2dist_azimuth
from obspy.taup import TauPyModel

AQUI = Path(__file__).resolve().parent
DESCARGAS = AQUI / "descargas"
DESCARGAS.mkdir(parents=True, exist_ok=True)
C3 = json.loads((AQUI / "estaciones-fiyi.json").read_text())
HORA = UTCDateTime("2018-08-19T00:19:40.670000Z")
LAT, LON, PROF = -18.1125, -178.153, 600.0
FILTRO = (0.02, 0.1)
ANTES, DESPUES = 300, 2100
COLUMNAS = 1400
T_INI, T_FIN = 0.0, 1800.0
MODELO = TauPyModel("iasp91")
UA = "GinColLab-documentacion/1.0 (uso educativo)"


def columnas(t: np.ndarray, x: np.ndarray) -> np.ndarray:
    bordes = np.linspace(T_INI, T_FIN, COLUMNAS + 1)
    k = np.clip(np.searchsorted(bordes, t, side="right") - 1, 0, COLUMNAS - 1)
    fuera = (t < T_INI) | (t > T_FIN)
    salida = np.zeros((COLUMNAS, 2))
    salida[:, 0], salida[:, 1] = np.inf, -np.inf
    np.minimum.at(salida[:, 0], k[~fuera], x[~fuera])
    np.maximum.at(salida[:, 1], k[~fuera], x[~fuera])
    salida[~np.isfinite(salida)] = 0.0
    return salida


def main() -> None:
    es = Client("EARTHSCOPE", user_agent=UA)
    elegidas, pistas = [], []
    for e in C3["estaciones"]:
        d = e["dist"]
        if not 12 <= d <= 130:
            continue
        red, est = e["red"], e["estacion"]
        fm, fi = DESCARGAS / f"{red}.{est}.mseed", DESCARGAS / f"{red}.{est}.xml"
        try:
            if not fm.exists():
                st = es.get_waveforms(red, est, "*", "BH?", HORA - ANTES, HORA + DESPUES)
                st.write(str(fm), format="MSEED")
            if not fi.exists():
                inv = es.get_stations(network=red, station=est, channel="BH?", starttime=HORA, endtime=HORA + DESPUES,
                                      level="response")
                inv.write(str(fi), format="STATIONXML")
            st, inv = read(str(fm)), read_inventory(str(fi))
            # si la estación tiene dos sensores, el primero (normalmente 00)
            loc = sorted({tr.stats.location for tr in st})[0]
            st = st.select(location=loc)
            st.merge(fill_value="interpolate")
            st.detrend("linear").taper(0.05)
            st.remove_response(inventory=inv, output="VEL", water_level=60)
            st.rotate("->ZNE", inventory=inv)
            baz = gps2dist_azimuth(LAT, LON, e["lat"], e["lon"])[2]
            st.rotate("NE->RT", back_azimuth=baz)
            st.filter("bandpass", freqmin=FILTRO[0], freqmax=FILTRO[1], corners=4, zerophase=True)
            tr = st.select(component="T")[0]
        except Exception as fallo:  # noqa: BLE001
            print(f"{red}.{est}: {type(fallo).__name__}: {str(fallo)[:90]}", flush=True)
            continue
        t = tr.times(reftime=HORA)
        x = tr.data.astype(float)
        llegadas = MODELO.get_travel_times(PROF, d, ["s", "S", "Sdiff"])
        ts = llegadas[0].time if llegadas else None
        if ts is None:
            print(f"{red}.{est}: sin S teórica a {d:.1f}°", flush=True)
            continue
        ruido = np.sqrt(np.mean(x[(t > -250) & (t < -20)] ** 2))
        pulso = np.abs(x[(t > ts - 20) & (t < ts + 60)]).max()
        fuera_p = np.abs(x[(t > ts - 120) & (t < ts - 30)]).max()
        pico = float(t[(t > ts - 20) & (t < ts + 60)][np.abs(x[(t > ts - 20) & (t < ts + 60)]).argmax()])
        escala = max(np.abs(x[(t > T_INI) & (t < T_FIN)]).max(), 1e-12)
        pistas.append(columnas(t, x / escala))
        elegidas.append({"red": red, "estacion": est, "sitio": e.get("sitio"), "dist": d, "t_s": round(float(ts), 2),
                         "fase": llegadas[0].name, "pico": round(pico, 1), "s_um_s": round(float(pulso * 1e6), 2),
                         "antes_um_s": round(float(fuera_p * 1e6), 2), "ruido_um_s": round(float(ruido * 1e6), 3),
                         "s_ruido": round(float(pulso / max(ruido, 1e-12)), 1)})
        print(f"{red}.{est} {d:6.1f}° {llegadas[0].name:6s} t={ts:7.1f} S/ruido={pulso / max(ruido, 1e-12):7.1f}", flush=True)
    orden = np.argsort([e["dist"] for e in elegidas])
    elegidas = [elegidas[k] for k in orden]
    pistas = np.array([pistas[k] for k in orden], dtype=np.float32)
    np.savez_compressed(AQUI / "seccion-s-fiyi.npz", columnas=pistas, t_ini=T_INI, t_fin=T_FIN,
                        dist=np.array([e["dist"] for e in elegidas]))
    (AQUI / "seccion-s-fiyi.json").write_text(json.dumps(
        {"evento": "us1000gcii (Fiyi, 19/08/2018, 600 km, Mww 8,2)", "componente": "transversal", "filtro_hz": FILTRO,
         "datos": "redes IU, II, G, GE, AU, MN, IC y GT, NSF NGF (EarthScope), CC BY 4.0", "estaciones": elegidas},
        ensure_ascii=False, indent=1))
    print(len(elegidas), "estaciones", flush=True)


if __name__ == "__main__":
    main()

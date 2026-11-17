"""Mapa para recortar: Sudamérica y África, con la costa y el borde sumergido a 200 m, a la misma escala.

Es el «Hazlo tú» de la clase «De la deriva continental a la tectónica de placas» (GinCol Lab): se imprime dos veces, una
copia se recorta por la costa (línea negra) y la otra por el borde sumergido (línea azul), y se comparan los dos encajes.

Las líneas salen del relieve ETOPO 2022 (NOAA NCEI, dominio público, doi:10.25921/fd45-gt74), a 1′ de resolución, con el
mismo suavizado que el encaje de la pizarra: la de 0 m (la costa) y la de −200 m (el borde de la plataforma, la línea que
usó Wegener). Sólo la mitad que mira al Atlántico, de 8° N a 36° S en Sudamérica y de 13° N a 35,5° S en África: la otra
mitad no hace falta para encajar, y así cabe a 1:25 millones en un A4.

Cada continente va en su propia proyección azimutal equivalente de Lambert, centrada cerca de su costa atlántica: a la
misma escala, sin deformar las áreas, y con la forma del borde casi exacta donde se juntan los dos trozos. Al encajarlos
sobre el papel, el giro en el plano no es igual que en la esfera: el encaje de papel es aproximado; el de la pizarra,
calculado sobre la esfera (encaje.py), da el resultado exacto.

    uv run --with matplotlib --with h5py --with scipy python clases/biologia-geologia-ccaa-t02-c1/materiales/mapa_para_recortar.py

Sale `mapa-para-recortar.pdf`, cuatro páginas A4: los dos continentes para cortar por la costa y los dos para cortar por
el borde sumergido. Licencia del mapa: CC BY 4.0, GinCol Lab; los datos de ETOPO, dominio público.
"""

from pathlib import Path

import h5py
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.backends.backend_pdf import PdfPages  # noqa: E402
from scipy.ndimage import gaussian_filter, label  # noqa: E402

AQUI = Path(__file__).resolve().parent
ETOPO = AQUI.parents[2] / "datos" / "descargas" / "biologia-t02" / "etopo2022" / "ETOPO_2022_v1_60s_N90W180_surface.nc"
SALIDA = AQUI / "mapa-para-recortar.pdf"
RADIO = 6371.0  # km
ESCALA = 25e6  # 1:25 millones: 1 mm del papel son 25 km
A4 = (210.0, 297.0)  # mm, vertical

# caja (sur, norte, oeste, este) y centro de la proyección (lat, lon), cerca de la costa atlántica
CONTINENTES = {
    "Sudamérica": {"caja": (-36.0, 8.0, -62.0, -32.0), "centro": (-14.0, -45.0)},
    "África": {"caja": (-35.5, 13.0, -19.0, 22.0), "centro": (-8.0, 5.0)},
}

TINTA, AZUL, TIERRA, PLATAFORMA, GRIS = "#111111", "#1f5fbf", "#efe6d2", "#d6e6f7", "#888888"


def laea(lat, lon, lat0, lon0):
    """Proyección azimutal equivalente de Lambert (esfera), en km."""
    f, l_, f0, l0 = map(np.radians, (lat, lon, lat0, lon0))
    k = np.sqrt(2 / (1 + np.sin(f0) * np.sin(f) + np.cos(f0) * np.cos(f) * np.cos(l_ - l0)))
    x = RADIO * k * np.cos(f) * np.sin(l_ - l0)
    y = RADIO * k * (np.cos(f0) * np.sin(f) - np.sin(f0) * np.cos(f) * np.cos(l_ - l0))
    return x, y


def relieve(caja, margen=1.0):
    s, n, o, e = caja
    with h5py.File(ETOPO, "r") as f:
        lat, lon = f["lat"][:], f["lon"][:]
        i0, i1 = np.searchsorted(lat, s - margen), np.searchsorted(lat, n + margen)
        j0, j1 = np.searchsorted(lon, o - margen), np.searchsorted(lon, e + margen)
        z = f["z"][i0:i1, j0:j1].astype(float)
        lat, lon = lat[i0:i1], lon[j0:j1]
    z = gaussian_filter(z, 1.5)  # el mismo suavizado que el encaje de la pizarra: quita el ruido de un píxel
    # sólo el continente con su plataforma: fuera las islas sueltas del océano (Ascensión, Santa Elena, Trindade…),
    # que no entran en el encaje y confunden al recortar
    trozos, _ = label(z > -200)
    mayor = np.argmax(np.bincount(trozos.ravel())[1:]) + 1
    z = np.where(trozos == mayor, z, np.minimum(z, -1000.0))
    lon2, lat2 = np.meshgrid(lon, lat)
    dentro = (lat2 >= s) & (lat2 <= n) & (lon2 >= o) & (lon2 <= e)
    return lat2, lon2, np.where(dentro, z, np.nan)


def borde_caja(caja, lat0, lon0, pasos=200):
    s, n, o, e = caja
    tramos = [(np.full(pasos, s), np.linspace(o, e, pasos)), (np.linspace(s, n, pasos), np.full(pasos, e)),
              (np.full(pasos, n), np.linspace(e, o, pasos)), (np.linspace(n, s, pasos), np.full(pasos, o))]
    lat = np.concatenate([t[0] for t in tramos])
    lon = np.concatenate([t[1] for t in tramos])
    return laea(lat, lon, lat0, lon0)


def pagina(pdf, nombre, datos, por_donde):
    lat0, lon0 = datos["centro"]
    lat, lon, z = datos["relieve"]
    x, y = laea(lat, lon, lat0, lon0)
    mm = lambda km: km * 1e6 / ESCALA  # km del terreno → mm del papel
    fig = plt.figure(figsize=(A4[0] / 25.4, A4[1] / 25.4))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, A4[0])
    ax.set_ylim(0, A4[1])
    ax.set_aspect("equal")
    ax.axis("off")
    # el mapa, centrado en la zona libre entre la cabecera y el pie
    bx, by = borde_caja(datos["caja"], lat0, lon0)
    cx = A4[0] / 2 - mm((bx.min() + bx.max()) / 2)
    cy = (A4[1] - 33 + 33) / 2 - mm((by.min() + by.max()) / 2)
    X, Y = cx + mm(x), cy + mm(y)
    ax.contourf(X, Y, z, levels=[-200, 0], colors=[PLATAFORMA])
    ax.contourf(X, Y, z, levels=[0, 9000], colors=[TIERRA])
    corte = por_donde == "costa"
    ax.contour(X, Y, z, levels=[0], colors=[TINTA], linewidths=1.6 if corte else 0.8)
    ax.contour(X, Y, z, levels=[-200], colors=[AZUL], linewidths=0.8 if corte else 1.6,
               linestyles="solid" if not corte else "dashed")
    ax.plot(cx + mm(bx), cy + mm(by), color=GRIS, lw=0.8, ls=(0, (1, 2)))
    # cabecera
    accion = ("Recorta por la COSTA (línea negra gruesa)" if corte
              else "Recorta por el BORDE SUMERGIDO, a 200 m de profundidad (línea azul gruesa)")
    ax.text(12, A4[1] - 14, f"{nombre} · el encaje de Wegener", fontsize=15, weight="bold", color=TINTA, va="center")
    ax.text(12, A4[1] - 22, accion, fontsize=10.5, color=AZUL if not corte else TINTA, va="center")
    ax.text(12, A4[1] - 28.5, "Tierra adentro, por la línea de puntos gris. Imprime todas las páginas al 100 %.",
            fontsize=8.5, color=GRIS, va="center")
    # leyenda y escala
    ly = 24
    ax.add_patch(plt.Rectangle((12, ly - 2), 6, 4, color=TIERRA))
    ax.text(20, ly, "tierra", fontsize=8, va="center")
    ax.add_patch(plt.Rectangle((40, ly - 2), 6, 4, color=PLATAFORMA))
    ax.text(48, ly, "plataforma continental, hasta 200 m de profundidad", fontsize=8, va="center")
    ax.plot([140, 140 + mm(1000)], [ly, ly], color=TINTA, lw=2)
    ax.plot([140, 140], [ly - 1.5, ly + 1.5], color=TINTA, lw=1)
    ax.plot([140 + mm(1000), 140 + mm(1000)], [ly - 1.5, ly + 1.5], color=TINTA, lw=1)
    ax.text(140 + mm(500), ly + 3, "1000 km", fontsize=8, ha="center")
    ax.text(140 + mm(500), ly - 4, "escala 1:25 000 000", fontsize=7, ha="center", color=GRIS)
    ax.text(12, 12, "Relieve: ETOPO 2022, NOAA NCEI (dominio público). Proyección azimutal equivalente de Lambert centrada en "
            f"{abs(lat0):.0f}° S, {abs(lon0):.0f}° {'O' if lon0 < 0 else 'E'}.", fontsize=6.5, color=GRIS)
    ax.text(12, 8, "GinCol Lab · «De la deriva continental a la tectónica de placas» · CC BY 4.0", fontsize=6.5, color=GRIS)
    pdf.savefig(fig)
    plt.close(fig)


def main():
    for d in CONTINENTES.values():
        d["relieve"] = relieve(d["caja"])
    with PdfPages(SALIDA) as pdf:
        for por_donde in ("costa", "borde"):
            for nombre, d in CONTINENTES.items():
                pagina(pdf, nombre, d, por_donde)
        info = pdf.infodict()
        info["Title"] = "Mapa para recortar: el encaje de Sudamérica y África"
        info["Author"] = "GinCol Lab"
    print(SALIDA)


if __name__ == "__main__":
    main()

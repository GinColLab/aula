"""Las dos líneas de la clase 5: la temperatura real y la temperatura de fusión, del suelo al centro de la Tierra.

Son estimaciones, no medidas, y se dibujan como tales: hasta 660 km el margen es de unos ±40 °C; en el borde del núcleo y en
el del núcleo interno, de unos ±500 °C. Lo que no depende de esas cifras son los hechos que la gráfica ordena (las S cruzan
el manto, no cruzan el núcleo externo y el núcleo interno vibra como un sólido): la temperatura exacta se mueve con el
margen, pero en el borde del núcleo interno las dos líneas se cruzan por definición (Labrosse, 2014; Mita y otros, 2024).

Fuentes y discusión, en `datos.md`, junto a este programa, sección E. Deja temperaturas.json y comprueba lo que dice la clase:

    uv run python clases/biologia-geologia-ccaa-t01-c5/temperaturas.py
"""

import json
from pathlib import Path

import numpy as np

AQUI = Path(__file__).resolve().parent

# La temperatura real (km, °C).
#   0–100 km: la litosfera, por donde el calor sale conduciendo: del suelo a unos 1350 °C, entre el convenio de los
#             1300 °C (Porter y Reid, 2021) y los 1399 °C de la adiabata a 100 km (Katsura, 2022, tabla 2).
#   100–2690: Katsura (2022), tabla 2; a 410 y 660 km, la media de encima y debajo de cada cambio de fase.
#   2690–2891: la capa límite de la base del manto, unos 200 km (Lay y otros, 2008: de 500 a 1800 K en unos 200 km);
#             3766 °C es el empalme con la adiabata del núcleo, dentro de lo que dan Lay y otros (2008), 3300–4300 K.
#   Núcleo:   adiabata T = T_ICB (ρ/ρ_ICB)^1,5 con T_ICB = 5500 K (Alfè y otros, 2002; Anzellini y otros, 2013, menos
#             700 K; Labrosse, 2014). Centro: unos 100 °C más que el borde, en el medio de lo que se estima (+0 a +200).
REAL = [(0, 15), (15, 330), (30, 620), (50, 950), (75, 1230), (100, 1350), (140, 1415), (200, 1445), (300, 1490),
        (410, 1556), (520, 1620), (660, 1704), (1000, 1810), (1500, 1960), (2000, 2110), (2500, 2240), (2690, 2290),
        (2750, 2480), (2800, 2760), (2850, 3220), (2891, 3766),
        (3500, 4305), (4000, 4664), (4500, 4951), (5000, 5172), (5150, 5227), (5700, 5290), (6371, 5330)]

# La temperatura de fusión de la roca del manto, seca (km, °C): Hirschmann (2000) hasta 50 km; Herzberg y otros (2000)
# hasta 660 km; de ahí abajo, la media de Fiquet y otros (2010) y Andrault y otros (2011).
FUSION_ROCA = [(0, 1120), (25, 1215), (50, 1308), (75, 1420), (100, 1520), (150, 1660), (200, 1780), (300, 1920),
               (410, 2030), (520, 2100), (660, 2165), (1000, 2496), (1500, 2896), (2000, 3259), (2500, 3605),
               (2800, 3813), (2891, 3895)]

# La de la aleación del núcleo (km, °C): cuenta propia, sólo para dibujar: la recta local de 9 K/GPa de Labrosse (2014,
# tabla 1) desde los 5500 K del borde del núcleo interno, con las presiones del PREM. En el núcleo interno, orientativa.
FUSION_ALEACION = [(2891, 3489), (3500, 4056), (4000, 4482), (4500, 4853), (5000, 5155), (5150, 5227), (5700, 5400),
                   (6371, 5542)]


def en(tabla, z):
    t = np.array(tabla, dtype=float)
    return float(np.interp(z, t[:, 0], t[:, 1]))


def main() -> None:
    salida = {
        "aviso": "Estimaciones para dibujar, no medidas. Margen: ±40 °C hasta 660 km; unos ±500 °C en los bordes del núcleo.",
        "real": REAL, "fusion_roca": FUSION_ROCA, "fusion_aleacion": FUSION_ALEACION,
    }
    (AQUI / "temperaturas.json").write_text(json.dumps(salida, ensure_ascii=False, indent=1))

    print("prof  real  fusión  margen")
    for z in (0, 50, 100, 150, 200, 410, 660, 1500, 2800):
        print(f"{z:5d} {en(REAL, z):6.0f} {en(FUSION_ROCA, z):6.0f} {en(FUSION_ROCA, z) - en(REAL, z):6.0f}")
    print(f"borde del núcleo: real {en(REAL, 2891):.0f}, roca {en(FUSION_ROCA, 2891):.0f}, aleación {en(FUSION_ALEACION, 2891):.0f}")
    for z in (3500, 4000, 5000, 5150, 5700, 6371):
        print(f"{z:5d} {en(REAL, z):6.0f} {en(FUSION_ALEACION, z):6.0f} {en(FUSION_ALEACION, z) - en(REAL, z):6.0f}")

    # Lo que la clase afirma de la gráfica
    for z in range(0, 2891, 5):
        assert en(REAL, z) < en(FUSION_ROCA, z), f"en el manto la real pasa de la fusión a {z} km"
    for z in range(2891, 5150, 5):
        assert en(REAL, z) >= en(FUSION_ALEACION, z), f"en el núcleo externo la real queda bajo la fusión a {z} km"
    for z in range(5155, 6371, 5):
        assert en(REAL, z) < en(FUSION_ALEACION, z), f"en el núcleo interno la real pasa de la fusión a {z} km"
    menor = min((en(FUSION_ROCA, z) - en(REAL, z), z) for z in range(60, 400))
    print(f"lo más cerca arriba: {menor[0]:.0f} °C a {menor[1]} km; salto de la fusión en el borde: "
          f"{en(FUSION_ROCA, 2891) - en(FUSION_ALEACION, 2891):.0f} °C")

    # El tiempo de Maxwell del manto: τ = η/μ
    ano = 365.25 * 86400
    for mu in (65.6e9, 80e9, 190e9, 294e9):
        print(f"η = 10²¹ Pa·s, μ = {mu / 1e9:.0f} GPa: τ = {1e21 / mu / ano:.0f} años")
    print(f"manto / brea: {1e21 / 2.3e8:.1e} veces más viscoso")
    # La marca de 1731: casi 2 m en 295 años; 1731–2026
    print(f"1,8 m en {2026 - 1731} años: {1800 / (2026 - 1731):.1f} mm/año")


if __name__ == "__main__":
    main()

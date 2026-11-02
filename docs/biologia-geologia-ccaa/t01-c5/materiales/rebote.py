"""La subida de Escandinavia, calculada: lo que hace un manto viscoso bajo un casquete de hielo que crece y se va.

Es el modelo de Haskell (1935) en su forma más sencilla: un semiespacio viscoso de una sola viscosidad, de densidad
uniforme, sin litosfera y en un corte plano. Cada ondulación de la superficie, de número de onda k, relaja hacia su
equilibrio con un tiempo propio:

    τ(k) = 2 η k / (ρ g)

de manera que las ondulaciones anchas tardan más. El equilibrio es la isostasia: bajo una columna de hielo de espesor h, la
superficie se hunde ρ_hielo · h / ρ_manto.

El flujo que acompaña a una ondulación que sube o baja W cos(kx), a una profundidad z, es la solución de Stokes del
semiespacio (incompresible, sin deslizamiento lateral en la superficie):

    subida:  W (1 + k z) e^(−k z) cos(k x)
    lateral: −W k z e^(−k z) sen(k x)

Como lo que se mueve es muy poco (cientos de metros frente a miles de kilómetros), la posición de cada partícula es
lineal en lo hundido en cada instante, y se puede dibujar exagerada.

    uv run python clases/biologia-geologia-ccaa-t01-c5/rebote.py

Deja rebote.json. No es un modelo de Escandinavia: es la física de Haskell con cifras redondas (hielo de 2,5 km,
η = 10²¹ Pa·s). Sirve para dibujar y para comprobar el orden de magnitud frente a lo medido (casi 1 cm/año, unas decenas
de metros por subir y unos 285 m de la Costa Alta).
"""

import json
from pathlib import Path

import numpy as np

AQUI = Path(__file__).resolve().parent
ETA = 1e21            # Pa·s
RHO_M, RHO_I = 3300.0, 917.0
G = 9.8
ANO = 365.25 * 86400
H_MAX = 2500.0        # m de hielo
ANCHO = 700e3         # m: el semiancho del casquete
L = 12000e3           # m: el dominio periódico
N = 2048
T = np.arange(-60000.0, 0.0 + 1, 50.0)   # años; hoy, 0


def hielo(t: float) -> float:
    """Espesor máximo: crece de −60 000 a −20 000 años, se queda y se va entre −14 000 y −9700, cuando el hielo dejó la
    Costa Alta (Stroeven y otros, 2016; UNESCO: 9600 años)."""
    if t < -20000:
        return H_MAX * (t + 60000) / 40000
    if t < -14000:
        return H_MAX
    if t < -9700:
        return H_MAX * (-9700 - t) / 4300
    return 0.0


def main() -> None:
    x = (np.arange(N) - N // 2) * L / N
    forma = np.clip(1 - (x / ANCHO) ** 2, 0, None) ** 0.5   # el perfil de un casquete, redondeado por arriba
    k = 2 * np.pi * np.fft.rfftfreq(N, L / N)
    tau = np.zeros_like(k)
    tau[1:] = 2 * ETA * k[1:] / (RHO_M * G) / ANO   # años
    f = np.fft.rfft(forma)
    w_k = np.zeros_like(f)   # lo hundido, en cada modo (positivo = hundido)
    dt = T[1] - T[0]
    guardado, centro, serie = [], [], []
    for t in T:
        eq = RHO_I / RHO_M * hielo(t) * f
        # exacto para un equilibrio que no cambia en el paso
        w_k[1:] = eq[1:] + (w_k[1:] - eq[1:]) * np.exp(-dt / tau[1:])
        guardado.append(w_k.copy())
        centro.append(float(np.fft.irfft(w_k, N)[N // 2]))
        serie.append(t)
    centro = np.array(centro)
    hoy = centro[-1]
    velocidad = (centro[-2] - centro[-1]) / dt * 1000   # mm/año
    k0 = np.pi / (2 * ANCHO)
    print(f"τ del casquete: {2 * ETA * k0 / (RHO_M * G) / ANO:.0f} años")
    print(f"hundido máximo: {centro.max():.0f} m (equilibrio: {RHO_I / RHO_M * H_MAX:.0f} m)")
    i_fin = int(np.argmin(abs(T + 9700)))
    print(f"al irse el hielo quedaba: {centro[i_fin]:.0f} m; hoy quedan {hoy:.0f} m; subido desde entonces: {centro[i_fin] - hoy:.0f} m")
    print(f"subida hoy: {velocidad:.1f} mm/año")

    # Lo que dibuja la pizarra: 240 instantes, 241 puntos de la superficie, y partículas del manto
    tiempos = np.linspace(0, len(T) - 1, 240).astype(int)
    xs_km = np.linspace(-2400, 2400, 241)
    malla = np.arange(N)[(x >= -2400e3) & (x <= 2400e3)]
    sup = []
    for i in tiempos:
        w = np.fft.irfft(guardado[i], N)
        sup.append(np.interp(xs_km * 1e3, x[malla], w[malla]).round(1).tolist())
    # partículas, repartidas en filas (hasta 2100 km), desplazadas con la solución de Stokes
    px0 = np.linspace(-2300e3, 2300e3, 25)
    pz0 = np.array([350e3, 800e3, 1300e3, 1900e3])
    PX, PZ = [a.ravel() for a in np.meshgrid(px0, pz0)]
    pos = []
    for i in tiempos:
        wk = guardado[i]
        dx, dy = np.zeros_like(PX), np.zeros_like(PX)
        # sólo los modos que pesan
        for m in range(1, 200):
            a = 2 * np.abs(wk[m]) / N
            fase = np.angle(wk[m])
            K = k[m]
            # la x de la transformada empieza en x[0]
            fase_x = K * (PX - x[0])
            c = a * np.cos(fase_x + fase)
            s = a * np.sin(fase_x + fase)
            # w>0 es hundido: la subida es −w
            dy += -c * (1 + K * PZ) * np.exp(-K * PZ)
            dx += s * K * PZ * np.exp(-K * PZ)
        pos.append(np.stack([dx, dy], axis=1).round(1).tolist())
    salida = {
        "aviso": "Modelo de Haskell con cifras redondas: η = 10²¹ Pa·s, hielo de 2,5 km, corte plano. Sólo para dibujar.",
        "años": [float(T[i]) for i in tiempos],
        "x_km": xs_km.tolist(),
        "hundido_m": sup,
        "hielo_m": [round(hielo(float(T[i])), 1) for i in tiempos],
        "ancho_hielo_km": ANCHO / 1e3,
        "particulas_x0_km": (PX / 1e3).tolist(),
        "particulas_z0_km": (PZ / 1e3).tolist(),
        "particulas_d_m": pos,
        "comprobacion": {"subida_hoy_mm_ano": round(float(velocidad), 1), "quedan_m": round(float(hoy), 0),
                         "subido_m": round(float(centro[i_fin] - hoy), 0)},
    }
    (AQUI / "rebote.json").write_text(json.dumps(salida))
    print("partículas:", len(PX), "instantes:", len(tiempos))
    d = np.array(pos[0])
    print("control: desplazamiento máx", np.abs(np.array(pos[100])).max(axis=(0, 1)))
    # hacia dónde se mueve el manto bajo el hielo cuando está hundido: a profundidad, hacia fuera (x>0 → dx>0)
    p = np.array(pos[150])
    q = (PX > 300e3) & (PX < 1500e3) & (PZ == 800e3)
    print("a 800 km, a la derecha del hielo, dx medio (debe ser > 0 = hacia fuera):", p[q, 0].mean())


if __name__ == "__main__":
    main()

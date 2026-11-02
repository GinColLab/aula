# Datos verificados · Biología, Geología y CCAA · Tema 1, clase 5: «Dos maneras de cortar la Tierra»

Dosier de investigación previo al guion (artículo 6 de la Constitución), hecho el 01/11/2026. No se ha tocado ningún guion
ni escena. Todas las peticiones web, con User-Agent genérico. Cálculos propios en
`/private/tmp/claude-501/-Users-gincol-proyectos-ia-personales-brainstorming/e5aff511-57ff-4aa8-b6db-6871b769a05d/scratchpad/calc/`
(`curvas.py`, `prem_calc.py`), con la tabla PREM de `clases/biologia-geologia-ccaa-t01-c4/medios/densidad-prem.json`.

**Cómo leer cada fila.** **[L]**: leído en el texto del documento (PDF o HTML extraído; la cita es literal, comprobada con
`grep`). **[R]**: sólo el resumen, el abstract o un fragmento devuelto por el buscador; la cita es fiel al fragmento, pero
no he visto el documento entero. Veredictos: CONFIRMADO, MATIZAR, NO SE SOSTIENE, NO CONFIRMABLE.

**Reutilizado de otras clases, y dicho aquí:** Pratt, Airy, Dutton (clase 2, F1); presiones del PREM en los bordes (clase 2,
`verificacion-datos-2.md`); masa y momento de inercia (clase 2, sección H; ficha [7][17]); Lehmann, 220 km (clase 4); Moho del
Macizo Ibérico (clase 4); Dziewonski y Gilbert 1971 (clase 4); gradiente adiabático y temperaturas de Earle (clase 2, 22–24).

---

## Lo que NO se puede decir (resumen)

1. **«La discontinuidad de Repetti es la de 660 km», como historia.** NO SE SOSTIENE. Repetti (tesis en Saint Louis, hacia
   1928–1930) describió algo a **unos 900–970 km**, otra cosa. Sólo manuales ibéricos e italianos llaman «de Repetti» a la de 660 km;
   la literatura internacional dice «discontinuidad de 660 km». La ficha y la auditoría dicen lo contrario: hay que corregirlas (D15).
2. **«Celsius talló la marca de 1731»** y **«la velocidad salió de Lövgrund»**. MATIZAR. La talló **Johan Rudman**, maestro de
   matemáticas, siguiendo instrucciones de Celsius (Lyell escribió mal «Rudberg»). La velocidad de 1743 salió de **otra** piedra,
   la de Iggön (C10).
3. **«Un X % de universitarios dibuja el manto líquido» (McAllister).** NO SE SOSTIENE: McAllister no da ese porcentaje. Su 38 %
   es del **núcleo interno** líquido (38 % de 90 dibujos). Sólo se puede decir «a menudo» (G28).
4. **«Parnell empezó en 1927 y vertió la brea en 1930»** está al revés: la brea se **vertió en 1927**; el tallo se **cortó en 1930** (B6).
5. **«Longpré y otros 2022, *Science Advances*»**: no he encontrado ese artículo. Los de *Science Advances* son Dayton y otros
   (2023) y Ubide y otros (2023); Longpré firma en *Nature Geoscience* (2025) (A2).
6. **«El magma de La Palma se formó a 25 km».** Lo que se mide es dónde se **almacenó** (unos 15–30 km). Dónde se fundió, no (A2).
7. **Cualquier temperatura del interior como cifra exacta o «medida».** Son estimaciones. Hasta 660 km, ±40 °C; en el borde
   núcleo-manto, ±500 °C; en el borde del núcleo interno, ±500 °C (E20).
8. **«El hierro funde a 6000 °C»** como cifra cerrada: según el método, de 5230 a 6080 °C a 330 GPa. Mejor «entre unos 5500 y 6000 °C» (E21).
9. **«El núcleo tiene un 10 % de elementos ligeros».** Ese 10 % es el **déficit de densidad** de Birch (hoy, 5–10 %), no el
   porcentaje en peso de esos elementos (E24).
10. **«Haskell midió la viscosidad del manto».** La **calculó** con un modelo sencillo a partir de curvas de levantamiento ya
    publicadas. No he leído su artículo: lo que sigue es de citas posteriores (B4).
11. **«El tiempo de Maxwell (unos cientos de años) es lo que tarda en recuperarse Escandinavia».** No: esa recuperación tarda miles de años (B5).
12. **«La astenosfera está parcialmente fundida»**, como hecho general. Se discute: bajo continentes apenas hay fundido, y donde lo
    hay es muy poco (0,1–0,3 %, con estimaciones de hasta el 1 %). Lo seguro: casi toda sólida, blanda porque está cerca de fundir (D14).
13. **«La zona de transición no cambia en nada»**: a 410 y 520 km sí es la misma roca recolocada; a 660 km el cambio de fase es lo
    aceptado, pero queda debate sobre si hay además cambio químico (D17). Un material oficial portugués atribuye Repetti a un cambio de composición.
14. **«El hielo y el manto fluyen por el mismo mecanismo»**, tal cual. Sí «el mismo tipo»: reptación de cristales. La ley del
    hielo no se explica con un único mecanismo (B7).
15. **«Nadie ha visto ondas S en el núcleo interno»** ni **«se han visto, seguro»**: PKJKP sigue en discusión (F26).
16. **Cifras únicas de La Palma**: 1180, 1219 o 1241 ha; 1676 o 2988 edificaciones. Dependen de quién y cómo cuenta (A1).
17. **«286 m» como cifra de la UNESCO**: la UNESCO dice «del orden de 285 m» (C11). **«Quedan 100 m por subir»**: las
    estimaciones van de 50 a 100 m (C11). **«3 km de hielo»**: las fuentes van de 2 a más de 3 km (C11).
18. **La nota de Yaemsiri (3,47 mm/mes)**: son 22 personas; una muestra tan pequeña no se usa como prueba. Basta «unos centímetros al año» (B3).

Lo que **sí** se sostiene y da mucho juego: que la temperatura real se acerca a la fusión de la roca en los **dos extremos** del manto, y
que la curva de fusión **salta hacia abajo** en el borde del núcleo porque cambia el material, no la temperatura (E22).

---

## A. La Palma 2021

### 1. Fechas, superficie, edificios

**Veredicto: CONFIRMADAS las fechas; MATIZAR superficie y edificios.**

| Dato | Valor | Fuente 1 | Fuente 2 | Matiz |
|---|---|---|---|---|
| Inicio | 19/09/2021, 15:10 hora local, Cabeza de Vaca | Martín Luis (2023), *Cosmológica* 3, 21–32, ULL ([ficha](https://portalciencia.ull.es/documentos/651b045d3b6943447b451a7e)) [R] | D'Auria y otros (2022), *Sci. Rep.* 12, 17654 [L] | — |
| Fin de la actividad | 13/12/2021, 22:21 | Martín Luis (2023) [R] | Wikipedia con AP [R]; D'Auria («active for 85 days») [L] | El fin **oficial** se declaró el **25/12/2021**, tras doce días sin actividad (CBC y BBC, vía Wikipedia [R]) |
| Duración | 85 días; oficialmente «85 días y 8 horas» | Martín Luis (2023) [R] | Deia/EFE (19/09/2022) [R] | Con las dos horas de arriba salen 85 d 7 h 11 min (cálculo): decir «ochenta y cinco días» |
| Superficie de lava | **Unos 12 km², unas 1200 ha** | Copernicus (20/01/2022): «1,241 ha» ([enlace](https://www.copernicus.eu/en/node/11414)) [L] | *Bull. Volcanol.* (2023), [s00445-023-01700-w](https://link.springer.com/10.1007/s00445-023-01700-w): unos 12 km² [R]; Martín Luis: más de 12 km² [R] | También 1219 ha (al declararse el fin; fuente secundaria, sin poder atribuirla a PEVOLCA) y 1180 ha (Deia/EFE). Satélites y catastro miden distinto |
| Edificios | **Más de 1600** | Catastro/Cabildo: 1676 edificaciones, 1345 viviendas (Deia/EFE, 19/09/2022) [R] | Copernicus: 2988 «built-up structures» [L] | No son comparables: Copernicus cuenta construcciones |

**No leído:** el informe final del IGN (la página «Serie de La Palma» no cargó su contenido).

**Redacción segura:** «La erupción de La Palma de 2021 duró ochenta y cinco días, cubrió de lava unos doce kilómetros cuadrados y destruyó más de mil seiscientos edificios.»

### 2. De qué profundidad salió el magma

**Veredicto: MATIZAR.** Hay acuerdo en lo grueso y discrepancia en los detalles.

| Dato | Valor | Fuente | Cita |
|---|---|---|---|
| Almacén de magma | 7–25 km | D'Auria y otros (2022), *Sci. Rep.* 12, 17654, doi:10.1038/s41598-022-21818-9 [L] | «a large sub-crustal magma-filled rock volume intrusion extending from 7 to 25 km depth» |
| Almacenamiento según inclusiones de CO₂ en olivino | 15–27 km | Dayton y otros (2023), *Sci. Adv.* 9, eade7641 [L, resumen en Europe PMC] | «translating into depths of 15 to 27 km, which falls within the reported deep seismic zone recording the main melt storage reservoir» |
| Enjambres de 2017–2021 | 15–20 km (Resultados); 10–25 km (Discusión) | D'Auria y otros (2022) [L] | «seismic activity is recorded mainly at depths between 15 and 20 km» |
| Sismicidad durante la erupción | Dos grupos: 10–14 y 33–39 km | Del Fresno y otros (2023), *Nat. Commun.* 14, doi:10.1038/s41467-023-35953-y [L] | «two clusters at ~10-14 km and ~33-39 km depth, separated by an aseismic zone» |
| Almacenes (interpretación) | 9–13, 18–32 (pastoso) y 33–38 km | Del Fresno y otros (2023) [L] | «shallow (9–13 km), intermediate mushy (18–32 km), and deep (33–38 km) reservoir systems» |
| ¿Corteza o manto? | Manto superior, para el almacén principal | Del Fresno y otros (2023) [L] | «pre-eruptive magma storage occurs in upper mantle reservoirs at ~15–26 km depth and possibly also down to 50 km» |
| Moho bajo las islas | 10–12 km; otros, 14 km | D'Auria y otros (2022) [L] | «the Moho (i.e., the base of the oceanic crust) is at ~ 10–12 km below sea level» |
| Subida final | De 10 km a la superficie en menos de 7 días | D'Auria y otros (2022) [L] | «magma ascended from 10 km depth to the surface in less than 7 days» |

**Matices.** D'Auria llama «sub-crustal» a un volumen que empieza a 7 km, más arriba de su propio Moho (10–12 km). **«Longpré y otros 2022,
*Science Advances*» no aparece**: el trabajo de Longpré sobre esta erupción es *Nat. Geosci.* (2025), «Shifting melt composition
linked to volcanic tremor at Cumbre Vieja volcano» [R]. Otro de *Sci. Adv.*: Ubide y otros (2023), doi:10.1126/sciadv.adg4813 [R].
Dónde **se fundió** la roca no lo dice ninguno de estos datos.

**Frase segura:** «El magma de La Palma estaba guardado a unos quince o treinta kilómetros de profundidad, ya por debajo de la corteza, en el manto de arriba, y en la última semana subió hasta la superficie. El núcleo, a casi tres mil kilómetros, no tuvo nada que ver.»

---

## B. El manto sólido que fluye

### 3. Velocidad del flujo

**CONFIRMADO: unos centímetros al año.**

- **USGS**, [¿Flotan las placas sobre magma?](https://www.usgs.gov/faqs/are-tectonic-plates-floating-magma) (copia de Wayback, 2023; la web da 403) [L]: «over long geologic timescales the mantle can behave like a thick liquid that slowly flows at about the same rate that fingernails grow».
- **IRIS/EarthScope**, [FAQ](https://www.iris.edu/hq/faq/why_do_tectonic_plates_move) [R]: «which move at about the rate your fingernails grow: several centimeters (about one inch) per year». Se refiere a las placas.
- **USGS**, [¿A qué velocidad se mueven las placas?](https://www.usgs.gov/faqs/how-fast-do-tectonic-plates-move) [R]: «roughly at the same rate that your fingernails grow».
- **Matiz:** las uñas crecen unos 4 cm/año (3,47 mm/mes × 12; Yaemsiri y otros, 2010, *JEADV* 24, 420–423 [R]). Son 22 personas: una muestra tan pequeña no se usa como prueba. La comparación del USGS basta.

### 4. Viscosidad del manto, de la brea y rigidez

| Dato | Valor | Fuente 1 | Fuente 2 | Veredicto y matiz |
|---|---|---|---|---|
| Manto | 10²¹ Pa·s, media | Mitrovica (1996), *JGR* 101, 555–569 [R]: «The Haskell [1935] value of 10²¹ Pa s for mantle viscosity is a classic and enduring constraint» | Fernández, Alonso Chaves y Anguita (2013), *Enseñanza de las Ciencias de la Tierra* 21(1) [L]: de 10²⁰ a 10²¹ Pa·s, «que se incrementa en uno a dos órdenes de magnitud en el manto inferior» | CONFIRMADO como orden de magnitud. Mitrovica: 0,65–1,10 × 10²¹ Pa·s, media hasta unos 1200–1400 km |
| Haskell: qué hizo | Halló el valor **ajustando** un modelo a curvas de levantamiento ya publicadas, no midiendo | Fragmento de «Glacial-isostatic adjustment I: the forward problem» [R; no se pudo abrir, autores sin comprobar]: «Haskell (1935, 1936), using a Newtonian viscous half-space earth model with a constant density and viscosity, inferred an 'effective' (and now classic) viscosity value» | Fragmento de otro artículo sobre viscosidad [R]: dos lugares, «Angerman River, Sweden, and Oslo, Norway»; Haskell (1938), *Nature* 141, 411: la estimó con el levantamiento de Fenoscandia [R]; Whitehouse (2018), *ESurf* 6 [R]: la datación de De Geer permitió «the first estimate of the viscosity of the mantle» | MATIZAR. Haskell (1935), *Physics* 6, 265–269, doi:10.1063/1.1745329, y parte II (1936), *Physics* 7, 56–61. **Sin leer el original** (de pago). No digo qué curvas exactas usó |
| Brea | (2,3 ± 0,5) × 10⁸ Pa·s | Edgeworth, Dalton y Parnell (1984), *Eur. J. Phys.* 5, 198–200 ([PDF](https://tcd.ie/media/tcd/physics/pdfs/Edgeworth_article_1984.pdf)) [L] | UQ: «100 billion times more viscous than water» [R]; Wikipedia: unos 230 000 millones [R] | CONFIRMADO. Es la media de 1930–1979: depende mucho de la temperatura (de 7,3 × 10⁵ a 2,35 × 10⁹ Pa·s entre 29,8 y 9 °C, mismo artículo) |
| Manto frente a brea | Unos 4 × 10¹² veces más viscoso | Cálculo: 10²¹ / 2,3 × 10⁸ | — | «Billones de veces» |
| Rigidez μ | De unos 66 a 294 GPa | Cálculo con PREM (ρ·vs²): 68 GPa a 50 km; 65,6 a 220 km; 92 a 410; 123 a 660; 187 a 1000; 246 a 2000; 293,8 a 2891 km | Clase 4: «μ de 2,94 × 10¹¹» | CONFIRMADO. El «70–290» de la consigna vale |

### 5. Tiempo de Maxwell

**CONFIRMADO: τ = η/μ, unos cientos de años.**

- **Cálculo** con η = 10²¹ Pa·s: μ = 80 GPa, 396 años; μ = 190 GPa, 167 años; μ = 294 GPa, 108 años.
- **Fuente 1:** Valente y Correia (2023), arXiv:2307.08770, manuscrito para *A&A* [L]: «µ ≈ 80 GPa (Karato & Wu 1993) […] η ∼ 10²¹ Pa s (Karato & Wu 1993), which gives τe ∼ 400 yr».
- **Fuente 2:** Sharma, Thakur, Jose y Govindarajan, arXiv:2507.23532, «Viscosity variation in fluid flows across scales» [L]: «the viscous stress response of the mantle is generally modelled as that of a Maxwell material, with the relaxation time scale being a few hundred years (Peltier, 1974; Ribe, 2018)».
- **Matiz clave:** no es lo que tarda Escandinavia. La misma arXiv:2307.08770: el rebote sugiere «τe ≈ 4400 yr (Turcotte & Schubert 2002)». Una cosa es cuándo el material empieza a fluir y otra cuánto tarda un planeta entero en recolocarse.
- **Sin leer:** Turcotte y Schubert, Ranalli, Peltier (libros o artículos de pago).

**Frase segura:** «Si empujas el manto menos de unos cientos de años, responde como un sólido elástico; si empujas durante mucho más, fluye.»

### 6. Pitch drop de Queensland

**CONFIRMADO, corrigiendo las fechas de la consigna: la brea se vertió en 1927; el tallo se cortó en 1930.**

- **Edgeworth y otros (1984)** [L]: «set up in 1927 by Professor Thomas Parnell»; «in 1930 the sealed stem was cut».
- **UQ**, [página oficial](https://smp.uq.edu.au/pitch-drop-experiment) [R]: «He allowed the pitch to cool and settle for 3 years, and then in 1930 he cut the funnel's stem.»
- **Nueve gotas:** 1938, 1947, 1954, 1962, 1970, 1979, 1988, 2000, 2014 (UQ en Wikipedia [R]). La novena: abril de 2014; Wikipedia: tocó a la octava el 12/04 y se separó el 24/04, durante un cambio de vaso; otras fuentes dicen 17 o 24. Decir «abril de 2014».
- **Décima, a 01/11/2026:** ninguna fuente dice que haya caído. UQ: «sometime in the 2020s». Wikipedia, tabla: «ongoing». ScienceBlog (2026) e IFL Science (enero de 2026): sigue formándose; esta última: «you could be waiting until 2027» [R]. Ninguna fuente es de las últimas semanas: **mirar la cámara en directo antes de grabar**.
- Nadie ha visto caer una en Queensland; la de Dublín sí se grabó, el 11/07/2013 (Wikipedia [R]).

### 7. Cómo fluye un sólido cristalino

**CONFIRMADO, con matiz en el hielo.**

- **Fernández, Alonso Chaves y Anguita (2013)** [L], en español y abierta ([PDF](https://ariasmontano.uhu.es/bitstreams/338afbec-876d-45b8-a800-b5d2b04a93d8/download)): «la ductilidad de las rocas está producida en último término por el movimiento de los defectos cristalinos (difusión de vacantes, lugares de la red cristalina en los que falta algún átomo, y desplazamiento de dislocaciones, defectos lineales en el cristal cuyo movimiento permite que acabe deformándose) en el interior de cada grano». **Es la mejor fuente para la clase.** Y compara con el hielo: «Otro análogo valioso es el hielo de los glaciares. Vibra o se rompe al golpearlo con un martillo, pero fluye descendiendo por el valle».
- **Karato y Wu (1993)**, *Science* 260, 771–778 [R]: «The hot and shallow upper mantle flows by dislocation creep, whereas cold and shallow or deep upper mantle may flow by diffusion creep.» Sólo manto superior.
- **Hielo:** Behn, Goldsby y Hirth (2021), *The Cryosphere* 15, 4589 [R]: la ley de Glen (n ≈ 3) «is not explained by a single deformation mechanism»; dislocaciones, n ≈ 4; deslizamiento de bordes de grano, n ≈ 1,8.
- **¿Mismo mecanismo?** Mismo **tipo**: cristales que se deforman por defectos, más fácil cuanto más cerca de fundir. **No** exactamente el mismo.
- **Ondas S en hielo glaciar: sí.** Unos 1800 m/s: Kim y otros (2010), Fourcade (Antártida), P 3466 y S 1839 m/s [R]; Tsuji y otros (2012): hielo puro, unos 1800 m/s [R]. Es el argumento perfecto: el hielo deja pasar las S y aun así fluye, igual que el manto.

### 8. Velocidad de los glaciares

**CONFIRMADO como orden de magnitud.** SERC (Carleton) [R]: «about a foot a day», unos 100 m/año. Sermeq Kujalleq (Jakobshavn): más de 17 km/año en máximos (Joughin y otros, 2014, por la prensa y por EGU [R]). Hielo policristalino: Behn y otros (2021) [R]. Un glaciar típico va miles de veces más deprisa que el manto (100 m/año frente a unos centímetros, cálculo).

---

## C. Isostasia y Escandinavia

### 9. Pratt, Airy, Dutton

**CONFIRMADO; reutilizado de clase 2, F1 (puntos 57–63).** Fuentes primarias leídas allí:

- Pratt (1855), *Phil. Trans.* 145, 53–100: 15″,885 calculados frente a 5″,236 («more than three times»). **Matiz de F1:** son *diferencias* entre las desviaciones de dos estaciones, no la desviación de una plomada.
- Airy (1855), *Phil. Trans.* 145, 101–104: «may be compared with perfect correctness to the state of a raft of timber floating upon water». Advierte: «This fluidity may be very imperfect; it may be mere viscidity». Muy útil: Airy ya no pedía un líquido.
- Pratt (1859), *Phil. Trans.* 149, 745–778. En 1855 no propuso nada bajo las montañas.
- Dutton: nota en 1882 («isostacy»); propuesta pública el 27/04/1889 («I propose the name isostasy»); volumen impreso en 1892. **Decir 1889.**

### 10. Celsius y la marca de 1731

**MATIZAR: lo que suele contarse está incompleto.** Fuente principal: **Martin Ekman (2016)**, *The Man behind «Degrees Celsius»*, Summer Institute for Historical Geophysics, Åland, cap. 5.4, pp. 95–102 ([PDF, vía Wayback](https://web.archive.org/web/2022/https://www.historicalgeophysics.ax/books/degrees_celsius.pdf)) [L].

| Dato | Valor | Fuente 1 | Fuente 2 |
|---|---|---|---|
| Quién la talló | **Johan Rudman**, maestro de matemáticas, por instrucciones de Celsius | Ekman p. 100: «The mark was cut according to Celsius' instructions by Rudman» | Uppsala [R]: Celsius hizo «hugga in ett särskilt märke för medelvattennivån 1731». Lyell (1835): «carved by one Rudberg in 1731» [L]: **errata del nombre** |
| Dónde | Roca de focas de Lövgrund, cerca de Gävle | Ekman p. 100 | Lyell: «on a fixed rock of mica-schist […] twelve miles north-east» de Gefle |
| Qué es | Una línea horizontal y encima «1731» | Ekman p. 100 | Lyell, figura 10 |
| Para qué | «in order to make future generations able to determine this rate of change more accurately» | Ekman p. 100, citando a Celsius (1743) | Uppsala [R] |
| De dónde salió la velocidad | De **otra** piedra, **Iggön**: 8 pies en 168 años (1563–1731), 1,4 cm/año | Ekman pp. 96–98 | Whitehouse (2018) [R]; Uppsala: «drygt 1 cm/år» [R] |
| Velocidad real allí | 0,8 cm/año | Ekman p. 98 | — |
| Qué creía | Que bajaba el agua | Ekman p. 98: «although Celsius looked upon it as a water decrease» | Uppsala [R]: «vattenminskningen, idag känt som landhöjningen»; Lyell: «gradually sinking» |
| Linneo | Apoyó la bajada del agua, por los cordones de Gotland | Ekman p. 99: «Support came first from Linnaeus» | Zittel (1901) [R]: Linneo y Celsius la atribuían a que bajaba el agua |
| Oposición | Browallius, tras morir Celsius, por errores y por la Biblia | Ekman p. 100 | — (una fuente) |
| ¿Sigue ahí? | **Sí** | Ekman p. 100: «It is still there, only it is now nearly 2 m above mean sea level» | Weisse y otros (2021), *Earth Syst. Dynam.* 12, 871, fig. 2 [L]: «about 2 m below the 1731 mark» (foto de Ekman) |
| Cuánto ha subido | **Casi 2 m**, respecto al mar | Las mismas | Ekman: marca «a little more than 10 cm too high»; quedarían unos 1,8 m, unos 6 mm/año (cálculo). Una web de vela dice 1,65 m: sin autoridad |

**Quién entendió qué:**

- **Playfair (1802):** podía moverse la tierra y no el agua, porque el agua no puede bajar sólo ahí: Lyell (1835) cita «in order to depress or elevate the absolute level of the sea, by a given quantity, in any one place, we must depress or elevate it by the same quantity over the whole surface» [L].
- **Von Buch (1807):** Lyell [L]: anunció «that the whole country from Frederickshall in Sweden to Åbo in Finland […] was slowly and insensibly rising»; también Zittel [R].
- **Lyell (1834–1835):** **midió** la marca el 03/07/1834: «two feet six inches and a half above the mean level of the water», unos 77 cm, y le dijeron que sumara otras cuatro pulgadas, unos 10 cm, por el viento [L]. Halló ritmos distintos según el lugar, y concluyó que subía la tierra. Ekman p. 101: «leading him to the conclusion that the phenomenon must be a land uplift».
- **Jamieson (1865):** el peso del hielo. Whitehouse (2018) [R]: «the idea that an ice sheet could have depressed the land was first proposed by Jamieson (1865)»; Wolf (1993) [R].
- **De Geer (1890):** líneas de costa antiguas. Sólo fuentes secundarias [R]: NO CONFIRMABLE con dos buenas; mejor no datarlo.

Hoy hay marcas de 1731, 1831 y 1931; en 2031 cabrá una última (Ekman p. 101). **Dato precioso, de una sola fuente.**

**Frase segura:** «En 1731 Celsius mandó grabar una raya al nivel del mar en una roca del Báltico, para que los del futuro midieran cuánto cambiaba. Él creía que bajaba el agua. Hoy esa raya está a casi dos metros sobre el mar. Y un siglo después se entendió al revés: no baja el agua, sube la tierra.»

### 11. Velocidad, total y hielo

| Dato | Valor | Fuente 1 | Fuente 2 | Matiz |
|---|---|---|---|---|
| Máximo hoy | **Unos 10 mm/año** | Vestøl y otros (2019), *J. Geod.* 93, 1759–1779, NKG2016LU [L]: «a maximum absolute uplift of 10.3 mm/a near the city of Umeå»; respecto al geoide, «from 10.3 to 9.6 mm/a» | SMHI, [Framtida vattenstånd](https://www.smhi.se/kunskapsbanken/klimat/vattenstand-och-klimat/framtida-vattenstand-langs-kusten) [L]: «I Norra Kvarkenområdet är landhöjningen […] som störst, nästan 10 mm/år» | CONFIRMADO. Respecto al mar real, menos: unos 8 mm/año (Ekman p. 98) |
| Total en la Costa Alta | **Unos 285 m** desde que se fue el hielo | UNESCO, [lista 898](https://whc.unesco.org/en/list/898/) (Wayback) [L]: «the uplift has been in the order of 285 m which is the highest known ''rebound''» | UNESCO, documento de candidatura [R]: «in excess of 280m» | MATIZAR: los 286 m no están en la ficha de la UNESCO. Contando lo subido bajo el hielo, otras fuentes dan unos 800 m [R] |
| Lo que queda | **Del orden de 50–100 m** | Ekman (1991), *Terra Nova* 3 [R]: «of the order of 50 m, but the latter quantity is very difficult to determine» | NLS Finlandia ([enlace](https://www.maanmittauslaitos.fi/en/node/1835)) [R]: «there is still some 100 meters to rise» | Sjöberg: 80 m [R]. Decir «unas decenas de metros» |
| Hielo | **Unos 2–3 km** | NLS Finlandia [R]: unos 2 km | Vaasa [R]: «up to 3 kilometers»; candidatura UNESCO [R]: 3400–3700 m | No hay cifra única |
| Cuándo se fue | Máximo 26 500–20 000 años; final tras 9700 años; Costa Alta, hace 9600 | Stroeven y otros (2016), *QSR* 147 [R] | UNESCO [L]: «the last retreat of the ice from the High Coast 9,600 years ago» | CONFIRMADO |

### 12. Puertos que se quedaron en tierra

**CONFIRMADO.**

- **Luleå:** UNESCO, [lista 762](https://whc.unesco.org/en/list/762/) (Wayback) [L]: «a progressive, natural land upheaval that had by the 17th century made the harbour unusable, thus forcing citizens to relocate the community's commercial centre». El año **1649** lo dan Wikipedia y el folleto de Gammelstad (fundada en 1621, trasladada 28 años después) [R]. Decir «en 1649».
- **Más:** Östhammar se quejaba ya en 1491 de su puerto (NLS Finlandia [R], una fuente). Lyell (1835) [L] cuenta que en Gefle preparaban alejar el puerto de la ciudad, por «the continued fall of the water». Weisse y otros (2021) [L]: «Shallow harbors were gradually abandoned as the water level apparently declined».

---

## D. Las capas y los nombres

### 13. «Astenosfera»

**CONFIRMADO.** Barrell, J. (1914), «The strength of the Earth's crust. Part VI. Relations of isostatic movements to a sphere of weakness — the asthenosphere», *J. Geol.* 22(7), 655–683, doi:10.1086/622181 (Crossref: octubre de 1914) [L, en [archive.org](https://archive.org/details/strengthofearths00barrrich)].

- Cita: «It may then be called the sphere of weakness — the asthenosphere».
- Resumen previo: reunión de la American Philosophical Society, abril de 1914, *Science* 39, 842 (nota 1 del artículo) [L].
- **Dato para la clase:** el mismo artículo arranca con Pratt y el Himalaya, y su lista de capas pone *lithosphere, asthenosphere, centrosphere*. La palabra nació por la isostasia.
- Griego: ἀσθενής, «débil» (el propio Barrell lo traduce: *sphere of weakness*). RAE y Merriam-Webster bloquearon la descarga: el griego, sin segunda fuente leída hoy.
- Segunda fuente: Fernández y otros (2013) [L]: «Definido por Barrell en 1914».

### 14. «Litosfera» y por qué la astenosfera es blanda

| Dato | Valor | Fuente 1 | Fuente 2 | Veredicto |
|---|---|---|---|---|
| Nombre | Barrell la usa como capa rígida; idea previa de Love (1911); Daly (1940) | Barrell (1914) [L]: «the rigid lithosphere» | Wikipedia [R] | CONFIRMADO. No digo que Barrell inventara la palabra: Wikipedia sí, sin que lo haya comprobado |
| Grosor oceánica | De casi nada en la dorsal a unos 100–140 km | Wikipedia [R]: «about 140 kilometres» la más vieja | Fernández y otros (2013) [L]: «su espesor tiende asintóticamente hacia un valor cercano a los 100 km» | CONFIRMADO. Decir «hasta unos cien kilómetros» |
| Grosor continental | De unos 40 a más de 200 km | Porter y Reid (2021), *GRL* [R]: «∼40 km and >200 km» | Wikipedia: 40 a 280 km [R] | CONFIRMADO |
| Base | **Unos 1300 °C es una convención**, no un hecho | Porter y Reid (2021): «the intersection of a geotherm with the 1300°C adiabat» [R] | Otros usan 1000–1100 °C: Wikipedia, Goldschmidt 2014 [R] | MATIZAR |
| ¿Por qué blanda? | Está cerca de fundir; defectos móviles | Fernández y otros (2013) [L] | USGS [L]: «overall, these areas of melt are comparatively small» | CONFIRMADO |
| Fundido | Muy poco, y discutido | Debayle y otros (2020), *Nature* 586 [R]: tope 0,30 %, hasta 150–200 km bajo dorsales y puntos calientes; casi nada bajo continentes | Chantel y otros (2016), *Sci. Adv.* [R]: desde un 0,2 %; Hirschmann (2010) [R]: «small amounts of melt are thermodynamically stable throughout the LVZ» | MATIZAR |
| La discusión | Definición mecánica frente a sísmica | Fernández y otros (2013) [L]: «no tiene, por tanto, nada que ver con la definición sísmica ni con la presencia o ausencia de un pequeño porcentaje de fundido»; espesor de 400 a más de 600 km | Karato (2012), citado ahí | Cuadra con SM («manto sublitosférico») |

**Frase segura:** «La astenosfera es roca sólida casi entera. Es blanda porque está cerca de su temperatura de fusión, no porque esté fundida. Si hay algo fundido, es muy poco, y los científicos aún discuten cuánto.»

### 15. «Discontinuidad de Repetti»

**NO SE SOSTIENE la equivalencia de la ficha.**

| Pregunta | Respuesta | Fuente |
|---|---|---|
| Quién | William C. Repetti, S.J. (1884–1966), jesuita; en 1926 estudió geofísica con Macelwane en Saint Louis; doctorado con «a thesis on the discontinuities of the structure of the earth interior»; en 1928 fue a Manila | [Manila Observatory](https://archives.observatory.ph/english/repetti.php), citando a Udías (2003) [R] |
| Fecha | Kawakatsu y Niu la citan como «Repetti, W. C. thesis, St. Louis Univ. (1930)»; la consigna dice 1928 | Kawakatsu y Niu (1994), *Nature* 371, 301, ref. 8 [L] |
| A qué profundidad | **Hacia 900–970 km, no 660** | Anderson (AGU 2002) [L]: «Birch called attention to the Repetti Discontinuity near 900 km depth»; Bolt y otros (1968) [R]: «(Repetti) discontinuity at about 920 km»; 970 km, sólo en una web floja [R] |
| ¿Se usa fuera? | Casi nada, y para los 900 km. Lo normal: «660-km discontinuity» | Kawakatsu y Niu (1994) [L]; Niu y Kawakatsu (1997) [L], la discontinuidad de unos 920 km, sin decir «Repetti» en el texto |
| Libros ibéricos | La ponen en 660–700 km, entre manto superior e inferior; algunos dan 700–1000 km | DGE, Portugal [L]: «Situada a cerca de 660 km de profundidade, encontra-se a descontinuidade Repetti, que separa o manto superior do manto inferior. Esta separação deve-se a uma mudança na composição química»; Casa das Ciências y un recurso gallego [R] |

**No leí** la tesis ni ningún libro español que use el nombre con cifra. SM dibuja la de 660 km (auditoría); la auditoría dejó esto «por confirmar».

**Dato incidental:** ese material portugués da como causa un cambio químico; lo aceptado es un cambio de fase (D17). Un motivo más para no apoyarse en él.

**Redacción honesta:** «En tu libro quizá veas el nombre de Repetti para la frontera entre manto superior e inferior. Cuidado: en la ciencia internacional se llama, sin más, discontinuidad de los seiscientos sesenta kilómetros, y lo que Repetti estudió en 1930 estaba más abajo, hacia los novecientos.» **Corregir** la ficha (clase 5, «Lo que se ve en la curva») y `plan/auditorias/biologia-geologia-ccaa-t01.md`.

### 16. «Discontinuidad de Lehmann», 220 km

**CONFIRMADO; reutilizado de la clase 4** (`verificacion-datos.md`, p27b): Lehmann (1959), Bolt (1997, p. 298), Revenaugh y Jordan (1991), Schmerr (2012). SM: borde del núcleo interno.

### 17. Zona de transición y capa D″

**CONFIRMADO a grandes rasgos.**

| Profundidad | Cambio | Fuente 1 | Fuente 2 |
|---|---|---|---|
| 410 km | Olivino → wadsleyita | Katsura (2022), *JGR Solid Earth* 127, e2021JB023562 [L]: «The D410 is usually attributed to the olivine-wadsleyite transition in peridotite» | Kawakatsu y Niu (1994) [L]: «due to the phase transitions of olivine → spinel → perovskite + magnesiowustite» |
| 520 km | Wadsleyita → ringwoodita | Katsura (2022) [L], salto de +43 K | Wikipedia [R] |
| 660 km | Ringwoodita → bridgmanita + ferropericlasa | Deschamps y Cobden (2022), *Front. Earth Sci.* [L]: «the phase transformation from ringwoodite to bridgmanite and ferro-periclase» | Kawakatsu y Niu [L] |

- **¿La roca no cambia de composición, sólo la estructura?** Sí a grandes rasgos. Pero la peridotita no es sólo olivino, y Anderson (AGU 2002) [L] sugiere que la frontera a unos 900 km «may be the chemical interface between the upper and lower mantles». Kawakatsu y Niu: «rather universal (although still controversial)».
- **Frase segura:** «Los átomos son más o menos los mismos, pero la presión los obliga a colocarse en cristales más apretados.»
- **Capa D″:** Bullen. Wikipedia [R]: letras de A a G (1942); en 1949 partió la D en D′ y D″. Howell y Kisslinger (2000), *Eos* [R]: acreditan a Dahm (1936) la primera descripción. **El nombre es de Bullen; decir que él «la descubrió» sería discutible.** Sin leer a Bullen.

### 18. Las dos cortezas

| Dato | Valor | Fuente 1 | Fuente 2 | Matiz |
|---|---|---|---|---|
| Continental, espesor | 35–40 km | Christensen y Mooney (1995), *JGR* 100 [R]: 41,1 km | Huang y otros (2013), arXiv:1301.0365 [L]: 34,4 ± 4,1 km | El segundo incluye márgenes y plataformas. Decir «unos 35–40 km» |
| Continental, densidad | 2,83 g/cm³ | Christensen y Mooney [R] | — | Encaja con la clase 1 (granito 2,5–2,8) |
| Continental, composición | Tipo granito arriba; SiO₂ 61,8 % | Christensen y Mooney [R] | Ficha [3] | — |
| Oceánica, espesor | 7–8 km | Wikipedia [R]: «7±1 km» | Huang y otros [L]: 8,0 ± 2,7 km | White (1992) no leído |
| Oceánica, densidad | 3,0 g/cm³ | Wikipedia [R] | Ficha [3]: basalto 2,7–3,3 | Sin segunda fuente exacta: decir «unos 3» |
| Oceánica, composición | Basalto arriba, gabro abajo (más de dos tercios) | Wikipedia [R] | Ficha [3] | — |
| Oceánica, edad | Unos 180–200 Ma | Britannica [R]; Wikipedia, con Müller (2008) [R] | Earle [R]: 180 Ma | Mediterráneo oriental, quizá 280–340 Ma (Granot, 2016): discutido, «si es que es oceánica» [R]. Decir «casi nunca más de unos doscientos millones» |
| Continental, edad | Circón de 4400 Ma | Valley y otros (2014), *Nat. Geosci.* [R, por sci.news y Discover] | ANU [R] | Es un **grano mineral** de Jack Hills, no una roca. No decir «la corteza más antigua es una roca de 4400 millones» |
| Moho bajo la península | 31 km en el Macizo Ibérico | Clase 4: Mancilla y Díaz (2015) | ALCUDIA | **Reutilizado.** Sistema Central y Tajo, 33–35 km |
| Máximo | Más de 50 km bajo Pirineos y Rif | Díaz, Gallart y Carbonell (2016), *Tectonophysics* 692, 74–85 [R]: «up to values exceeding 50 km beneath the Pyrenees or the Rif Cordillera» | Otro estudio [R]: al menos 45–50 km | CONFIRMADO. El postprint del CSIC sigue bloqueado |

### 19. Nombres de los modelos

**CONFIRMADO, reutilizado de la auditoría** (`plan/auditorias/biologia-geologia-ccaa-t01.md`, H8): Valencia, Decreto 108/2022: «Modelo geoquímico y dinámico», «modelos geodinámico y geoquímico». Madrid, Decreto 64/2022: «composición… mecánica». Galicia: «composición e o comportamento». SM: «unidades geoquímicas» y «dinámicas». Oxford: «composicionales» y «dinámicas». Bruño: «estático» y «dinámico».

**Matiz:** «mecánico» lo sostiene Madrid, como «en función de su mecánica»; no he visto «modelo mecánico» literal.

---

## E. Las dos curvas

### 20. Temperatura real

K − 273,15 = °C. Presiones: PREM en los bordes (clase 2) y mi integración entre medias (que da 135,9, 329,3 y 365,0 GPa frente a los 135,75, 328,85 y 363,85 de la tabla: vale para dibujar).

| Prof. (km) | P (GPa) | T (K) | **T (°C)** | Margen | Fuente |
|---|---|---|---|---|---|
| 0 | 0 | — | unos 15 | — | Convención del dibujo |
| Unos 100 (base de la litosfera) | 3 | unos 1570 | **unos 1300** | Convención | Porter y Reid (2021) [R] |
| 100 (bajo la placa) | 3,1 | 1672 | **1399** | ± 36 | Katsura (2022), tabla 2 [L] |
| 200 | 6,4 | 1718 | **1445** | ± 37 | Katsura (2022) [L] |
| 410, encima / debajo | 13,7 | 1799 / 1860 | **1526 / 1587** | ± 39 | Katsura (2022) [L] |
| 660, encima / debajo | 23,5 | 1994 / 1960 | **1721 / 1687** | ± 40 | Katsura (2022) [L] |
| 2800 (antes de la capa límite) | 130,6 | 2587 | **2314** | ± 60 | Katsura (2022) [L] |
| 2891, borde núcleo-manto | 135,75 | unos 3700–4050 | **unos 3500–3800** | 3030–4030 | Lay y otros (2008): 3300–4300 K [L]; Deschamps y Cobden (2022): 3470–3880 K [L] |
| 5150, borde del núcleo interno | 328,85 | unos 5500 | **unos 5230** | 4880–5930 | Ver abajo |
| 6371, centro | 363,85 | unos 5500–5700 | **unos 5230–5430** | ± 500 | Cálculo propio |

**Dentro del núcleo externo** (adiabata propia, T = T_ICB (ρ/ρ_ICB)^1,5; γ = 1,5, el de Mita y otros; reproduce su cociente: 0,734 frente a 0,735):

| Prof. (km) | T (K) | T (°C) |
|---|---|---|
| 2891 | 4039 | 3766 |
| 3500 | 4578 | 4305 |
| 4000 | 4937 | 4664 |
| 4500 | 5224 | 4951 |
| 5000 | 5445 | 5172 |
| 5150 | 5500 | 5227 |

Con T_ICB = 5000 K, resta unos 370 °C arriba y 500 abajo; con 6000 K, súmalos.

**Cuánto se ponen de acuerdo:**

- **Hasta 660 km:** decenas de grados. Por eso Katsura ancla en los cambios de fase: es la parte más segura. Katsura (2010): 1830 ± 48 K a 410 km; revisado: 1839 ± 38 K.
- **Base del manto:** discrepan unos 150 K. Katsura (2010): 2730 ± 50 K a 2700 km [R]. Katsura (2022): 2587 ± 60 K a 2800 km, por un error de cálculo corregido. Lay (2008): 2500–2800 K. Andrault (2011): «2500 K ± 250 at 2700 km» [L].
- **Capa límite:** Lay (2008): salto de «500–1,800 K in temperature across a 200 km thick superadiabatic» capa.
- **Borde núcleo-manto:** Lay [L]: «loosely constrained CMB temperatures (TCMB) of 3,300–4,300 K (Fig. 2), which is a huge range for such an important Earth parameter». Deschamps y Cobden [L]: «from about 3000 K to 4500 K and more».
- **Borde del núcleo interno:**

| Estimación | T (K) | Fuente |
|---|---|---|
| Lay y otros (2008) | 5300–5650 | [L] |
| Fischer (2016), según la composición | 5150–6200 | Por Deschamps y Cobden (2022) [L] |
| Anzellini (2013) menos 700 ± 200 K | unos 5500 | ESRF [R] |
| Alfè y otros (2002, 2003) | 5600–5650 ± 600 | [L]; [R] |
| Labrosse (2014), tabla 1 | 5500–5700 | [L] |
| Sinmyo y otros (2019), techo | 5120 ± 390 | [R] |
| Mita y otros (2024) | 3730–5720 | [L]; bajos, si hay C e H |

- **Centro:** ningún dato directo. Con γ = 1,3–1,5, adiabata del núcleo interno: +180 a +210 K (cálculo). Si no es adiabático, menos; Deguen y otros (2013) lo tienen por subadiabático probablemente [R]. **Sólo se sostiene «poco más que el borde».** Earle: unos 5000 °C (clase 2); Universidad de Ehime: «5000 K or higher» (clase 2).
- **Sin leer:** Stacey y Davis (2008), Sumita, Boehler salvo la cifra citada.

### 21. Temperatura de fusión

**Roca (peridotita seca):**

| Prof. (km) | P (GPa) | Solidus (°C) | Fuente |
|---|---|---|---|
| 0 | 0 | **1120** | Hirschmann (2000), por el código de `terratools` [R] |
| 50 | 1,5 | 1308 | Interpolación lineal de `terratools` |
| 100 | 3,2 | **1520** | Herzberg y otros (2000), *G³*, T = 1086 − 5,7P + 390 ln P, 2,7–22,5 GPa [R, abstract y código] |
| 200 | 6,5 | **1780** | Herzberg |
| 410 | 13,8 | **2030** | Herzberg |
| 660 | 23,5 | **2165** | Herzberg (2172 a 22,5 GPa) y Andrault (2163): empalman |
| 1000 | 38,7 | 2406–2587 | Andrault (2011) [L] / Fiquet (2010) |
| 1500 | 62,2 | 2769–3023 | Ídem |
| 2000 | 87,0 | 3140–3378 | Ídem |
| 2500 | 113,6 | 3522–3689 | Ídem |
| 2800 | 130,6 | 3762–3864 | Ídem |
| 2891 | 135,75 | **unos 3880–3910** | Fiquet: 4180 ± 150 K; Andrault: 4150 ± 150 K |
| 2891, estudios bajos | 135,75 | **3160–3300** | Nomura (2014): 3570 ± 200 K [R]; Kim (2020): 3430 ± 130 K (por Mita) [L] |

- Andrault [L]: T = T₀ (P/a + 1)^(1/c), T₀ = 2045 K, a = 92 GPa, c = 1,3. Da 4107 K a 135,75 GPa, no 4150: dentro del error.
- Los valores de Fiquet entre 36 y 135 GPa son el ajuste de `terratools`, no del artículo.
- **Sin leer:** Hirschmann (2000) y Fiquet (2010) enteros (403). Las cifras de 1120 °C y 4180 K están en dos fuentes cada una.
- **A presión ambiente:** 1120 °C (la consigna decía unos 1100, y vale). **A 100 km:** unos 1520 °C, secos.
- **Con agua:** Katsura (2022) [L], peridotita con 140 ppm de H₂O: 1590 ± 10 K (1317 °C) a 1,5 GPa.

**Hierro puro:**

| Punto | P (GPa) | T (K) | T (°C) | Fuente |
|---|---|---|---|---|
| Superficie | 0 | 1811 | **1538** | Wikipedia y periodictable.com [R] |
| Borde núcleo-manto | 136 | 4300 ± 250 | **4027** | Li y otros (2020), *GRL* 47, doi:10.1029/2020GL087758 [R, abstract en Crossref] |
| Borde del núcleo interno | 330 | 5500 ± 220 | 5227 | Sinmyo y otros (2019), *EPSL* 510 [R] |
| | | 5950 ± 400 | 5677 | Li y otros (2020) [R] |
| | | 6225 ± 42 | 5952 | Rao y otros, arXiv:2512.25061, preprint [L] |
| | | 6230 ± 500 | 5957 | Anzellini y otros (2013), *Science* 340 [R, clase 2] |
| | | 6230 ± 540 | 5957 | Kraus y otros (2022), según el preprint; la cifra, sin confirmar en primaria |
| | | 6350 ± 600 | 6077 | Alfè (2003) [R] |
| | | 4850 ± 200 | 4577 | Boehler (1993), *Nature* 363; superada |
| Centro | 364 | unos 6500 | unos 6230 | Ajuste de arXiv:2512.25061, 307–352 GPa: extrapolación propia |

**Aleación del núcleo** (dibujo, T_ICB = 5500 K, pendiente 9 K/GPa de Labrosse 2014, tabla 1 [L]):

| Prof. (km) | P (GPa) | Fusión (K) | Fusión (°C) | T real − fusión (°C) |
|---|---|---|---|---|
| 2891 | 135,75 | 3762 | **3489** | +277 |
| 3500 | 198,8 | 4330 | 4056 | +248 |
| 4000 | 246,1 | 4755 | 4482 | +182 |
| 4500 | 287,3 | 5126 | 4853 | +98 |
| 5000 | 320,8 | 5428 | 5155 | +17 |
| 5150 | 328,85 | 5500 | **5227** | 0 |
| 6371 | 363,85 | 5815 | 5542 | −115 a −315 |

- Esta tabla es **mi cuenta**, una recta local, no una curva publicada. Es sólo para el dibujo.
- La rebaja respecto al hierro: Alfè y otros (2002) [L]: «ΔT = −700 ± 100 K»; ESRF [R]: 700 ± 200 K; Mita y otros (2024) [L]: el eutéctico Fe-FeH, hasta 1440 K por debajo del hierro.
- Comprobación: la adiabata sube 7,6 K/GPa (cálculo); la fusión, 8,5–9 K/GPa. **La fusión es más empinada**, y por eso se cruzan una sola vez.
- En el núcleo interno la aleación sólida tiene otra composición que la líquida: la última fila es orientativa.

### 22. Las tres afirmaciones

**(i) El borde del núcleo interno está donde la temperatura real cruza la fusión de la aleación. CONFIRMADO.**

- Mita y otros (2024), arXiv:2405.09890 [L]: «the ICB temperature is the liquidus temperature of the outer core liquid at 330 GPa».
- Deschamps y Cobden (2022) [L]: esa temperatura «can be estimated from the liquid to solid transition of iron alloys».
- Labrosse (2014), *C. R. Geoscience* [L], usa T_L(r_IC) como temperatura del borde.
- **Matiz:** «exactamente» vale por definición; lo incierto es la cifra.

**(ii) A unos 100–200 km se acerca al solidus sin alcanzarlo, o lo alcanza con agua. CONFIRMADO, con matiz.**

- Cálculo con Katsura (2022) [L] y Herzberg (2000) [R]: a 100 km, 1399 °C frente a 1520 °C: **faltan unos 120 °C**. A 200 km, 1445 frente a 1780: faltan **unos 335 °C**. El acercamiento es **arriba** del tramo, y se aleja al bajar.
- Hirschmann (2010), *PEPI* 179 [R]: con el agua y el CO₂ normales del manto, «small amounts of melt are thermodynamically stable throughout the LVZ».
- **A 50 km, bajo las dorsales,** la adiabata (1373 °C) ya **supera** el solidus seco (unos 1310 °C): por eso funde y sale corteza oceánica. Katsura (2022) [L]: «The peridotite melting may start at slightly deeper regions than 50-km depth». Bajo una placa normal, a 50 km se está dentro de la litosfera, más fría: **la tabla de Katsura no vale para esa zona**.

**(iii) En el borde núcleo-manto, por debajo de la fusión de la roca y por encima de la de la aleación. CONFIRMADO en lo cualitativo; el número, no.**

- Lo seguro son las ondas: encima pasan las S, debajo no. Mita y otros (2024) [L]: «Since the lowermost mantle is not extensively molten, it has been argued that the CMB temperature is lower than the solidus temperature of a pyrolitic mantle at 135 GPa».
- Nomura y otros (2014) [R]: «The low T(CMB) also requires that the melting temperature of the outer core is depressed largely by impurities».
- Con mis cifras centrales: aleación 3489 °C, real 3766 °C, roca 3880–3910 °C.
- **Pero los números chocan.** Si valen Nomura o Kim (solidus de 3160–3300 °C), la temperatura real debe ser menor, y el núcleo necesita más hidrógeno. Mita y otros [L]: «less than ~3500 K at the CMB (~4800 K or less at the ICB)». Fiquet (ESRF) [R] habla de fusión parcial posible «when the temperature approaches 4200 K», y Andrault [L] la ve improbable salvo manchas. Las zonas de velocidad ultrabaja podrían ser eso (Andrault [L]).

**Lo que dibujaría:** dos bandas, no dos líneas. La fusión es de roca hasta 2891 km y de aleación por debajo: **salta hacia abajo unos 400 °C** en el borde (de 3880 a 3490). La temperatura real no salta: sube por la capa límite. Rótulos: «sólido» donde real < fusión; «líquido» entre 2891 y 5150; «sólido» debajo. Etiquetar las dos curvas como «estimadas», y la fusión de la roca como «seca».

### 23. Presiones

**CONFIRMADO; reutilizado de `clases/biologia-geologia-ccaa-t01-c2/verificacion-datos-2.md`** (PREM, tabla II): 135,75 GPa (núcleo-manto); 328,85 GPa (núcleo interno; «330» es el redondeo habitual); 363,85 GPa (centro). 1 GPa = 9869 atm (cálculo): 330 GPa son unos 3,3 millones de atmósferas.

### 24. Composición del núcleo

**MATIZAR.**

- Birch (1952, 1964): 10 % de diferencia (por citas en revisiones [R]).
- Hirose, Wood y Vočadlo (2021), *Nat. Rev. Earth Environ.* [R]: déficit «between 5 and 10%» respecto al hierro puro.
- Anderson e Isaak (2002) [R]: 3–7 %.
- Sigue sin saberse qué elementos son: Mita y otros [L] y Alfè y otros [L] proponen mezclas distintas.

**Frase segura:** «El núcleo es sobre todo hierro, con algo de níquel, pero pesa algo menos de lo que pesaría el hierro puro a esa presión, entre un cinco y un diez por ciento. Así que lleva elementos más ligeros, y aún se discute cuáles.»

---

## F. La cuenta final

### 25. Masa y momento de inercia

**CONFIRMADO; reutilizado:** clase 2, sección H, y ficha [7][17]. PREM integrado: 0,3308; NASA: 0,3308; IERS 2010: 0,3307; masa con 0,017 % de diferencia (la ficha dice 0,02 %). Bola uniforme: 2/5 = 0,4. Ya verificado: el modelo se ajustó a esos datos, así que no son prueba independiente (ficha).

### 26. Ondas S en el núcleo interno

**CONFIRMADO, con debate abierto.**

- **Cómo se sabe que es rígido:** Dziewonski y Gilbert (1971), *Nature* 234, 465–466, por las vibraciones de la Tierra (clase 4). Cao, Romanowicz y Takeuchi (2005), *Science* 308 [L]: «indirect evidence of the solidity of the inner core was documented by means of seismic normal mode eigenfrequency measurements».
- **PKJKP:** una P que se convierte en S al entrar en el núcleo interno. Cao y otros [L]: «has been a controversial issue». Deuss y otros (2000) dijeron que las de Julian y otros eran errores, y propusieron otra observación. Wookey y Helffrich (2008), *Nature* 454 [R]: 700 sismómetros en Japón. Shearer, Rychert y Liu (2011) [R]: dudan de que se pueda observar de rutina.
- **Velocidad S:** PREM, **3,50 km/s** arriba, **3,67 km/s** en el centro [L, tabla].
- **Frase segura:** «Ninguna onda S llega al núcleo interno como S, porque el líquido las frena. Lo sabemos sólido por cómo vibra el planeta entero. Y se han propuesto ondas S nacidas dentro, tan débiles que aún se discuten.»

### 27. Campo magnético y calor

**CONFIRMADO.**

- BGS, [Earth's magnetism](https://geomag.bgs.ac.uk/education/earthmag.html) [R]: «The Earth's magnetic field is generated in the fluid outer core by a self-exciting dynamo process.»
- Lay y otros (2008), *Nat. Geosci.* 1, 25–32 [L]: «The power available to the geodynamo through convection in the core is ultimately controlled by heat flow into the base of the mantle.»
- **Matiz:** además del calor, el núcleo interno al crecer libera elementos ligeros (Space.com y otras [R]). Y la edad del núcleo interno se discute.

**Frase segura:** «El calor que sale del núcleo hacia el manto mantiene en movimiento el hierro líquido, y ese movimiento genera el campo magnético.»

---

## G. La idea más expuesta

### 28. McAllister (2014) y otros

**NO SE SOSTIENE un porcentaje de «manto líquido» en McAllister.**

McAllister, M. L. (2014), *J. Astronomy & Earth Sciences Education* 1(1), 23–36, [ERIC EJ1101087](https://files.eric.ed.gov/fulltext/EJ1101087.pdf) [L]:

- Estudiantes: 92 entrevistas; datos demográficos, N = 91; dibujos, N = 90.
- **Lo que tiene número:** tabla 3, «Liquid inner core 38 %», «Solid inner core 62 %». Cita: «38% of students described the inner core as a liquid, instead of a solid». Motivo: «the core had to be a liquid since they knew it was also very hot».
- **Lo que no tiene número:** «students often referred to this layer as a magma layer»; King (2000): «a "mushy" or "partially melted magma" layer»; «the inaccurate notion that Earth's mantle is entirely composed of molten magma».
- **Ojo:** el propio artículo dice que la astenosfera «contains enough liquid to allow it to behave in a ductile manner». No citarlo en eso.

**Mejor dato disponible:**

- Clark, Libarkin, Kortz y Jordan (2011), *J. Geosci. Educ.* 59, 251–262, reproducido por Kortz ([PDF, SERC](https://cdn.serc.carleton.edu/files/NAGTWorkshops/earlycareer2015/monday_am_example_misconceptio.pdf)) [L, leído de la figura]: histograma de quienes estimaron qué porcentaje del manto es líquido. Unas 50 respuestas (lectura mía de las barras: 2, 2, 5, 4, 4, 3, 6, 7, 13, 4); la moda, **76–85 %**; unas 30 de 50 dan más del 55 %. **Sólo 2 dan 0–5 %**, lo correcto. Muestra pequeña: por el ADR-120, **no** como prueba con cifra.
- Clark y Libarkin (2008), resumen, n = 495 [R]: «many students believe that the mantle is liquid», sin porcentaje.

**Redacción honesta:** «Muchos estudiantes, incluso en la universidad, creen que bajo sus pies hay un mar de lava o un manto líquido. Se ha documentado una y otra vez.» Sin cifra. El 38 % sólo para el error del núcleo interno, y sólo como «en un estudio con unos noventa universitarios»; **hay que decidir si cabe en el ADR-120**.

---

## Lo que no he podido leer

| Documento | Motivo | Qué depende de él |
|---|---|---|
| Haskell (1935, 1936) | De pago | Qué datos exactos usó (B4) |
| Tesis de Repetti | Sin copia | Profundidad exacta (D15) |
| Turcotte y Schubert; Ranalli; Stacey y Davis (2008) | Libros | Sustituidos por otras fuentes abiertas |
| Hirschmann (2000), Fiquet (2010), Anzellini (2013), Sinmyo (2019) | Editorial bloqueada (403) | Sólo abstract, nota de prensa o citas; cifras en dos fuentes |
| Informe final del IGN | Página sin contenido | Superficie oficial (A1) |
| Hirose y otros (2021), Frost (2008) | Sin copia accesible | Sustituidas |
| Perales-Palacios y otros (2021); Díaz y otros (2016), postprint | Bloqueo Anubis del CSIC | Sólo el abstract de Díaz |
| Lantmäteriet (página inglesa) | Sin contenido | Sustituida por Vestøl y SMHI |
| Bolt y otros (1968) | Sólo el fragmento | D15 |
</content>

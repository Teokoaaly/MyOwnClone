---
id: 2026-10-25-refinery-alexhost
type: briefing
date: 2026-10-25
sources: [sources/2026-10-24-alexhost-home.md]
---

# Briefing — Refinery: AlexHost (home de alexhost.com, 2026-10-24)

## Qué se procesó

Captura `0-raw/2026-10-24-alexhost-home.md` (stub, 5 líneas) → fuente `sources/2026-10-24-alexhost-home.md` (1287 líneas, 49 KB, home completa de alexhost.com con catálogo de precios embebido).

**16 átomos nuevos** en `2-atoms/`, todos con prefijo `2026-1024-alexhost-`.

## Hallazgo principal: la premisa del encargo era incorrecta

El encargo anticipaba que la captura declararía explícitamente la pertenencia de AlexHost al segmento "bulletproof" / alto-anonimato (KYC, DMCA, tolerancia a retiradas). **La captura no lo dice en ningún punto.** Se comprobó por búsqueda sobre el texto completo: no aparecen "bulletproof", "DMCA ignored", "no KYC", "anonymous", "without verification", "we do not log", ni política de uso aceptable.

Lo único que sobrevive del positioning es **una ruta de assets heredada**: ocho de las nueve banderas del selector se sirven desde `img/dmca/icons/` (moldova, netherlands, sweden, bulgaria, switzerland, france, england, romania) y solo la de Estados Unidos sale de `img/icons/usa.svg`. La misma ruta sirve los iconos de CPU, RAM, disco y el reloj de las fichas de dedicados, lo que confirma que es un prefijo de assets general y no un marcador de política. Es diseño de interfaz coherente con ese perfil, **no una declaración**.

Consecuencia para el vault: si se trata a AlexHost como "el proveedor bulletproof que declara su postura", esa etiqueta no tiene respaldo textual. Se registró como átomo con bloque `## [FRICTION]` que marca la corrección para juicio humano, sin auto-resolver.

## Los claims extraídos

1. **Escala de dedicados** — 17 fichas, 26,00 € a 408,00 € (×15,7), todas "per Month" y transaccionales. El precio no es función de los cores: el eje es la generación del socket (las etiquetas de modelo de la captura van de un Intel Pentium Dual Core G3220 a un AMD RYZEN 9 5950X; un Xeon E5-2620 de 2009 sigue a 55 €). La primera ficha de la lista es el Ryzen 9 5950X a 260,00 €, no la más barata. El disco se expresa en siete formulaciones distintas.
2. **Misma CPU a dos precios** — 2x E5-2699 v3 a 149 € y 224 € (×1,50) con specs idénticas línea por línea; 2x Gold 6138 a 333 € y 408 € igual; y un tercer par, 2x E5-2690 v4, duplicado **al mismo precio** (180 €) con ficha técnica distinta. No es el caso de Evoxt (dos tablas distintas): es el mismo catálogo con el producto duplicado.
3. **Configurador de VPS** — 24 fichas (8 U1 + 8 U2 + 8 U4). **7 (todas de U1) sin importe; las 17 restantes sí lo muestran**: U1 6 €, U2 10 €, U4 16 €. Solo **3 fichas enlazan a `bill.alexhost.com`** (cid 3725/3726/3727); las otras 21 apuntan a `alexhost.com/#`.
4. **Escala U1/U2/U4** — el número codifica los vCPU; RAM y disco ×2 por escalón; 4,00 → 2,50 → 2,00 €/GB de RAM. "Shared 100 Mbps" y "Shared 1 Gbps" salen al mismo precio, así que el ancho de banda no es un eje de precio.
5. **Nueve ubicaciones sin ping** — MD, NL, SE, BG, CH, FR, EN, RO, US; las nueve "Online" con "Ping: —"; ninguna con ASN, Test IP, dirección ni precio por ubicación. Seis son del EEE (cinco de la UE + Suiza), más el Reino Unido y dos fuera de Europa.
6. **Dos series de cifras de capacidad que no coinciden** — 3,5 Tbit/s anti-DDoS y 231 Gbit/s de canal (bloque de estadísticas) frente a 500 Gbit/s y 20 Gbit/s (bloque de ventajas): ×7 y ×11,55. Además "The latest hardware" junto a "hardware infrastructure was last updated in 2018".
7. **Datacenter propio** — Chisinau, Moldavia, en el solar de una antigua fábrica de armas, en un refugio antiaéreo metros bajo tierra; apertura 2010; 1,6 MW; uptime "garantizado" 99,99 %.
8. **Superficie legal y garantía** — Fee for Service Agreement (ALEXHOST S.R.L., Moldavia), DPA (agosto 2026, importador de datos nombrado), Cookie Policy (septiembre 2026), Privacy Policy, términos de afiliados, garantía de 30 días "for any of the listed services" sin condiciones publicadas, y un Looking Glass público (`lg.alexhost.com`).

Otros: hosting compartido LiteSpeed de 4 planes con doble precio y descuento escalonado inverso (8,4 %–33,3 %); pagos con 9 logotipos cripto sin nombrar moneda (el único identificable por archivo es `cryptomus.png`, un agregador); soporte de dos relojes (tickets 24/7 vs chat en horario); casos de uso que incluyen Forex trading y "government entities"; y una noticia del 21.10.2026 anunciando alza de precios de disco.

## Dónde encaja en el vault

Fuera del umbral de ≤ €4/mes (suelo 6 €), pero reencuadra tres reglas del thread de hosting barato:

- **"Número de ubicaciones no es unidad comparable"**: AlexHost es el caso extremo — nueve banderas, cero dato.
- **Cifra de mitigación comparable**: aquí se publica **la misma magnitud dos veces con valores que difieren ×7**, así que la regla necesita una segunda condición: que la cifra no tenga gemela contradictoria en otra sección de la misma página.
- **"Postura de identidad" vs "cumplimiento auditable"**: AlexHost queda en el intervalo "entre no pide nada y no publica nada" — paga en cripto sin decir nada sobre identidad. Refuerza que el criptopago sin declaración de identidad es el estado por defecto de medio sector, no un privativo del tramo offshore explícito. Su ventaja real frente a Anubiz es la geografía física, no una garantía jurídica.

Propuesta de actualización de thread: `1-desk/thread-addition-alexhost.md`, dirigida a `3-threads/escala-de-hosting-barato-y-el-limite-de-4-euros.md`, con §8.12, fricciones 27–29 y una nota de método. **Aplicada el 2026-10-25** con la numeración final del thread.

## Nada que extender en átomos existentes

Se buscó en `2-atoms/` y no existe ningún átomo sobre AlexHost ni sobre el tramo de Moldavia como proveedor. No hubo que extender ningún átomo previo con nota fechada.

## Notas de proceso

- Se comprobó el mojibake al final: los 16 archivos están limpios de CJK, cirílico, árabe y fullwidth. Los valores en alfabeto cirílico que sí aparecen en la fuente (frecuencias y ancho de banda del bloque VPS) están descritos en prosa en los átomos, no transcritos.
- La captura en `0-raw/` era un stub de 5 líneas que solo remitía a la fuente. Se movió sin modificar a `0-raw/archive/2026-10-25-2026-10-24-alexhost-home.md`. La fuente en `sources/` no se tocó.
- **Revisión factual posterior**: una primera pasada de los átomos afirmaba "solo 3 fichas de VPS con precio" y listaba mal el catálogo de dedicados. Se contrastó cada cifra contra la fuente (recuento programático de las 17 fichas de dedicados y las 24 de VPS) y se corrigieron los átomos afectados: el configurador (7 sin importe / 17 con importe / 3 comprables), la escalera de dedicados (orden y rango 26–408 €, primera ficha Ryzen 9 5950X a 260 €, solo dos fichas con RAM fija), la escalera LiteSpeed (descuentos 8,4 %–33,3 %) y las rutas de banderas (ocho bajo `img/dmca/icons/`, EE. UU. aparte).

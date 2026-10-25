---
id: 2026-1024-veridrop-home-top10-con-sitios-repetidos-y-no-diez-distintos
type: atom
certainty: solid
sources: [sources/2026-10-24-veridrop-home-leaderboard.md]
links: ["[[2026-1024-veridrop-leaderboard-home-paga-la-posicion-pero-no-el-verdict]]", "[[2026-1024-veridrop-concentracion-de-muestras-en-tres-relays]]", "[[2026-1024-veridrop-insignia-pro-de-9-de-50-y-no-es-ranking-de-actividad]]"]
---

## Claim
Los cuatro tableros Top 10 de la home suman **35 filas**, pero esas 35 filas **no son 35 relays distintos: solo 14 lo son**. El desglose por tablero: "Opus 4.8" tiene **10 filas y 10 sitios distintos** (`apikey.fan`, `88api.ai`, `cc.yzzt.top`, `api.koozhan.com`, `x-llm.net`, `mintpop.ai`, `www.hejuapi.com`, `shushutoken.com`, `coding.dx.com.ai`, `routerra.ai`); "GPT 5.6" tiene **10 filas y 8 distintos**, porque **`mintpop.ai` aparece tres veces** (puestos 6, 9 y 10, con 80 % y 4,4 s idénticos); "Opus 5" tiene **5 filas y 3 distintos**, con **`shushutoken.com` en los puestos 2, 4 y 5** (100 % y 2,9 s idénticos); "Fable 5" tiene **10 filas y 5 distintos**, con **`shushutoken.com` cuatro veces** (puestos 4 a 7) y **`api.zhaomoxing.com` tres veces** (puestos 8 a 10, 54 % y 5,0 s). Los sitios que se repiten lo hacen **con cifras idénticas fila a fila**, lo que indica repetición de la misma medición, no mediciones distintas.

## Why It Matters
Es la **consequence operativa de que la posición sea un producto**: cuando una casa compra espacios de patrocinio, compra **filas**, no posiciones distintas. Un Top 10 que en un tablero contiene solo tres sitios distintos **no es un ranking de diez competidores**, y leerlo como tal infla artificialmente la competencia aparente del mercado. El vault ya tiene el precedente exacto en el otro extremo: en el directorio, 22 de 50 entradas tienen 6 tests o menos y la mediana es de 9, de modo que una lista de 50 filas no era una muestra de 50 ([[2026-1024-veridrop-concentracion-de-muestras-en-tres-relays]]); aquí el problema no es la profundidad de muestra sino la **repetición de filas**, que es aún más fácil de no detectar si se lee la captura como un ranking.
La consecuencia para el uso como fuente es concreta: **cualquier extracción de "los N mejores relays" desde esta home produce menos de N entidades**, y si se deduplica por dominio, el resultado son 14 candidatos, no 35. Para un vault que construye una lista blanca de `OPENAI_API_BASE`, la diferencia entre 35 y 14 es la diferencia entre una lista y un catálogo.
Y hay un matiz que refuerza lo anterior: la repetición llega **con marcas comerciales distintas en la columna de promoción** (cada fila patrocinada muestra la oferta de su anunciante), lo que hace que el Top 10 se lea como una lista de ofertas y no como una medición. Es el mismo efecto de mezcla sponsor/tabla que el vault ya había criticized en PriceAI ([[2026-1023-priceai-transit-patrocinadores-y-ranking-en-la-misma-pagina]]) y que aquí se repite a escala de fila.

## Nota de verificación
Recuento literal de dominios sobre las 35 filas de los cuatro tableros. La captura **no** publica: cuántos de esos espacios están pagados en cada tablero, ni si las filas repetidas corresponden a detecciones en instantes distintos. La conclusión "no son diez sitios distintos" es una medición del vault sobre la tabla, no una declaración del sitio.

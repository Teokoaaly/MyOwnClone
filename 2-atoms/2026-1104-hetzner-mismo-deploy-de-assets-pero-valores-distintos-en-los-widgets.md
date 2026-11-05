---
id: 2026-1104-hetzner-mismo-deploy-de-assets-pero-valores-distintos-en-los-widgets
type: atom
certainty: solid
sources: [sources/2026-11-04-hetzner-cloud.md]
links: ["[[2026-1104-hetzner-max-mo-vuelve-a-negativo-el-cero-del-11-03-no-se-repite]]", "[[2026-1104-hetzner-ahorro-medio-cambia-con-operandos-identicos-al-11-03]]", "[[2026-1103-hetzner-cinco-capturas-estabilidad-catalogo-vs-widgets-dinamicos]]"]
---

## Claim
Las tres imágenes estáticas del tema que Hetzner sirve con un parámetro de versión (`?m=`) cambian **una sola vez** en toda la serie de capturas: **m=1792487548** (2026-10-22) → **m=1793092891** (10-31, 11-01, 11-02) → **m=1793691058** (11-03 y 11-04). Es decir, **el 11-03 y el 11-04 se sirvieron desde el mismo despliegue de assets**, y sin embargo sus widgets dinámicos renderizan valores distintos: los techos "max/mo." pasan de **€ 0.00 / € -35.97 / € -240.99** a **€ -27.93 / € -30.33 / € -203.90**, y el "Average traffic cost savings with Hetzner" pasa de **€ -5.378,26** a **€ -4.633,59**, mientras los tres operandos del comparador (AWS € 1.560,28, Azure € 1.287,00, Google € 1.326,50) permanecen **idénticos**.

## Why It Matters
Aísla la causa de la inestabilidad de los widgets: **no es un redespliegue del sitio**. Si el cambio de cifras entre capturas fuera efecto de un despliegue nuevo de la web, dos capturas consecutivas con el mismo `?m=` —el mismo build de assets— deberían renderizar los mismos valores, y no es el caso. La consecuencia práctica es que **ninguna re-captura de esta URL puede "arreglar" ni fijar una cifra dinámica**: el valor es función del render, no del build, así que una captura posterior del mismo día con el mismo despliegue sigue dando un valor distinto. Eso refuerza el marco de [[2026-1103-hetzner-cinco-capturas-estabilidad-catalogo-vs-widgets-dinamicos]] y obliga a tratar los dos widgets como **ruido no citable**, dejando como único material firme el "starting from" del catálogo y el bloque de cumplimiento. Para el thread `escala-de-hosting-barato-y-el-limite-de-4-euros` la conclusión es directa: **no hay que volver a capturar esta página para saber cuánto cuesta Hetzner**, y no hay forma de capturar el valor "correcto" de un widget que se recalcula en cada visita.

## [FRICTION]
> [[2026-1103-hetzner-cinco-capturas-estabilidad-catalogo-vs-widgets-dinamicos]] (escrita hace 2 días) afirma que "la **capa dinámica cambia en cada render**" y, en su nota de verificación, que "no hay forma de comprobar si el propio widget es un render del servidor o un cálculo hecho en el cliente".
> Este átomo presiona esa creencia en un punto concreto: **el servidor sí sirve la página con un build de assets identificable (`?m=1793691058`), y las dos capturas que lo comparten (11-03 y 11-04) renderizan valores distintos**. Si el widget fuera un cálculo puramente de cliente sobre datos del servidor, tendría que haber consumido datos distintos; como los tres operandos del comparador son idénticos y solo cambia el resultado, la lectura más consistente es que **el valor se deriva o se aleatoriza en el render, no en los datos**. La pregunta que el átomo dejaba abierta ("¿render del servidor o cálculo de cliente?") se estrecha: **no es un dato de servidor**.
> Ambas no pueden ser completamente correctas: o el parámetro `?m=` no identifica el build de los widgets (y entonces dos capturas del mismo build deberían coincidir, lo que no ocurre), o los widgets sí se calculan en cliente. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
El parámetro `?m=` se ha extraído directamente de las URL de las tres imágenes del tema presentes en cada captura (`pattern-background-particles-grid.svg`, `openingQuote.svg`, `cloud-location-map.svg`); su valor es único por captura salvo en el 11-03 y el 11-04. Este dato **no aparece en el texto de la página**: es un parámetro de la URL de un asset, y se usa aquí como marca de build, no como afirmación de la fuente.

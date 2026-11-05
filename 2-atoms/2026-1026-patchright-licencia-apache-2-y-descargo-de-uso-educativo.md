---
id: 2026-1026-patchright-licencia-apache-2-y-descargo-de-uso-educativo
type: atom
certainty: solid
sources: [sources/2026-10-25-patchright-playwright.md]
links: ["[[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]]", "[[2026-1022-superficie-legal-publica-dpa-clon-terms]]"]
---

## Claim
El bloque "Copyright and License" declara: **© Vinyzu** y **"Patchright is licensed Apache 2.0"** —con el badge *Apache-2.0 license* confirmado en la página del repo. La atribución de origen es explícita: *"Some Parts of the Codebase are inspired by Driverless (Selenium-Driverless)"* y *"Thanks to Nick Webson for the idea of .patch-File Documentation"* (enlazando a `rebrowser/rebrowser-patches`). El bloque "Disclaimer" dice: *"This repository is provided for **educational purposes only**. No warranties are provided regarding accuracy, completeness, or suitability for any purpose. Use at your own risk... Any misuse or legal violations are the sole responsibility of the user"*. El bloque "Authors" nombra a **Vinyzu** como mantenedor activo y a **Kaliiiiiiiiii** como co-mantenedor, y el "Support our work" ofrece contactar por Discord con `@vinyzu` o `@steve_abcdef`.

## Why It Matters
La **licencia Apache 2.0** es la diferencia legal relevante frente al bot Go, que era **MIT** ([[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]]): Apache 2.0 incluye cláusula de patentes y de concesión de derechos de propiedad industrial, lo que la hace más restrictiva en la distribución empresarial que MIT. Para el producto del vault, que tiene superficie legal propia —DPA, términos, clones— ([[2026-1022-superficie-legal-publica-dpa-clon-terms]]), la diferencia importa si algún día se incorpora el componente en un producto propio: **Apache 2.0 obliga a mantener el aviso de licencia y la atribución de los autores originales**.
El dato más interesante para el vault es la **trazabilidad de la ascendencia técnica**: el código está "inspired by Driverless" y el formato de documentación `.patch` viene de `rebrowser-patches` de Nick Webson. Es decir, **esta técnica tiene un linaje público y con nombre**, y el propio README reconoce las dos fuentes. Eso es útil como criterio de atribución y como advertencia: quien use estos parches está, en términos de genealogía técnica, cerca de un ecosistema —rebrowser, Driverless— que el vault todavía no tiene atomizado.
Y el descargo es del mismo tipo que el del bot Go, pero **más fuerte**: "educational purposes only" con exención de responsabilidad por daños, cuestiones legales y cualquier otro tipo de incumplimiento. Eso sitúa el proyecto en la misma categoría de riesgo legal que el corpus de registro, y por tanto no es material que el vault pueda recomendar, solo registrar.

## Nota de verificación
Licencia, copyright, créditos y descargo están transcritos literalmente. La captura **no** incluye el texto del fichero LICENSE, ni un CLA ni un CONTRIBUTING, ni el alcance exacto de la porción "inspired by Driverless" — solo un enlace a un rango de líneas concreto (`driver_patches/framesPatch.ts#L156-L171`) en un commit antiguo. La lectura sobre las obligaciones de Apache 2.0 es conocimiento general del vault, no de la fuente.

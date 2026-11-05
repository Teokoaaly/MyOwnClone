---
id: 2026-1026-patchright-tests-de-playwright-con-bugs-no-resolubles-y-ventana-de-dias
type: atom
certainty: solid
sources: [sources/2026-10-25-patchright-playwright.md]
links: ["[[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]", "[[2026-1024-github-search-diez-de-catorce-se-pushearon-en-las-veinticuatro-horas]]", "[[2026-1026-patchright-mil-commits-y-cinco-mil-estrellas-actividad-activa]]"]
---

## Claim
Dos bloques del README acotan el riesgo del proyecto. **"Bugs"**: *"Patchright is now tested against the Playwright Tests after every release"* —con la advertencia *"Patchright passes most, but not all the Playwright tests. Some bugs are considered impossible to solve, some are just not relevant. See the list of bugs and their explanation here (issues/30)"*, y el remate *"Based on the Playwright Tests, we concluded that its highly unlikely that you will be affected by these bugs in regular usecases"*. **"Development"**: *"Deployment of new Patchright versions are automatic, but bugs due to Playwright codebase changes may occur. Fixes for these bugs might take a few days to be released."* El TODO marca como hecho *"Setup Automated Testing on new Release"* y como **pendiente** *"Implement Patchright on Java"*.

## Why It Matters
El dato estructural es la **ventana de ruptura de días**: el despliegue de la nueva versión es automático, pero **el parche puede no ser compatible con el código de Playwright nuevo hasta que llegue el fix**. Es decir, cada release de Playwright abre un periodo —"might take a few days"— en el que la versión más reciente de Patchright está rota para algún caso. Para un pipeline en producción, eso significa que **la dependencia se actualiza sola y a veces se rompe sola**, lo que es un perfil de riesgo distinto del de una dependencia estable.
Y el argumento de cobertura es explícitamente **relativo**: "pasa la mayoría, pero no todos" los tests de Playwright, con una lista de bugs explícitamente **irresolubles** y otros **no relevantes**, y la conclusión de que es "altamente improbable" que afecten a casos de uso regulares. Es una afirmación razonada, no una garantía — el propio README ofrece el issue 30 como fuente de la lista, y esa lista no está en la captura.
El contraste con el corpus de registro del §7.5 es instructivo: allí la regla era "sin push desde hace más de 88 días" = proyecto muerto ([[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]). Aquí hay un proyecto **activamente mantenido con testing automático en cada release**, y aun así declara una ventana de breakage de días y un conjunto de tests que no pasan. Los dos criterios de calidad —frecuencia de commits y cobertura de tests— no son la misma medida, y el vault gana un criterio nuevo: **un proyecto con CI puede ser insostenible en un momento concreto**.

## Nota de verificación
Las citas son literales del README. La captura **no** incluye el issue 30 con la lista de bugs, ni el workflow de CI, ni el número de tests que fallan, ni la fecha de la última release. "Might take a few days" no viene con SLA. El ítem de Java pendiente es la única línea del TODO sin marcar.

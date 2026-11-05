---
id: 2026-1026-stealth-status-declaracion-de-indetectabilidad-y-su-limite-explicito
type: atom
certainty: solid
sources: [sources/2026-10-25-puppeteer-extra-stealth.md]
links: ["[[2026-1026-patchright-declara-pasar-catorce-detectores-publicados]]", "[[2026-1026-rebrowser-bot-detector-como-banco-de-pruebas-publico]]", "[[2026-1026-puppeteer-extra-604-commits-559-tags-y-ultimo-commit-en-marzo-de-2023]]"]
---

## Claim
La sección "Status" del README es una afirmación **binaria** —"✅ **`puppeteer-extra` with stealth passes all public bot tests**"— seguida inmediatamente de su **propia limitación declarada**: "I consider this a friendly competition in a rather interesting cat and mouse game. If the other team (👋) wants to detect headless chromium there are still ways to do that (at least I noticed a few, which I'll tackle in future updates)". Y la tesis del autor es explícita: "It's probably impossible to prevent all ways to detect headless chromium, but it should be possible to make it so difficult that it becomes **cost-prohibitive** or triggers **too many false-positives** to be feasible".

## Why It Matters
El objetivo declarado **no es la indetectabilidad, es el coste de la detección**. Eso es una **afirmación de economía dentro de un README técnico**, y el vault tiene poco material de esa categoría. La consecuencia operativa es que el plugin no promete "no me detectan", promete **"detectar esto sale caro"** —lo que, en un mercado donde el detector cobra por captcha resuelto ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]) y donde los propios proveedores de navegador remoto venden "detección gestionada" como producto, es exactamente la **forma de competir del sector**.
Y hay un dato de calendario que el vault ya tenía y que esta frase reencuadra: el plugin está **congelado desde marzo de 2023** ([[2026-1026-puppeteer-extra-604-commits-559-tags-y-ultimo-commit-en-marzo-de-2023]]). Es decir, la frase "which I'll tackle in future updates" **quedó sin cumplir** — la detección que el propio autor vio y no llegó a tapar sigue ahí tres años y medio después, y eso es un coste conocido y no cubierto, no un misterio.
El contraste con el resto del corpus de evasión es lo que hace útil el átomo: `patchright` declara pasar **catorce detectores publicados** ([[2026-1026-patchright-declara-pasar-catorce-detectores-publicados]]), y rebrowser expone **su propio detector como banco de pruebas público** ([[2026-1026-rebrowser-bot-detector-como-banco-de-pruebas-publico]]). El plugin de inyección es la **generación anterior**: su propia evidencia es una tabla de capturas de pantalla de `bot.sannysoft.com` y un conjunto de tests públicos de la era 2019–2021.
La lectura que el vault debería hacer: **"passes all public bot tests" es una afirmación con fecha implícita**, y la fecha implícita es la de los tests que el README muestra.

Nota de verificación: las citas son literales de la sección "Status". La captura **no** publica fecha de ejecución de los tests, ni la lista completa de detectores superados; las tablas son imágenes enlazadas cuyo contenido no es texto auditable.

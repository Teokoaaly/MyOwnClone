---
id: 2026-1026-stealth-bancos-de-prueba-publicos-que-el-plugin-cita-como-evidencia
type: atom
certainty: solid
sources: [sources/2026-10-25-puppeteer-extra-stealth.md]
links: ["[[2026-1026-rebrowser-bot-detector-como-banco-de-pruebas-publico]]", "[[2026-1026-patchright-declara-pasar-catorce-detectores-publicados]]", "[[2026-1026-stealth-status-declaracion-de-indetectabilidad-y-su-limite-explicito]]"]
---

## Claim
El README nombra **cinco detectores o bancos de prueba públicos** como evidencia del plugin: `bot.sannysoft.com` ("Tests have been done using this test site and these scripts"), el test de **Paul Irish** `headless-cat-n-mouse` (que el changelog de `v2.4.2`/`v2.4.1` declara superado con un "⭐️"), los tests de **fpscanner** de antoinevastel (todos en verde desde `v2.4.0`), los tests de **intoli** (también en verde desde `v2.4.0`) y el test **areyouheadless**. El README declara además que la sección "Test results" compara **cuatro combinaciones**: Chromium+headless, Chromium+headful, Chrome+headless y Chrome+headful, con y sin el plugin, y señala una salvedad: "The `MQ_SCREEN` test is broken on their page (will fail in regular Chrome as well)".

## Why It Matters
El vault tenía un solo banco de pruebas público documentado —el detector que rebrowser expone en la web ([[2026-1026-rebrowser-bot-detector-como-banco-de-pruebas-publico]])— y una lista de catorce detectores declarados por `patchright` ([[2026-1026-patchright-declara-pasar-catorce-detectores-publicados]]). Esta captura aporta **el banco de pruebas de la generación anterior**, y aporta algo que las otras dos no: **su antigüedad implícita y su marco de comparación**.
La antigüedad: los detectores citados son de la era **2018–2021** —`headless-cat-n-mouse` es de Paul Irish, los tests de fpscanner e intoli son de antoinevastel— y el changelog que los menciona se cierra en `v2.4.7`. Es decir, **la evidencia del plugin es contemporaneous a sus propias evasiones**, y como el código no se toca desde 2021–2022, la evidencia se quedó congelada con él ([[2026-1026-stealth-status-declaracion-de-indetectabilidad-y-su-limite-explicito]]).
El marco: la comparación es **cuatro Browsers × dos modos × con/sin plugin**, es decir, una matriz que separa el efecto del plugin del efecto del modo headless/headful. Eso es un diseño de evaluación decente y el vault debería citarlo como tal: **el plugin se declara útil en headful**, donde la detección por `HeadlessChrome` no aplica y el valor del resto de evasiones es lo que queda. Y la salvedad del `MQ_SCREEN` ("will fail in regular Chrome as well") es un precedente raro y valioso: **el propio README separa el fallo del detector del fallo del plugin**, que es exactamente la disciplina que el thread viene exigiendo al vault en sus fricciones.

Nota de verificación: nombres, fechas y la matriz de cuatro combinaciones son transcripción literal del README. La captura **no** publica los resultados como texto —son imágenes enlazadas— ni la fecha de ejecución, ni el número de tests que el sitio `bot.sannysoft.com` contiene.

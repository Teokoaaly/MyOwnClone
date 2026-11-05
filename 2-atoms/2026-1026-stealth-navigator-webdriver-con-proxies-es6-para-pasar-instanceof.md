---
id: 2026-1026-stealth-navigator-webdriver-con-proxies-es6-para-pasar-instanceof
type: atom
certainty: solid
sources: [sources/2026-10-25-puppeteer-extra-stealth.md]
links: ["[[2026-1026-rebrowser-runtime-enable-la-fuga-que-usan-todos-los-antibot]]", "[[2026-1026-rebrowser-el-fix-solo-no-basta-y-hacen-falta-canvas-y-webgl]]", "[[2026-1026-stealth-evasions-nombradas-en-el-changelog-del-plugin]]"]
---

## Claim
El changelog del plugin describe con detalle la **técnica** de dos evasiones. En `v2.4.7`: "Improved: `navigator.webdriver`: Now uses ES6 Proxies to pass `instanceof` tests (#117)", con crédito a `@aabbccsmith`. En `v2.1.2`: "Fixed: `navigator.webdriver` now returns undefined instead of false". Y en `v2.4.2`/`v2.4.1`, para `iframe.contentWindow`: "We now proxy the original window object and smartly redirect calls that might reveal it's true identity, **as opposed to mocking it like peasants** :)".

## Why It Matters
El vault acaba de registrar, en la fuente de rebrowser, el principio de criterio del sector: **"the less you manipulate browser internals via JS injections, the better"**, porque existen formas de detectar que objetos internos como `console` y `navigator` han sido afectados por objetos `Proxy` o por `Object.defineProperty` ([[2026-1026-rebrowser-el-fix-solo-no-basta-y-hacen-falta-canvas-y-webgl]]). Esta fuente muestra **el otro lado del mismo problema visto desde dentro**: el plugin de inyección sabe que la señal hay que taparla, y su respuesta es **más ingeniería de enmascaramiento** —un Proxy ES6 que además hace que `instanceof` no delate el objeto, y un `undefined` en lugar de `false` para que el valor no sea un booleano sospechoso.
Es decir: **ambos lados coinciden en el diagnóstico y divergen en la receta**. Rebrowser dice que hay que dejar de manipular internos y parchar el binario; el plugin responde manipulando internos con más maquinaria. La consecuencia de método para el vault es que **"tapar una señal" y "no producir la señal" no son la misma estrategia**, y una es medible con el mismo detector público que la otra (`bot.sannysoft.com` en el ejemplo del propio README), mientras la segunda necesita un driver parcheado ([[2026-1026-stealth-evasions-nombradas-en-el-changelog-del-plugin]]).

## [FRICTION]
> [[2026-1026-rebrowser-el-fix-solo-no-basta-y-hacen-falta-canvas-y-webgl]] afirma que **inyectar JavaScript para disimular el navegador es en sí mismo un vector de detección**, y que por eso la ruta correcta es el parche del código fuente, no el plugin de inyección.
> Este átomo presiona esa afirmación en un punto de ingeniería que el vault no había separado: el plugin **ya era consciente** del problema y lo jujubeó explícitamente —dejar de "mockear" `iframe.contentWindow` y pasar a **proxear** el objeto real redirigiendo las llamadas que delatarían su identidad, con un Proxy ES6 que además supera las pruebas de `instanceof` y devuelve `undefined` en lugar de `false`—. Es decir: **la vía de inyección no es ingenua**, tiene una técnica propia, y el propio sector la considera sophisticated. Y aun así, la recomendación de rebrowser es no usar esa vía. Las dos cosas no pueden ser a la vez: o el enmascaramiento por Proxy es suficiente y detectable-como-cualquier-cosa, o la inyección bien hecha no deja rastro y el argumento "parchea el binario" es superfluous.
> Marcado para juicio humano, no auto-resuelto: **la captura no publica ninguna medición** —ni tasa de detección del Proxy, ni resultado de pasar los detectores de 2026 con el plugin, ni comparación entre plugin y parche sobre el mismo detector—. El vault solo puede registrar que el diagnóstico es compartido y las recetas divergen ([[2026-1026-rebrowser-runtime-enable-la-fuga-que-usan-todos-los-antibot]]).

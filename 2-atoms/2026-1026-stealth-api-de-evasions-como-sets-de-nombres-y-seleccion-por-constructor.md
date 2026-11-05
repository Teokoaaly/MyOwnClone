---
id: 2026-1026-stealth-api-de-evasions-como-sets-de-nombres-y-seleccion-por-constructor
type: atom
certainty: solid
sources: [sources/2026-10-25-puppeteer-extra-stealth.md]
links: ["[[2026-1026-puppeteer-extra-api-de-plugins-con-clase-base-puppeteerextraplugin]]", "[[2026-1026-stealth-evasions-nombradas-en-el-changelog-del-plugin]]", "[[2026-1026-puppeteer-extra-catalogo-de-plugins-numerados-en-la-captura]]"]
---

## Claim
La clase exportada es `StealthPlugin` y **extiende `PuppeteerExtraPlugin`**. Su única opción documentada es `opts.enabledEvasions`, de tipo **`Set<string>`** —"Specify which evasions to use (by default all)"—, con **dos propiedades de solo lectura** que devuelven `Set<string>`: `.availableEvasions` ("Get all available evasions") y `.enabledEvasions` ("Get all enabled evasions"). La documentación da un ejemplo de cada: `console.log(pluginStealth.availableEvasions) // => Set { 'user-agent', 'console.debug' }` y, para el segundo, `pluginStealth.enabledEvasions.delete('console.debug')` —"Enabled evasions can be configured either through `opts` or by modifying this property". El export por defecto es `defaultExport(opts?)`, "Default export, PuppeteerExtraStealthPlugin".

## Why It Matters
El vault ya tenía la clase base del framework registrada como superficie de extensión ([[2026-1026-puppeteer-extra-api-de-plugins-con-clase-base-puppeteerextraplugin]]), pero **no la forma concreta en que una evasión se identifica**. Y la forma importa: **un `Set<string>` de nombres**, no un objeto de configuración. Eso significa que el identificador de una evasión es **una cadena plana y estable** —`console.debug`, `user-agent`— y por tanto comparable entre versiones, publicable en una documentación, y **enumerable en runtime**: `.availableEvasions` da la lista y `.enabledEvasions` permite **quitar una evasión dinámicamente** sin reconstruir el plugin.
Eso convierte la evasión en una **unidad configurable y desactivable**, no solo en un módulo que se carga. Es la diferencia entre "el plugin tapa lo que tapa" y "el pipeline decide qué señales tapa y cuáles deja visibles". Y esa lectura conecta con el corpus de rebrowser, donde el diagnóstico es que **cada señal que se tapa es una señal que se puede tapar mal**: tener la lista en runtime permite **experimentar** —quitar una evasión y medir— en lugar de aceptar el paquete entero ([[2026-1026-stealth-evasions-nombradas-en-el-changelog-del-plugin]]).
El dato fino del ejemplo: `.availableEvasions` se ilustra con `Set { 'user-agent', 'console.debug' }` —un ejemplo **deliberadamente distinto del conjunto real**, porque el README remite al directorio `evasions` como lista actualizada. El vault no puede tomar ese ejemplo por inventario ([[2026-1026-puppeteer-extra-catalogo-de-plugins-numerados-en-la-captura]]).

Nota de verificación: tipos, firmas y ejemplos son transcripción literal de la sección API. La captura **no** publica el contenido de la clase `PuppeteerExtraPlugin` ni la implementación de `availableEvasions`.

---
id: 2026-1104-memphis-aparece-como-decimo-tercer-datacenter-en-la-faq-de-regiones
type: atom
certainty: solid
sources: [sources/2026-11-04-digitalocean-droplets-pricing.md]
links: ["[[2026-1102-digitalocean-tiene-regiones-europeas-amsterdam-londres-y-frankfurt]]", "[[2026-1104-digitalocean-captura-vuelve-a-render-completo-tras-el-render-reducido-del-3-nov]]", "[[2026-1102-digitalocean-la-transferencia-incluida-escala-con-el-plan-de-500-a-11-000-gib]]"]
---

## Claim
La FAQ "Where are DigitalOcean's datacenters located?" de la captura del **2026-11-04** lista **trece** ubicaciones —"San Francisco, Richmond, NYC, Kansas City, Atlanta, **Memphis**, Toronto, Amsterdam, London, Frankfurt, Bangalore, Singapore, and Sydney"— donde las capturas del **2026-11-01** y del **2026-11-02** listaban **doce**: las mismas sin **Memphis**. Memphis se sitúa entre Atlanta y Toronto, en el grupo estadounidense. Las tres regiones europeas (Amsterdam, Londres, Fráncfort) y Bangalore (India) siguen apareciendo en la misma posición de la lista.

## Why It Matters
Es una **novedad real de la quinta captura**, no una variación de formato: la lista de regiones publicada cambia —de doce a trece— en la única ventana en que la página vuelve a renderizar completa después del corte del 11-03. Para el vault, la consecuencia es de **cobertura geográfica de los droplets v5**, no de precio: los enlaces de "Get started" de los v5 apuntan a `region=mem1`, lo que ya dejaba abierto el matiz de que las configuraciones v5 **no están disponibles en todas las regiones** (ver la nota de [[2026-1102-digitalocean-tiene-regiones-europeas-amsterdam-londres-y-frankfurt]]). Una región nueva en la lista general **no implica** que los v5 estén disponibles en ella: la página de precios no publica ni qué regiones ofrecen qué variantes.

Lo que sí aporta al criterio de hosting barato es una confirmación de encuadre: **las tres regiones europeas siguen siendo las únicas de la UE** en la lista de DO, por lo que la ventaja de cobertura europea frente a proveedores de un solo país se mantiene intacta, y la región ampliada es precisamente la que **no** aporta al requisito del vault (hosting en la UE). Es un recordatorio de que "más regiones" y "región donde estoy" son cosas distintas: para MyOwnClone, lo que suma es Ámsterdam/Londres/Fráncfort, no Memphis.

## [FRICTION]
> [[2026-1102-digitalocean-tiene-regiones-europeas-amsterdam-londres-y-frankfurt]] (escrita el 2026-11-02) enumera "El resto de regiones listadas en la captura son San Francisco, Richmond, NYC, Kansas City, Atlanta, Toronto, Bangalore (India) y Singapur, más Sídney" — **doce** ubicaciones, sin Memphis.
> La captura del 2026-11-04 lista **trece** e incluye **Memphis**. Ambas no pueden ser simultáneamente la lista vigente de la página: o la página de DO **añadió una región** entre el 11-02 y el 11-04, o la captura del 11-02 estaba ya desactualizada respecto a la página real (cosa posible, porque el texto de la FAQ cambia por renders independientes y no hay forma de fechar la actualización desde la captura).
> Marcado para juicio humano, no auto-resuelto. Consecuencia operativa: la enumeración de regiones de [[2026-1102-digitalocean-tiene-regiones-europeas-amsterdam-londres-y-frankfurt]] **queda desactualizada en un punto** y este átomo no la modifica; a partir de ahora la referencia vigente de regiones es la del 11-04.

## Nota de verificación
Lista de regiones transcrita literalmente de `sources/2026-11-04-digitalocean-droplets-pricing.md` (línea 267). Las listas del 11-01 y del 11-02 se compararon sobre el mismo archivo: el 11-01 la presenta con separadores ("including San Francisco, Richmond, …") y el 11-02 y el 11-04 sin espacio tras "including" — diferencia de render, no de contenido. La captura del **2026-10-31** no renderiza esta FAQ (no contiene la cadena "Amsterdam" ni "Richmond"), y la del **2026-11-03** la sustituye por "…", por lo que la comparación de doce contra trece se hace contra el 11-01 y el 11-02. La captura **no publica** el número de regiones v5 disponibles, ni qué regiones sirven a qué familia, ni precios por región.

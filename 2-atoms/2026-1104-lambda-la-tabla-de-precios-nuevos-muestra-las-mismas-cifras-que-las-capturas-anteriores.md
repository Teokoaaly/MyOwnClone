---
id: 2026-1104-lambda-la-tabla-de-precios-nuevos-muestra-las-mismas-cifras-que-las-capturas-anteriores
type: atom
certainty: solid
sources: [sources/2026-11-04-lambda-gpu-pricing.md, sources/2026-11-01-lambda-gpu-pricing.md, sources/2026-11-02-lambda-gpu-pricing.md, sources/2026-10-31-lambda-gpu-pricing.md]
links: ["[[2026-1104-lambda-anuncia-precios-nuevos-con-vigencia-el-16-de-noviembre-de-2026]]", "[[2026-1102-lambda-precios-identicos-en-las-tres-capturas]]", "[[2026-1101-lambda-precio-sube-al-encoger-la-instancia]]"]
---

## Claim
Aunque la captura del 2026-11-04 anuncia precios nuevos ([[2026-1104-lambda-anuncia-precios-nuevos-con-vigencia-el-16-de-noviembre-de-2026]]), **las cifras que muestra son exactamente las mismas de las capturas previas**: la comparación de todos los importes de la tabla (Instances 8x/4x/2x/1x y Clusters B200/H100) da un conjunto idéntico al de `sources/2026-11-01-lambda-gpu-pricing.md`, y el subconjunto compartido con la del 2026-11-02 también coincide ($9,86/$9,36/$8,87 en clusters B200; $6,69/$3,99/$2,79/$1,99/$0,79 en Instances 8x; $6,16/$5,85/$5,54 en clusters H100). Es decir: **el anuncio de cambio de precio no viene acompañado de ninguna cifra distinta en la página pública**.

## Why It Matters
Deja al vault en una disyuntiva explícita que solo el proveedor puede resolver: o bien el aviso del 16 de noviembre se refiere a tarifas, productos o clientes **no publicados en la página** (reservado, "1 year+", o lo que solo se ve logueado), o bien las cifras de la tabla ya eran las nuevas y el "precio actual" hasta el 16 de noviembre es un precio distinto del que se ha estado citando en las cuatro capturas anteriores. La consecuencia operativa es una **regla de citación** que hay que aplicar a partir de ahora: cuando el vault escriba "$3,99/GPU-hora del H100 8x ([2026-1101-lambda-precio-sube-al-encoger-la-instancia])", debe hacerlo como "precio publicado en la tabla, con vigencia declarada a partir del 2026-11-16", no como precio firme de mercado, porque la fuente ha dejado de ofrecer esa garantía.

## [FRICTION]
> [[2026-1102-lambda-precios-identicos-en-las-tres-capturas]] (escrita hace ~3 semanas) afirma que los precios "pueden usarse como referencia de mercado vigente en la semana del 3 de noviembre de 2026 **sin fechas de caducidad inmediata**".
> La captura del 2026-11-04 presiona esa lectura en un punto: la estabilidad numérica sigue siendo real (las cifras no cambian), pero la página ha **dejado de ser timeless** — declara una fecha de vigencia el 16 de noviembre de 2026 y remite el precio aplicable hasta entonces a la cuenta del cliente. "Estable" y "vigente" ya no son la misma cosa: la estabilidad observada puede ser la de una tabla de precios futuros, no la de una tarifa en curso.
> Ambas no pueden ser completamente correctas. Marcado para juicio humano, no auto-resuelto.

## Nota de método
Comparación literal de todos los tokens `$` de `sources/2026-11-04-lambda-gpu-pricing.md` frente a `sources/2026-11-01-lambda-gpu-pricing.md` (conjuntos idénticos) y frente a `sources/2026-11-02-lambda-gpu-pricing.md` (subconjunto compartido idéntico). Ninguna aritmética: solo coincidencia de cifras.

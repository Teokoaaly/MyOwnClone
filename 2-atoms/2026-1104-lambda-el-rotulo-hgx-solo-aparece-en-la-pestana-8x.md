---
id: 2026-1104-lambda-el-rotulo-hgx-solo-aparece-en-la-pestana-8x
type: atom
certainty: solid
sources: [sources/2026-11-04-lambda-gpu-pricing.md, sources/2026-11-01-lambda-gpu-pricing.md, sources/2026-11-02-lambda-gpu-pricing.md]
links: ["[[2026-1102-lambda-cambia-el-rotulo-de-los-modelos-entre-capturas]]", "[[2026-1102-lambda-precios-identicos-en-las-tres-capturas]]", "[[2026-1101-lambda-recurso-por-gpu-casi-constante-entre-tamanos]]"]
---

## Claim
La captura del 2026-11-04 muestra las **cuatro pestañas de Instances con dos convenciones de rótulo distintas según el tamaño**: la pestaña **8x** rotula sus filas "NVIDIA HGX B200", "NVIDIA HGX H100", "NVIDIA HGX A100" (80 GB) y "NVIDIA HGX A100" (40 GB), mientras que las pestañas **4x, 2x y 1x** rotulan las suyas "NVIDIA B200 SXM6", "NVIDIA H100 SXM", "NVIDIA A100 PCIe" y "NVIDIA A6000" — exactamente la convención de la captura del 2026-11-01. En la misma captura, "NVIDIA Tesla V100" aparece con su nombre completo en 8x, y la fila de 1x mantiene la mezcla "NVIDIA A100 SXM" / "NVIDIA A100 PCIe" ambas a $1,99.

## Why It Matters
Corrige la lectura del rótulo como un atributo de la página: **"HGX" no es una marca de catálogo que Lambda alterna entre capturas, es el nombre de la plataforma de 8 GPUs**, y por eso solo aparece en la pestaña 8x, cuyas specs (208 vCPU, 2900 GiB, 22 TiB) son las de una máquina de 8 GPUs ([[2026-1101-lambda-recurso-por-gpu-casi-constante-entre-tamanos]]). La consecuencia práctica para el vault es una regla de transcripción: **al citar una cifra de Instances hay que declarar la pestaña (8x/4x/2x/1x) y usar el rótulo literal de esa fila**, porque "$6,69" es el "NVIDIA HGX B200" de 8x y no el "NVIDIA B200 SXM6" de 4x ($6,79) aunque sean el mismo chip.

## [FRICTION]
> [[2026-1102-lambda-cambia-el-rotulo-de-los-modelos-entre-capturas]] (escrita hace ~3 semanas) framea la diferencia de rótulo como **un cambio entre capturas**: "el 2026-10-31 y el 2026-11-01 usan 'NVIDIA B200 SXM6 / H100 SXM / A100 SXM' y el 2026-11-02 usa 'NVIDIA HGX B200 / NVIDIA HGX H100 / NVIDIA HGX A100'".
> Esta captura presiona ese encuadre: el rótulo HGX aparece **en la misma captura** en la que las pestañas 4x/2x/1x mantienen los nombres sin HGX, y la captura del 2026-11-01 (que sí renderizaba las cuatro pestañas) usaba nombres sin HGX en todas ellas. Es decir, la variable parece ser **la pestaña**, no la fecha de captura.
> La atribución de "HGX" a la plataforma de 8 GPUs sigue siendo una inferencia del nombre y de las specs, no una frase de la fuente; la coexistencia de ambas convenciones en una sola captura, en cambio, es literal.
> Marcado para juicio humano, no auto-resuelto.

## Nota de método
Columna "Plan" de las cuatro tablas de Instances en `sources/2026-11-04-lambda-gpu-pricing.md`, contrastadas con las de `sources/2026-11-01-lambda-gpu-pricing.md` (las cuatro pestañas con nombres sin HGX) y `sources/2026-11-02-lambda-gpu-pricing.md` (solo la pestaña 8x, con nombres HGX).

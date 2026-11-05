---
id: 2026-1104-lambda-anuncia-precios-nuevos-con-vigencia-el-16-de-noviembre-de-2026
type: atom
certainty: solid
sources: [sources/2026-11-04-lambda-gpu-pricing.md]
links: ["[[2026-1102-lambda-precios-identicos-en-las-tres-capturas]]", "[[2026-1101-lambda-precio-sube-al-encoger-la-instancia]]", "[[2026-1101-lambda-instancias-1x-precios-de-gpu-de-consumo]]"]
---

## Claim
La captura del **2026-11-04** es la primera de `lambda.ai/pricing` que incluye un **anuncio de cambio de precio con fecha de vigencia**: las cuatro tablas de Instances (8x, 4x, 2x, 1x) repiten al pie la nota literal *"Plus applicable sales tax/VAT/GST. **New prices take effect November 16, 2026, at 00:00 UTC.** Until then, log in to your Lambda Cloud account to see current pricing."* Ninguna de las capturas del 2026-10-31, 2026-11-01 ni 2026-11-02 contiene esa frase: sus notas al pie eran solo *"plus applicable sales tax/VAT/GST"*.

## Why It Matters
Es la primera vez que el corpus de Lambda aporta **una discontinuidad programada** en vez de una serie estable: hasta ahora el proveedor publicaba un catálogo fijo y el vault podía citarlo como "precio de mercado vigente". A partir de esta captura hay que fechar las cifras: **las de la tabla son las de después del 16 de noviembre de 2026, no las que se cobran hasta entonces**. Es además un dato de transparencia operativa para el corpus (mismo patrón que ya se aplicó a las ventanas de vigencia de otras fuentes), porque obliga a distinguir el precio *anunciado* del precio *facturable* en cualquier cálculo de coste con Lambda: los $3,99/GPU-hora del H100 8x ([2026-1101-lambda-precio-sube-al-encoger-la-instancia]) son un valor futuro respecto al 4 de noviembre de 2026, y la regla operativa del vault pasa a ser **citar siempre "precio publicado, vigente desde 2026-11-16"**.

## Nota de método
Cadena verificada literalmente en `sources/2026-11-04-lambda-gpu-pricing.md` (aparece 4 veces, una por tabla de Instances). Comparado contra `sources/2026-11-01-lambda-gpu-pricing.md` y `sources/2026-11-02-lambda-gpu-pricing.md`, donde el pie es únicamente `* plus applicable sales tax/VAT/GST`.

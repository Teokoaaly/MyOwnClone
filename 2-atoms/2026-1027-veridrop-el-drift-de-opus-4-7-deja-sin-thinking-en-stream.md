---
id: 2026-1027-veridrop-el-drift-de-opus-4-7-deja-sin-thinking-en-stream
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-thinking-signature-500-a-2000-caracteres-con-peso-25]]", "[[2026-1027-veridrop-los-tres-modos-de-deteccion-y-sus-conteos-no-coinciden-entre-paginas]]", "[[2026-1026-new-api-uso-en-stream-y-costo-de-generaciones-completadas]]"]
---

## Claim
La FAQ documenta un **API drift conocido de Claude Opus 4.7**: con la combinación **adaptive thinking + streaming + summarized**, el **SSE en streaming no emite bloques `thinking`**, mientras que la vía **no-stream funciona con normalidad**. La corrección que aplica el detector es explícita: **"Veridrop 的 thinking_signature detector 已经针对这个切到非流式,确保检测可靠"**. Es decir: **el fallo no estaba en el relay, estaba en la propia prueba**, y se resolvió desactivando el streaming para esa comprobación.

## Why It Matters
Es el **caso de un detector que se corrige a sí mismo ante un cambio del proveedor**, y documenta una clase de fallo que el vault va a encontrar en cualquier detector que construya: **la ausencia de una señal no es evidencia de ausencia del modelo**. Si el detector de firma criptográfica corriera en streaming contra Opus 4.7, daría **0 por firma ausente** — el mismo resultado que un relay que sustituye el modelo por Kiro o Amazon Q — y por tanto produciría **un falso positivo de fraude**.
La lección de arquitectura es transferible al producto del vault: **un detector debe registrar qué superficie de API usó para cada comprobación**, porque el mismo par (modelo, veredicto) puede significar cosas distintas según se haya medido en stream o en no-stream. Es la misma clase de error que la **fidelidad de conversión campo a campo** del gateway ([[2026-1026-new-api-fidelidad-de-conversion-orden-de-campos-y-esquema-json]]): el detalle que se pierde al cambiar de forma de la petición es el que decide el resultado.
Y hay una lectura de mercado que importa para el vault como comprador: **un detector que documenta sus propias limitaciones es más fiable que uno que no**. VeriDrop no solo corrige el detector, **lo cuenta**, lo que permite a quien lee el informe saber que el "0 en firma" de una detección antigua era un artefacto de la prueba y no del relay. Es la misma honestidad estructural que exige el detector de firma criptográfica de [[2026-1027-veridrop-thinking-signature-500-a-2000-caracteres-con-peso-25]]: **una señal ausente solo significa algo si se sabe sobre qué superficie se midió**.

## Nota de verificación
Literal de la FAQ. La captura **no** publica la fecha del drift, ni la versión exacta de Opus 4.7 afectada, ni si otros modelos presentan la misma deriva.

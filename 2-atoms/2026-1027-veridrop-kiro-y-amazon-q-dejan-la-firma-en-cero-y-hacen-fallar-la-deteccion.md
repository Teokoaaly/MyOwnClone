---
id: 2026-1027-veridrop-kiro-y-amazon-q-dejan-la-firma-en-cero-y-hacen-fallar-la-deteccion
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-thinking-signature-500-a-2000-caracteres-con-peso-25]]", "[[2026-1027-veridrop-tres-formas-de-dilucion-o-concubamiento]]", "[[2026-1023-new-api-una-sola-api-multiproto]]"]
---

## Claim
La FAQ identifica los **sustitutos concretos** de Claude: **Kiro y Amazon Q** son **"Amazon 的 Claude 替身网关"** que responden por la **interfaz simplificada de AWS Bedrock** y **no devuelven la firma de servidor**, porque no son Anthropic. El efecto sobre el detector es total: **"Veridrop 在 thinking_signature 检测上会直接判 0 分,fail 整体检测"** — no es una penalización parcial, es **fallo de la detección entera**. La FAQ lo incluye entre los **5 modos de falsificación** más comunes, junto con el GPT-4o cambiado por GPT-4o-mini y la inyección de un system prompt extra.

## Why It Matters
Aporta el **mecanismo físico** por el que la sustitución se sostiene: **no es que el relay quiera mentir, es que está sirviendo Bedrock**, una API de AWS con otro contrato, otro modelo detrás y otra ausencia de campos. Es el caso donde **la ausencia de la firma criptográfica no es un subterfugio del intermediario sino la firma de un proveedor distinto** — y por eso el detector puede leerla sin ambigüedad.
Para el vault esto tiene una consecuencia de arquitectura que ya estaba en su propio producto: **una capa de unificación que normaliza hacia un protocolo común (OpenAI-compatible) elimina por diseño las diferencias de proveedor que son la evidencia** ([[2026-1023-new-api-una-sola-api-multiproto]]). Un gateway como el del vault **no puede** decir "esto es Claude" a partir de la forma de la respuesta, porque la forma es su propia invención. Solo la capa de más abajo, que ve el upstream crudo, puede. Es el argumento definitivo para **mantener el acceso al upstream sin normalizar** si se quiere ser capaz de auditarlo.
Y hay una lectura de mercado: **el sector tiene al menos un proveedor de sustitutos de Claude con nombre propio (Kiro, Amazon Q)**, lo que significa que "usar Claude vía relay" puede ser "usar Bedrock vía relay", una de las tres formas de dilución de [[2026-1027-veridrop-tres-formas-de-dilucion-o-concubamiento]] sin que ninguna de las dos partes lo diga.

## Nota de verificación
Literal de la FAQ. La captura **no** publica qué modelo concreto sirve Amazon Q detrás, ni si Kiro y Amazon Q exponen la interfaz Bedrock completa o solo un subconjunto.

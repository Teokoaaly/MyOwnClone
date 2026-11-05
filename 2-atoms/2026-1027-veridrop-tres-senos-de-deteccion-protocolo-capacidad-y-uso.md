---
id: 2026-1027-veridrop-tres-senos-de-deteccion-protocolo-capacidad-y-uso
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-openai-deteccion-nivel-comportamiento-protocolo-sin-prueba-criptografica]]", "[[2026-1027-veridrop-thinking-signature-500-a-2000-caracteres-con-peso-25]]", "[[2026-1027-veridrop-la-prueba-de-pureza-en-tres-pasos]]"]
---

## Claim
La FAQ describe la verificación en **tres senos**: **① campos de protocolo** ("id 前缀、object、finish_reason 是否符合官方规范"), **② huella de capacidad** ("thinking signature 加密签名、PDF 多模态、function calling shape") y **③ campos de uso** ("usage 里有没有混入异源痕迹如 claude_cache_creation_*"). Los tres se **combinan en 7-10 comprobaciones** ("Veridrop 把这三类合成 7-10 项检测"). En el lado de los falsos, la FAQ enumera **cinco modos de falsificación** con la misma estructura: Kiro / Amazon Q / Bedrock como Claude falso; backend Claude detrás de peticiones GPT (con residuos `claude_*` en `usage`); **GPT-4o cambiado por GPT-4o-mini**; Capability stripping (thinking, PDF multimodal) e **inyección de un system prompt extra** que reescribe la identidad.

## Why It Matters
Es el **modelo de datos de un detector de intermediarios**, y el vault lo necesita porque su propio producto de agregación va a tener que jugar en el mismo tablero: un detector que separa en tres ejes (forma del protocolo, capacidades sobrevivientes, forma del contador de consumo) es **una taxonomía de campos, no un bool**, y por tanto es reutilizable como **esquema de campos de una API de catálogo**: para cada relay, el agregador podría almacenar no "es bueno" sino "qué eje falla".
El tercer eje es el que más importa para el vault: **el contador de tokens es el único campo donde el fraude se paga**. Un relay que infla `usage` no está mintiendo sobre el modelo, está **facturando**. Es exactamente la partida que el vault ya sabe incomparable entre proveedores ([[2026-1023-priceai-transit-formula-del-multiplicador-compuesto]]) y la que el gateway de referencia ya Cobra con una lógica de facturación que corrige seis casos de desacople ([[2026-1026-new-api-uso-en-stream-y-costo-de-generaciones-completadas]]).

## Nota de verificación
Estructura y cifras son literales de la FAQ. La captura **no** publica la lista de detectores individuales (solo el recuento agregado "7-10") ni el criterio que decide el recuento.

---
id: 2026-1024-gptgrok2api-gateway-unificado-gpt-y-grok-en-api-compatible
type: atom
certainty: solid
sources: [sources/2026-10-24-gptgrok2api.md]
links: ["[[2026-1024-gptgrok2api-compatibilidad-multiprotocolo-y-despacho-por-modelo]]", "[[2026-1023-new-api-gateway-unificado-de-modelos]]", "[[2026-1023-midjourney-proxy-convierte-discord-en-api-rest]]"]
---

## Claim
`AuuCoder/gptGrok2api` (GPTGrok2API) se define en su README como un **gateway unificado y autoalojado de GPT y Grok** que convierte en API compatible con OpenAI la capacidad de **cuentas de suscripción ya conectadas**, y añade una consola de gestión de cuentas, proxies, registro, logs, imágenes y estado de ejecución. La tabla de "capacidades actuales" precisa el alcance: el módulo de gateway **fusiona tres catálogos de modelos distintos —GPT, Grok SSO y Grok Build OAuth—** y la raíz `/v1` **despacha automáticamente según el modelo**, conservando además `/grok/v1` como interfaz Grok completa. Es software libre bajo licencia **MIT** (fichero `LICENSE` propio más `GROK2API_LICENSE` heredado) y el repositorio declara ser una segunda versión ("desarrollo secundario") de `yukkcat/chatgpt2api`.

## Why It Matters
Es el **tercer patrón de envoltorio que el vault encuentra**, y el más parecido al que MyOwnClone ya usa: un proveedor sin API oficial o con API reutilizada a la inversa, un tercero construye el puente HTTP. La diferencia con Midjourney-Proxy ([[2026-1023-midjourney-proxy-convierte-discord-en-api-rest]]) es el número de proveedores: allí un solo canal y un solo modelo; aquí **dos proveedores de frontera y tres mecanismos de autenticación distintos** (SSO de Grok, OAuth de Grok Build y cuentas de GPT) detrás de **una sola URL base y un solo esquema de autenticación por token Bearer**. El producto del vault podría hablar con este gateway exactamente igual que habla con un relay comercial: `OPENAI_API_BASE` + `OPENAI_API_KEY`.
La lección de arquitectura se repite: **la envoltura es el producto, no el modelo**. Y aquí la envoltura añade una capa que los proxies de canal único no tienen: **gestión del ciclo de vida del credencial** (alta, sondeo, recuperación, cuota, almacenamiento), es decir, el gateway trata la cuenta de suscripción como una **fuente de capacidad que se renueva**, no como una clave estática.
Se puede encuadrar también como la alternativa "vertical" al relay comprado: en lugar de multiplicador sobre cuota reventada, **la capacidad se produce con cuentas propias en lugar de comprada reventa** ([[2026-1023-new-api-gateway-unificado-de-modelos]]).

## Nota de verificación
El README capturado describe 17 módulos de capacidad; esta nota se limita al que da nombre al proyecto. La captura **no** publica: los nombres concretos de los modelos GPT que expone `/v1/models` (el ejemplo usa `gpt-5`), ni las cuotas o precios de las cuentas que consume, ni si el autor opera el servicio `muyuai.top` que el README menciona como sitio propio.

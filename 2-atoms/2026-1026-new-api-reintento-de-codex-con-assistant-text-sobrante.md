---
id: 2026-1026-new-api-reintento-de-codex-con-assistant-text-sobrante
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1026-new-api-correcciones-de-continuidad-de-stream-y-registro-de-uso]]", "[[2026-1023-new-api-relaykit-conversion-perdida-de-campos]]", "[[2026-1023-new-api-una-sola-api-multiproto]]", "[[2026-1026-new-api-fidelidad-de-conversion-orden-de-campos-y-esquema-json]]"]
---

## Claim
**v1.0.0-rc.43** corrige un 400 en la conversión de entrada de **Responses** hacia Claude y Gemini: cuando la petición incluye **texto de asistente posterior al último mensaje de usuario o al último resultado de herramienta**, ese texto **se elimina** y se registra una advertencia **`trailing_assistant_omitted`**. El caso que lo dispara es **Codex reintentando un stream que falló después de que ya hubiera llegado una respuesta**. **Claude 4.6** en adelante, **Gemini 3.6 Flash** y **Gemini 3.5 Flash-Lite** en adelante rechazaban esa entrada con un 400. Las peticiones de **Chat Completions y Claude Messages conservan su prefill**.

## Why It Matters
Este es un caso de **conversión que rompe el cliente, no el gateway**: el cliente (Codex) envía algo que el gateway **reenvía** y el upstream lo rechaza con un 400 cuya causa es invisible para el usuario final. El arreglo no es adaptar la petición al upstream, sino **recortar lo que el upstream no tolera y dejar rastro** (`trailing_assistant_omitted`).
La diferencia con Chat Completions y Claude Messages es el dato clave: **el prefill se conserva** en esos protocolos porque es una semántica legítima (continuar el turno del asistente), mientras que en Responses ese texto **solo puede ser residuo de un reintento**. Es una distinción fina de protocolo que solo se aprende leyendo release notes, y que es exactamente el tipo de conocimiento que el gateway multi-protocolo del vault tiene que internalizar ([[2026-1023-new-api-una-sola-api-multiproto]]).
Y el patrón de fondo —**el gateway reenvía fielmente una estructura que el upstream considera inválida** — es exactamente lo que el átomo de RelayKit ya señalaba como riesgo de la conversión ([[2026-1023-new-api-relaykit-conversion-perdida-de-campos]]). Aquí aparece la mitigación concreta que faltaba: **recortar y avisar**, en lugar de reenviar y fallar.
Para el vault, la lectura de negocio es que **el reintento automático del cliente es un multiplicador de peticiones** que el gateway tiene que absorber bien: cada reintento mal formado es un 400 visible para el usuario final y una llamada cobrada al upstream ([[2026-1026-new-api-correcciones-de-continuidad-de-stream-y-registro-de-uso]]).

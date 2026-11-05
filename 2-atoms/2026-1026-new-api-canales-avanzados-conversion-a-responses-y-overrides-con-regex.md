---
id: 2026-1026-new-api-canales-avanzados-conversion-a-responses-y-overrides-con-regex
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-relaykit-conversion-perdida-de-campos]]", "[[2026-1023-new-api-gateway-unificado-de-modelos]]", "[[2026-1026-new-api-fidelidad-de-conversion-orden-de-campos-y-esquema-json]]"]
---

## Claim
**v1.0.0-rc.42** añade que los **canales personalizados avanzados (Advanced Custom) pueden convertir Claude Messages y Gemini generateContent a OpenAI Responses**, y que los **overrides de parámetros avanzados admiten condiciones de regex** (PR #7698). **rc.42** añade además que los **canales Moonshot reenvían `/v1/responses` sin modificar**, y que Kimi sirve **`kimi-k3`** en esa ruta. En **rc.47** se corrige que **"Passthrough Body" (透传请求体) se perdía al guardar** el canal Advanced Custom (PR #7971, `seefs001`).

## Why It Matters
Esto es la **tercera variante del mismo problema** —convertir a Responses— y la fuente no dice que sustituyese a las anteriores: los canales **OpenAI, Moonshot y Advanced Custom** pueden todos hablar Responses, cada uno con su propia regla. Un operador que configure mal su Advanced Custom pierde el **Passthrough Body** y, con él, la capacidad de enviar campos que Responses exige y que el gateway no conoce. La corrección de rc.47 es una **pérdida de configuración silenciosa**: el canal se guardaba sin el campo y el síntoma aparece en producción, como un 400 del upstream.
La parte más valiosa para el vault es el **regex en los overrides**: por primera vez el gateway permite **condicionar un parámetro a un patrón del contenido de la petición**. Es la primitiva que hace falta para un producto de reventa — "si el prompt menciona X, baja el esfuerzo; si menciona Y, cambia de modelo" — y es también una primitiva **peligrosa**, porque es una regla de negocio ejecutada sobre texto no confiable.
La conversión a Responses está dejando de ser marginal: es ya **el formato de destino de varias rutas de entrada** (Claude, Gemini, Chat Completions, WebSocket), lo que confirma que Responses se está volviendo **el bus interno del gateway** y no solo un formato de cliente. Es el riesgo exacto que el átomo de RelayKit ya señalaba: **convertir no es una operación gratis** ([[2026-1023-new-api-relaykit-conversion-perdida-de-campos]]), y el gateway de referencia sigue añadiendo rutas de conversión en lugar de cerrar las existentes ([[2026-1023-new-api-gateway-unificado-de-modelos]]).

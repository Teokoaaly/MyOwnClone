---
id: 2026-1101-assemblyai-tarifas-por-hora-no-por-minuto
type: atom
certainty: solid
sources: [sources/2026-11-01-assemblyai-pricing.md, sources/2026-11-03-assemblyai-pricing.md]
links: ["[[2026-1031-assemblyai-pricing]]", "[[2026-1031-deepgram-pricing]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
El precio base del Pre-recorded Speech-to-Text de AssemblyAI se publica **por hora de audio, no por minuto**: Universal-3.5 Pro a **$0.21/hr** ("The most accurate async speech-to-text model… works across 18 languages, with native code switching and our most accurate speaker diarization yet") y Universal-2 a **$0.15/hr** ("trained on over 12.5 million hours of audio data. Supports 99 languages"). Ambos con la misma estructura: columna "Pay as you go" con la tarifa y columna "Custom" que solo dice "Contact us".

## Why It Matters
Esto fija la **unidad de medida** con la que hay que cotizar un módulo de voz en el vault: la hora, no el minuto. Con Universal-2 a $0.15/hr, un tenant que consume 10 horas de audio al mes cuesta **$1,50**; 100 tenants con 5 horas cada uno cuestan **$75/mes** en transcripción. Frente al techo de hosting de ≤ €4/mes documentado en [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]], la partida de audio **no es una línea marginal del presupuesto de infraestructura**: se vuelve material en cuanto el producto tiene usuarios reales. Y el tipo de línea que genera es de consumo variable por tenant — encaja en la categoría `categoryCloneResponses` que [[2026-1022-costes-por-categoria-tenant]] define como facturable al cliente, no en `categoryPlatformOps`. El coste dominante sigue siendo el SaaS por asiento, no la transcripción: la fricción real está en elegir proveedor, y el átomo hermano [[2026-1031-deepgram-pricing]] ya plantea esa comparación per-minute vs per-seat.

## [FRICTION]
> [[2026-1031-assemblyai-pricing]] (escrita hace ~4 semanas) afirma que "AssemblyAI's pricing is per-minute of transcribed audio with volume-based discounts, similar to Deepgram's usage-based model, where cost scales with audio duration rather than per-user seats".
> La página de precios de AssemblyAI no publica ningún precio por minuto: publica **$/hr** en las dos columnas de la tabla de modelos, y la segunda discrepancia es que **los descuentos por volumen no están publicados** — la FAQ solo ofrece "custom pricing for customers with high-volume usage" vía equipo de ventas (ver [[2026-1102-assemblyai-facturacion-mensual-sin-minimos-ni-contratos]]). Ambas notas no pueden ser completamente correctas: o la unidad es la hora, o el minuto. Marcado para juicio humano, no auto-resuelto.

## 2026-11-03 — re-verificación
La cuarta captura de `assemblyai.com/pricing` (`sources/2026-11-03-assemblyai-pricing.md`) reproduce **sin una sola variación** la tabla de modelos de pre-recorded: **Universal-3.5 Pro a $0,21/hr** ("The most accurate async speech-to-text model… works across 18 languages, with native code switching and our most accurate speaker diarization yet") y **Universal-2 a $0,15/hr** ("trained on over 12.5 million hours of audio data. Supports 99 languages"), con la misma columna "Pay as you go" y una columna "Custom" que ofrece "Get custom rate limits, enhanced concurrency, and enterprise-grade flexibility" con "Contact us" (ver [[2026-1103-assemblyai-columna-custom-tercer-escalon-de-precios]]). Confirma por tanto la unidad **$/hr** una vez más y confirma que el nombre del modelo flagship sigue siendo **Universal-3.5 Pro** — no hay fricción de nombre ni de precio con este átomo.
Lo que la captura del 11-03 **no** permite es re-verificar nada del resto del catálogo (Realtime, Sync, Dictation y TTS vienen como "..."), así que esta re-verificación aplica **solo a pre-recorded**: el alcance de la afirmación es más estrecho del que parecía. Ver [[2026-1103-assemblyai-captura-reducida-solo-pre-recorded-expandido]].

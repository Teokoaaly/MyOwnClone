---
id: 2026-1022-myclone-carece-modos-memories-ni-visitors
type: atom
certainty: tentative
sources: [raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md]
links: ["[[2026-1022-myclone-vs-myownclone-gaps-api]]", "[[2026-1022-arquitectura-rac-tres-modos-por-clon]]", "[[2026-1022-myclone-workflows-beta-dominio]]"]
---
## Claim
El handoff afirma que **MyClone.is no tiene** tres capacidades que [[myownclone]] ya posee: modos por clon (pedagogía/soporte/ventas), memorias/firmas/plantillas (memories/signatures/templates) y visitor tracking (solo `conversations.visitor_id`, falta UI y captura). El propio autor lo marca como "ventaja competitiva" de MyOwnClone.

## Why It Matters
Invierte la lectura del comparativo de gaps: la mayor superficie de API de MyClone (227 endpoints, ver [[2026-1022-myclone-api-superficie-227-endpoints]]) no se traduce en esas tres capacidades de producto. Si es cierto, la ventaja de [[myownclone]] no está en la API sino en el **modelo de producto** — el clon con modos configurables y memoria persistente, que es exactamente el eje que [[2026-1022-arquitectura-rac-tres-modos-por-clon]] define como diferenciador frente a [[delphi]].
Matiz importante: en MyClone los modos se sustituyen por **workflows** con estado y objetivo ([[2026-1022-myclone-workflows-beta-dominio]]), que es más potente en un flujo guionizado pero más rígido: no es lo mismo un clon que cambia de rol por conversación que un clon que recorre un workflow. El handoff, al no mencionar esta sustitución, simplifica.
Se marca `tentative`: es una afirmación del autor del informe, deducida de la ausencia de endpoints, no de una verificación negativa explícita.

## [FRICTION]
> El **mismo handoff** documenta en su Parte 1 el endpoint `GET /api/v1/personas/{id}/visitors` ("Lista de leads") con autenticación Bearer, y la tabla de endpoints "más importantes" incluye también `POST /api/v1/sessions/{token}/capture-lead`. Es decir, MyClone.is **sí expone gestión de visitors/leads** por API.
> Este átomo afirma, siguiendo la sección "Notas importantes para el LLM" del handoff, que MyClone "NO tiene" visitor tracking. Ambas no pueden ser completamente correctas: o el endpoint `visitors` existe pero no equivale a un sistema de visitor tracking (p. ej. solo lista leads ya capturados sin persistir visitors, sin `last_seen_at` ni metadata, y sin UI), o la afirmación "MyClone NO lo tiene" es una simplificación del autor.
> Consecuencia práctica: el gap `visitors/*` que aparece en [[2026-1022-myclone-vs-myownclone-gaps-api]] sí está respaldado por la API del competidor, pero la "ventaja competitiva" del visitor tracking propio de [[myownclone]] solo se sostiene si se demuestra que el `/visitors` de MyClone no persiste perfil de visitante. Marcado para juicio humano, no auto-resuelto.

---
id: 2026-1023-lzt-superficie-de-avisos-faq-y-tickets
type: atom
certainty: solid
sources: [sources/2026-10-22-lzt-market-home.md]
links: ["[[2026-1022-soporte-al-cliente-separado-y-escalado]]", "[[2026-1022-myclone-competidor-arquitectura]]", "[[2026-1023-lzt-captura-parcial-sin-precios-ni-stock]]"]
---

## Claim
La captura de lzt.market expone una **superficie de servicio al cliente y de avisos** con cuatro piezas: un sistema de avisos con banner dismissible (`/account/dismiss-notice?notice_id=-1` y un enlace a "List Notices"), una página de cookie con su propia explicación (`/help/cookies`), una **FAQ** (`/help/faq`) y un sistema de **tickets de soporte** (`/support-tickets/open`). El aviso de cookies incluye el enlace "What is it?" a su propia página de ayuda, es decir que la documentación del sistema de avisos es parte del producto. Nota técnica: el parámetro `notice_id=-1` es un valor negativo, señal de que el caso "sin aviso concreto" (el banner genérico) se modela en el mismo endpoint que los avisos numerados.

## Why It Matters
Es la diferencia entre un marketplace y una plataforma: el ticket de soporte es un ticket de **disputa de transacción** (la unidad que se compra es una cuenta que puede no funcionar), no un ticket de soporte de software. Para el producto del vault, el modo soporte con escalado a humano y envío automático de email ([[2026-1022-soporte-al-cliente-separado-y-escalado]]) cubre el caso de "el clon no sabe responder", pero no el caso de "el usuario compró un bien y el bien está roto": ahí la operación es de mediation, no de retrieval. El sistema de avisos, con su dismissal persistido por `notice_id`, es además la vía por la que un operador comunica cambios de política a toda la base sin tocar la interfaz — relevante cuando el producto es transaccional y con miles de clientes ([[2026-1022-myclone-competidor-arquitectura]]).

## Nota de verificación
Las cuatro rutas y el parámetro `notice_id=-1` están transcritos literalmente. La captura **no** publica: contenido de la FAQ, tiempo de respuesta del soporte, tipos de ticket ni estados del ciclo de vida de una disputa.

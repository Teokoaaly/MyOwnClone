---
id: 2026-1022-modulo-reuniones-booking-video
type: atom
certainty: solid
sources: [raw/articles/myownclone-frontend-recon.md, raw/articles/myownclone-new-findings-may-2026.md]
links: ["[[myownclone]]", "[[2026-1022-soporte-al-cliente-separado-y-escalado]]", "[[multi-tenant-saas]]"]
---
## Claim
El módulo de reuniones de [[myownclone]] (`/admin/meetings/*`) incluye una página de reserva pública (`PublicBooking`) con calendario y detección automática de timezone, videollamadas servidas "on myownclone", grabación con transcripción, descarga de calendario ICS compatible con Google, Outlook, Office 365 y Apple, y una burbuja de chat del clon incrustada en las páginas de grabación.

## Why It Matters
Es la integración de scheduling de primer nivel que diferencia a un clon "que responde" de un clon "que agenda y atiende": la reserva es pública (no requiere sesión del admin), la llamada es un producto en sí mismo y la grabación con transcripción reutiliza el mismo pipeline de audio y texto que usa el clon. La burbuja del clon en las páginas de grabación es el patrón de "canal de conversión" más reutilizable del producto: cada activo grabable se convierte en una landing conversacional. En un modelo [[multi-tenant-saas]] esto significa que cada tenant tiene su propia superficie de reserva con su propia marca, y para el modelo de soporte de [[2026-1022-soporte-al-cliente-separado-y-escalado]] es el punto donde el escalado a humano deja de ser theory.

## Extensión (nuevos hallazgos, mayo 2026)
Los bundles separan explícitamente la superficie pública de la del creator: `PublicBooking` (calendario público con videollamada integrada e ICS para Google/Outlook/Apple), `MyBooking` (vista de reserva con videollamada servida en myownclone y cancelación) y `PublicRecording` (grabación con transcripción + chat con el clon IA contextual). Que la videollamada se serve "en myownclone" y no en un proveedor third-party, y que la grabación tenga su propio chat contextual, convierte cada sesión en un activo conversacional reutilizable — el mismo activo que el creator puede embeber. Ver [[2026-1022-mapa-modulos-internos-desde-bundles-js]].

---
id: 2026-1026-mailsac-throttling-en-las-direcciones-publicas-y-buzon-unificado-de-equipo
type: atom
certainty: solid
sources: [sources/2026-10-25-mailsac-test-email.md]
links: ["[[2026-1026-onlinesim-numeros-gratis-publicos-renovados-a-diario]]", "[[2026-1022-myclone-access-control-por-persona]]", "[[2026-1023-5sim-casos-de-uso-qa-y-privacidad]]"]
---

## Claim
La gratuidad de la ruta pública viene con **dos límites explícitos** y uno de ellos es un límite de tasa: "Sending to any address @mailsac.com works, but it's public and **subject to throttling**". Ningún otro dato numérico acompaña al throttling: la captura **no publica el límite** (ni de envío, ni de lectura, ni de buzones, ni de retención). En paralelo, la página describe el producto de equipo: "**Full Unified Inbox View** — Get a complete view of your application workflow with **multiple inboxes, recipients, and filters in a single view** for you and your team", más "You can share email test logins, access the same custom domains, **manage team API keys**, manage **sub-accounts**, and delegate management of certain tasks", y la sección de organización: "**Create spontaneous inboxes based on whatever criteria you see fit: environment, role, or scenario. You can even create an inbox on each test case.**"

## Why It Matters
Es el **contraste directo con el correo gratuito del resto del corpus**: OnlineSim publica un módulo de números gratuitos que **renueva a diario** y avisa de que sus números "**are public, so they may already be used**" ([[2026-1026-onlinesim-numeros-gratis-publicos-renovados-a-diario]]); MailS.ac declara el mismo carácter público pero **le pone un nombre de límite: throttling**, y lo compensa con una superficie de equipo (buzón unificado con filtros, sub-cuentas, claves de API por equipo, delegation) que es **producto de gestión de identidades de prueba**, no de buzones.

Dos consecuencias para el vault. La primera, la aritmética: **"gratis" en este sector no significa "ilimitado"**, y un throttling sin cifra publicada es exactamente el tipo de límite que hace un proveedor no cotizable — pero al revés que el resto del corpus, aquí **el límite está declarado**, lo que lo hace auditable en principle (aunque no medible con esta captura). La segunda, la de diseño: el patrón "**un buzón por caso de prueba**" es el que un equipo de QA necesita y no el que el mercado de registro masivo necesita — son buoyancy rules de propósito distinto, y el vault ya tiene el caso de uso de QA declarado por 5sim solo para SMS ([[2026-1023-5sim-casos-de-uso-qa-y-privacidad]]).

La conexión con el producto propio es de granularidad de acceso: MyOwnClone ya separa el acceso por persona ([[2026-1022-myclone-access-control-por-persona]]) y por tenant; el modelo de MailS.ac (sub-cuentas + claves de equipo + delegation) es **el mismo esquema aplicado a buzones**, y es la referencia de qué pedir a un proveedor si el vault quisiera externalizar la capa de correo de prueba.

Nota de verificación: la captura **no** publica la cifra del throttling ni los límites de los planes; las citas sobre equipo son texto de marketing sin detrás verificable.

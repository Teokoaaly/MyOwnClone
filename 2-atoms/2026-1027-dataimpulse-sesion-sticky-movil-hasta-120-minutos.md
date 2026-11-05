---
id: 2026-1027-dataimpulse-sesion-sticky-movil-hasta-120-minutos
type: atom
certainty: solid
sources: [sources/2026-10-26-dataimpulse-mobile-proxies.md]
links: ["[[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]", "[[2026-1026-decodo-sesion-sticky-hasta-30-minutos-contra-30-120-de-dataimpulse]]", "[[2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero]]", "[[2026-1022-myclone-scraping-ingestion-pipeline]]"]
---

## Claim
La página móvil **publica por fin la duración de la sesión sticky del pool móvil**: el bloque Key Facts dice **"120 min — STICKY SESSIONS"** con la glosa **"The same IP address remains active for up to 2 hours"**, el bloque de Social Media Management lista **"Active sessions up to 120 minutes"** y el FAQ de sticky dice **"users may activate stable sticky sessions up to 120 minutes"**. Las dos modalidades siguen coexistiendo: **"Users can choose between rotation mode, when IP changes on each request, or sticky sessions, which keep the same IP for up to 120 minutes"**.

## Why It Matters
Este dato **cierra la fricción que el thread tenía abierta** sobre el tipo más caro por gigabyte: el móvil a $2/GB (el doble que el residencial a $1/GB) era precisamente el pool cuya sesión sticky estaba **sin cifra de duración**, y el vault ya tenía anotado que "para un flujo que necesita la misma IP durante una verificación con confirmación humana, la duración de la sesión es el parámetro que decide si el flujo se rompe". Con 120 minutos publicados, **el móvil es hoy la sesión sticky más larga medida en el corpus** (residencial 30–120 min, datacenter 30 min, Decodo 30 min como tope absoluto, [[2026-1026-decodo-sesion-sticky-hasta-30-minutos-contra-30-120-de-dataimpulse]]).
La consecuencia operativa es directa para el patrón de verificación del vault: HeroSMS exige que la IP coincida con el país del número y prohíbe varias cuentas desde la misma IP ([[2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero]]); **una ventana de 120 minutos cubre un flujo completo de alta —registro, SMS y confirmación por email— en una sola sesión**, sin que la rotación rompa la coherencia de IP a mitad. Es exactamente lo que la §8.2 del thread describía como "tres sesiones, no una" cuando el tope era de 30 minutos.

## [FRICTION]
> [[2026-1024-dataimpulse-sesiones-rotating-y-sticky]] afirma, para el pool móvil, **"Sticky sessions como característica destacada, sin duración declarada"**, y su Nota de verificación dice literalmente que "la captura no publica el rango exacto de la sesión sticky móvil".
> Este átomo **presiona ese dato**: la captura móvil del 2026-10-26 sí lo publica, y lo publica en el **máximo del rango residencial** (120 minutos), no en el mínimo de 30 que la home daba como valor por defecto. Es decir, el "sin cifra" del átomo viejo no era una ausencia de dato sino una ausencia de página: el dato estaba en la landing de producto, no en la home.
> Ambas no pueden ser completamente correctas: o la cifra de 120 minutos es del **pool móvil**, que es lo que dice esta página, o es una fórmula de marketing reutilizada del residencial y el móvil conserva el tope de 30 minutos — la captura móvil **no** dice qué pasa si se pide más de 120. Marcado para juicio humano, no auto-resuelto: la página no publica el mecanismo de renovación ni el límite por plan.

## Nota de verificación
Cifras y frases transcritas literalmente de "Key Facts", "Social Media Management" y "Can I use mobile proxies for social media automation?". La captura **no** publica: si la sesión sticky se renueva automáticamente, el número máximo de sesiones concurrentes, ni si el tope de 120 minutos es igual para el plan Intro de $5 que para el Custom+ de 5 TB+.

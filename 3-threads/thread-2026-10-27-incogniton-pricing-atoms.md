## 2026-10-27-incogniton-pricing Atoms — 2026-10-27

Created 4 atomic notes from capture `2026-10-27-incogniton-pricing.md` (sources/2026-10-27-incogniton-pricing.md, 1893 words). Atoms extracted from Incogniton pricing page covering 4 tiers, cookie policy, antidetect browser features, and payment/VAT.

### Atoms created:

1. **2026-1027-incogniton-precios** — Estructura de 4 niveles de precios: Starter Plus $13.99/mo (10 perfiles, 1 Cloud Phone gratuito 1 mes), Entrepreneur $20.99/mo (50 perfiles, integración Selenium/Puppeteer, API Access, Cookie Collector, Synchronizer), Professional $55.99/mo (150 perfiles, 3 asientos de equipo), Custom Package $104.99+/mo (500+ perfiles, gerente de cuenta dedicado, SLA). Todos los planes tienen descuentos 6 meses (30%) y anual (40%). El trial de 2 meses para Starter Plus que descuenta a 3 perfiles después es un gancho de conversión clave.

2. **2026-1027-incogniton-cookies** — Política de cookies clasificada en tres categorías: **Funcional** (siempre activas, necesarias para la funcionalidad del sitio), **Estadísticas** (recogen datos estadísticos anónimos para análisis de uso), **Marketing** (crean perfiles de usuario para enviar publicidad o hacer seguimiento en varios sitios). La disponibilidad de funcionalidades como Cookie Collector y Profile Synchronizer varía por plan, y los usuarios que rechacen cookies de marketing pueden tener acceso limitado a características de seguimiento ligadas a la optimización de conversión de planes.

3. **2026-1027-incogniton-fingerprinting** — Navegador antidetect con motor de antidetect que mascara huellas dactilares, fingerprints de dispositivos reales, paste as human typing para simular entrada humana natural, soporte Widevine DRM para contenido streaming, y compatibilidad con Pixelscan / BrowserLeaks / BrowserScan para evadir scripts de detección. El motor de fingerprint está disponible en todos los planes, pero características avanzadas como Selenium/Puppeteer integration, API Access y Cookie Collector están gated por tier. Usuarios en Starter Plus pueden ejecutar navegadores con fingerprint masking pero no pueden acceder a los endpoints de API que automatizan creación de perfiles a escala.

4. **2026-1027-incogniton-pago-vat** — Métodos de pago: Stripe, PayPal, tarjetas de crédito (Visa, Mastercard, American Express) y criptomonedas (BTC, ETH, LTC, DOGE, Dai). VAT puede aplicarse en ciertos países para servicios digitales. Empresas registradas para VAT pueden entrar su número de negocio y VAT number para estar exentas del cargo VAT, tal como se explica en la guía de edición de detalles de cuenta. Los fallos de pago suelen atribuirse a retrasos y los usuarios deben contactar soporte para activar suscripciones con anticipación.

### Cross-atom tensions:

- **Cookies vs. funcionalidad de planes**: La política de cookies (3 categorías con diferentes niveles de activación automática) cruza con la disponibilidad de características en los planes de precios. Características como Cookie Collector y Profile Synchronizer dependen del almacenamiento de preferencias de usuario, por lo que el rechazo de cookies de marketing podría afectar el acceso a estas funcionalidades, contradiciendo la afirmación de que el motor antidetect está disponible en todos los planes por igual.

- **Fingerprinting vs. consentimiento de cookies**: El motor antidetect y los fingerprints reales pueden depender de cookies de funcionalidad y preferencias para mantener consistencia de fingerprint entre sesiones. Si un usuario bloquea cookies de marketing, la capacidad del sistema para mantener perfiles coherentes a través de sesiones podría verse afectada, lo que contradice la afirmación de disponibilidad universal del motor.

- **VAT vs. perfil de negocio**: El tratamiento VAT y las exenciones basadas en registro empresarial cruzan con la política de cookies y el perfil de usuario. Las cookies de Marketing recogen datos de perfiles de usuario que, en ciertas jurisdicciones, podrían activar obligaciones de declaración fiscal o afectar la elegibilidad para exenciones VAT basadas en el perfil de negocio del usuario.

### Follow-up needed:

- Verificar el impacto del bloqueo de cookies de marketing en la disponibilidad de Cookie Collector y Profile Synchronizer en cada plan de precios.
- Testing de fingerprint persistence bajo bloqueo de cookies para determinar si el motor antidetect mantiene consistencia de fingerprint cuando el usuario rechaza categorías de cookies.
- Análisis jurisdiccional del impacto del consentimiento de cookies en la responsabilidad VAT y elegibilidad para exenciones basadas en perfil de negocio.
- Monitorear si Incogniton agrega nuevas categorías de precios o características que requieran átomos adicionales.
- Evaluar si los bloques [FRICTION] entre pares de átomos necesitan actualización después de juicio humano.

### Additional notes:

- Fuente única: `sources/2026-10-27-incogniton-pricing.md` (captura de la página de precios de Incogniton, 1893 palabras, fecha de captura 2026-10-27).
- Cierto `certainty` es solid en todos los átomos basado en datos literales de la captura de la página de precios.
- La red de enlaces [[wikilink]] forma un grafo completo entre los 4 átomos: precios ↔ cookies ↔ fingerprinting ↔ pago-VAT, permitiendo tracing cross-cutting themes across pricing structure, cookie policy, browser fingerprinting, and payment/VAT treatment.
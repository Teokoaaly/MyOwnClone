---
id: 2026-1026-heroku-soporte-superficie-legal-en-trailblazer-y-salesforce
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-support-home.md]
links: ["[[2026-1026-heroku-tres-variantes-de-privacy-por-region-y-consentimiento-de-marketing]]", "[[2026-1026-heroku-soporte-canales-externos-stackoverflow-y-pagina-de-estado]]", "[[2026-1023-live-verify-aviso-legal-aun-declara-vercel]]"]
---

## Claim
El pie de la home de soporte de Heroku declara **cinco enlaces legales y corporativos, y ninguno de ellos está en `heroku.com` salvo uno**: **"Terms of Service"** apunta a un **PDF alojado en `trailblazer.me`** (`trailblazer.me/resource/documents/documents/pdf/TermsOfUse_en_US.pdf`), **"Privacy"** a `www.salesforce.com/company/privacy/`, **"Cookies"** a `www.salesforce.com/company/privacy/full_privacy.jsp#nav_info`, **"Cookie Preferences"** a un ancla interna `help.heroku.com/#`, y **"Your Privacy Choices"** a `www.salesforce.com/form/other/privacy-request/`. El copyright es **"© 2026 Salesforce.com"**. El único enlace a `heroku.com` del pie es el logo (`www.heroku.com/`), y el único enlace de política propio del conjunto es **"Heroku Security"**, que apunta a `www.heroku.com/policy/security/`.

## Why It Matters
El dato duro es que **los Términos de Servicio de Heroku se sirven como PDF desde `trailblazer.me`**, el dominio de Trailhead, la plataforma de formación de Salesforce. Es decir, **la capa legal de un PaaS de Salesforce cuelga de una marca de formación de Salesforce**, no de un dominio corporativo de Salesforce — una señal precisa de hasta dónde llega el efecto de "todo es Salesforce" en un producto que se vende con su propia marca.
El vault ya había registrado que el pie del **alta** declara que "your personal data will be processed by Salesforce" con cuatro bloques regionales de Privacy Statement ([[2026-1026-heroku-tres-variantes-de-privacy-por-region-y-consentimiento-de-marketing]]). Esta captura añade la pieza que faltaba: **el soporte tiene su propio pie legal, con el mismo operador y los mismos destinos**, más un formulario de "Your Privacy Choices" — el mecanismo de solicitud de derechos de dato que en el alta no aparecía.
Y hay un precedente en el vault exactamente del tipo contrario: el Aviso Legal del producto propio declara "Vercel Inc." mientras la infraestructura real es nginx en una IP ([[2026-1023-live-verify-aviso-legal-aun-declara-vercel]]). El caso Heroku es el simétrico: **la identidad legal es coherente con el operador real — Salesforce — y por eso mismo no hay ninguna identidad "Heroku" que pueda reclamar la cuenta**. Para el thread de reventa de cuentas, esto importa: **no hay entidad legal bajo la que un comprador pueda reclamar** el acceso a una cuenta de infraestructura cuyo titular formal es Salesforce.

Nota: la captura **no** reproduce el texto de los Términos de Servicio ni su fecha de versión; solo el enlace al PDF.

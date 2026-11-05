---
id: 2026-1026-heroku-alta-seis-campos-y-empresa-acepta-el-email
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-signup.md]
links: ["[[2026-1024-chatgpt-creator-alta-por-correo-sin-telefono-en-el-flujo]]", "[[2026-1022-live-verify-alta-y-precios-ya-publicos]]", "[[2026-1024-anubiz-sin-kyc-registro-anonimo-con-cripto]]"]
---

## Claim
El formulario de alta de `https://signup.heroku.com/` pide **seis campos, todos obligatorios** (marcados con `*`): **First name, Last name, Email address, Company name, Country/Region y State**. El campo de empresa lleva la ayuda literal **"\\*No company? Enter your email, again."**, es decir que **el mismo correo electrónico puede servir como nombre de empresa**. El desplegable de **Country/Region** enumera más de 240 entradas (de "United States" a "Zimbabwe"), y el de **State** solo ofrece los 50 estados de EE.UU. más District of Columbia, American Samoa, Guam, Northern Mariana Islands, Puerto Rico, U.S. Virgin Islands y U.S. Minor Outlying Islands.

## Why It Matters
Es el **formulario de alta de una plataforma de hosting de nivel enterprise** medido con el mismo rigor con que el vault midió el alta de un bot contra ChatGPT. Y el patrón es el mismo que allí, con una diferencia de grado: contra OpenAI el alta documentada es de **nueve pasos y verificación por OTP de correo, sin teléfono** ([[2026-1024-chatgpt-creator-alta-por-correo-sin-telefono-en-el-flujo]]); aquí **la verificación visible es un captcha**, no un OTP, y la identidad que se pide es **corporativa y geográfica** (empresa + país + estado), no personal.
La frase "No company? Enter your email, again." importa porque **degrada la regla de empresa obligatoria a un campo nominalmente obligatorio pero semánticamente vacío**: el formulario no verifica nada del campo que pide. Es exactamente el patrón que el vault ya registró en el otro extremo del mercado, en el registro sin KYC de Anubiz ([[2026-1024-anubiz-sin-kyc-registro-anonimo-con-cripto]]), pero aquí en un proveedor de infraestructura y con una capacidad de marca detrás: **la misma holgura de identidad que en un exchange cripto se paga con límites de volumen, en un PaaS se paga con acceso a la cuenta y a la facturación**.
Y sirve de línea de base frente al alta del producto propio, que es self-service con cuatro campos (`name`, `personality`, `language`, `confirm`) más magic link ([[2026-1022-live-verify-alta-y-precios-ya-publicos]]): **el formulario de Heroku pide seis campos frente a los cuatro del nuestro, y ninguno de los seis que exige es de identidad verificable**.

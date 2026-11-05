---
id: 2026-1026-heroku-soporte-catorce-categorias-con-identificadores-numericos
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-support-home.md]
links: ["[[2026-1026-heroku-soporte-basico-gratis-y-success-plans-enterprise]]", "[[2026-1026-heroku-postgres-essential-5-a-20-dolares-con-4-horas-de-parada]]", "[[2026-1026-heroku-kafka-desde-100-dolares-con-1-semana-de-retencion]]"]
---

## Claim
La home de soporte de Heroku publica su **taxonomía documental como una lista de 14 categorías, cada una con un identificador numérico estable en la URL** (`help.heroku.com/n/<id>/<slug>`): **General Platform Features (236)**, **Account Management (5)**, **Domains & Routing (8)**, **Security (12)**, **Billing, Verification & Payments (2)**, **Heroku Postgres (3)**, **Heroku Connect (10)**, **Heroku Key-Value Store (22)**, **Apache Kafka on Heroku (21)**, **Heroku AppLink (538)**, **CI, Pipelines & Review apps (15)**, **Platform Error Codes (248)**, **Command Line Tools (268)** y **Add-on Provider (533)**. La instrucción de uso es literal: *"Select a topic, then pick a category and we'll show you commonly asked questions and answers."* Los identificadores **no siguen orden de creación ni de importance**: el 2 es billing y el 538 es AppLink.

## Why It Matters
Es la única captura del vault que documenta **cómo está organizada la superficie de soporte de un PaaS enterprise**, con identificadores que permiten seguir la línea documental por producto. Y su reparto es el dato: de las 14 categorías, **cuatro son de datos gestionados** (Postgres 3, Connect 10, Key-Value Store 22, Kafka 21) y **dos son de identidad/facturación** (Account Management 5, Billing, Verification & Payments 2). Es decir, el soporte de Heroku está dimensionado alrededor de lo que el vault ya mide como su parte cara — Postgres desde $5 ([[2026-1026-heroku-postgres-essential-5-a-20-dolares-con-4-horas-de-parada]]), Kafka desde $100 ([[2026-1026-heroku-kafka-desde-100-dolares-con-1-semana-de-retencion]]) — y de lo que el vault encuentra más frágil: la verificación de la cuenta, que tiene categoría propia ([[2026-1026-heroku-alta-protegida-por-recaptcha-enterprise-de-imagenes]]).
La categoría con id más alto, **Add-on Provider (533)**, indica además que el soporte cubre a terceros que venden sobre la plataforma, no solo a Heroku.
Y el marco encaja con lo que el pricing ya decía: la oferta de soporte es una **línea de producto** —Basic gratuito, tres planes Enterprise de pago sin precio publicado ([[2026-1026-heroku-soporte-basico-gratis-y-success-plans-enterprise]])— y esta captura muestra **la parte que el pricing no publica: dónde vive esa línea cuando el cliente tiene un problema**.

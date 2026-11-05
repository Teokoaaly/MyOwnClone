---
type: desk-note
date: 2026-11-04
target: 3-threads/economia-de-la-verificacion-y-reventa-de-cuentas.md
---

# Actualización del thread de verificación y reventa de cuentas — 2026-11-04

Hilo destino: `3-threads/economia-de-la-verificacion-y-reventa-de-cuentas.md` (único archivo modificado en el vault).
Fuentes nuevas leídas: `sources/2026-11-03-auth0-pricing.md`, `sources/2026-11-03-workos-pricing.md`, `sources/2026-11-03-twilio-sms-pricing.md`.
Átomos leídos: los 18 del 2026-11-03 indicados en el encargo (10 Auth0, 5 WorkOS, 3 Twilio/MMS). Ningún átomo ni fuente modificados.

## Secciones añadidas

- **§14. Tercera vuelta de identidad y SMS: las capturas del 2026-11-03 (Auth0, WorkOS, Twilio)** — nueva sección de síntesis, colocada justo antes del bloque "Nota de método".
  - **§14.1 Auth0: 5 Organizations en Free y 10 en Essentials, y el umbral de fricción real** — tabla comparativa 1/3/12/∞ (feature matrix del 2026-11-01) frente a 5/10 Organizations (tarjetas de plan del 2026-11-03); $35/$240 bajo el encabezado "B2B BILLING"; header "Flexible pricing … from user 1 to 1,000,000+"; entornos producción/desarrollo; Log Streaming a SIEM incluido en Essentials; "Secure Agentic AI workflows" en Free; las 4 features de seguridad de Professional ($240) y Enterprise en "Contact us"; verificación de tarjeta para el dominio personalizado; franja de 16 logos enterprise; render de 540 palabras sin tablas ni feature matrix.
  - **§14.2 WorkOS: la calculadora, el ancla de "$100 to build it yourself" y el positioning** — calculadora interactiva con deslizador por producto y default "$0/month $0.00 — Free" + CTA "Schedule a call"; literal "vs $100 to build it yourself" en SSO y Directory Sync frente a la escalera $125/$100/$80/$65; "Expand your market" / "Crossing the Enterprise Chasm" / "What happens if you don't become Enterprise Ready?"; inventario de 10 funciones de AuthKit (Organization auth policies, CLI Authentication, JIT, passkeys…); volcado crudo de 580 palabras sin tabla "Support Plans" y con "Need additional scale? Talk to us" en lugar del rung "101+ | Custom".
  - **§14.3 Twilio: el MMS entrante, la tercera renderización y el recomendador con OpenAI** — MMS entrante $0.0165 (long/short codes) y $0.02 (toll-free) frente a $0.022 outbound, adjuntos de 5 MB y 1.600 caracteres; tercera variante de render (texto plano, 9.029 bytes, word_count 610) con las tablas intactas pero sin Traffic Optimization Engine, sin descuentos comprometidos y sin enlaces CSV; recomendador de productos con IA híbrido Twilio+OpenAI y su descargo legal.
  - **§14.4 Lo que esta tanda deja escrito para el producto** — tres conclusiones: umbral de fricción de identidad movido y no zanjado; la elección de proveedor de identidad es decisión de go-to-market antes que de coste; ninguna cifra de esta tanda es un compromiso.
- **§13.5 Fricciones añadidas por la octava tanda (43–44)** — nueva subsección dentro de §13, siguiendo el patrón de §13.4 (que ya numeraba 39–42).
  - Fricción **43**: Auth0 cuenta "Organizations" (5/10) donde el thread contaba tenants (1/3/12/∞) — contradicción no resuelta, con la consecuencia aritmética (umbral en el 6º cliente, no en el 2º).
  - Fricción **44**: una captura reducida no es ni evidencia de estabilidad ni de retirada; regla (a) ausencia ≠ retirada, (b) contradicción sí es señal.
- **Nota de método — octava tanda** — párrafo añadido al final del bloque "Nota de método" (después de la séptima tanda, para conservar el orden cronológico): nombra las tres fuentes, declara que todas las cifras son transcripciones de páginas públicas no verificadas contra contrato/cotización/panel/factura, mantiene la distinción medición/claim (esta tanda no tiene ninguna medición; solo diff entre capturas y ausencias documentadas) y advierte que los renders reducidos no deben leerse como ofertas retiradas.

## Frontmatter actualizado

- `updated: 2026-11-03` → `updated: 2026-11-04`.
- `sources:` — añadidas las tres capturas nuevas (`sources/2026-11-03-auth0-pricing.md`, `sources/2026-11-03-workos-pricing.md`, `sources/2026-11-03-twilio-sms-pricing.md`). Total: 29 fuentes; las 26 previas conservadas.
- `links:` — añadidos los 18 wikilinks de los átomos del 2026-11-03 (10 Auth0, 5 WorkOS, 3 Twilio/MMS), más dos que el cuerpo nuevo cita y que no estaban en la lista: `2026-1101-workos-plan-scale-de-soporte-1000-al-mes` y `2026-1102-workos-el-plan-scale-perdio-revision-trimestral-y-configuracion`. Total: 135 enlaces, todos únicos. Ninguna fuente ni enlace previo eliminado.

## Links añadidos (18 átomos nuevos + 2 de apoyo)

Auth0: `2026-1103-auth0-organizaciones-5-en-free-y-10-en-essentials`, `2026-1103-auth0-precios-35-y-240-bajo-el-encabezado-b2b-billing`, `2026-1103-auth0-header-precios-flexibles-hasta-millon-de-usuarios`, `2026-1103-auth0-entornos-produccion-y-desarrollo-separados-en-essentials`, `2026-1103-auth0-log-streaming-a-siem-incluido-en-essentials`, `2026-1103-auth0-workflows-agentes-ai-incluidos-en-plan-free`, `2026-1103-auth0-professional-4-features-de-seguridad-enterprise`, `2026-1103-auth0-custom-domain-free-exige-verificacion-de-tarjeta`, `2026-1103-auth0-lista-de-clientes-enterprise-en-la-pagina-de-precios`, `2026-1103-auth0-captura-reducida-sin-tablas-ni-feature-matrix`.
WorkOS: `2026-1103-workos-se-posiciona-como-puente-al-mercado-enterprise`, `2026-1103-workos-inventario-de-funciones-de-authkit`, `2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call`, `2026-1103-workos-vs-100-para-construir-sso-o-scim-uno-mismo`, `2026-1103-workos-captura-cruda-no-trae-tabla-de-soporte`.
Twilio/MMS: `2026-1103-mms-inbound-0-0165-y-0-02-en-toll-free`, `2026-1103-twilio-tercera-renderizacion-texto-plano-sin-algunas-secciones`, `2026-1103-twilio-el-recomendador-de-productos-usa-openai-y-procesa-la-entrada-del-usuario`.
Apoyo (ya existentes en `2-atoms/`, añadidos al frontmatter porque el cuerpo nuevo los cita): `2026-1101-workos-plan-scale-de-soporte-1000-al-mes`, `2026-1102-workos-el-plan-scale-perdio-revision-trimestral-y-configuracion`.

## Fricciones y afirmaciones tocadas (solo seguimiento; nada borrado ni reescrito)

- **§13.1 (afirmación existente sobre tenants de Auth0).** El hilo afirmaba "los tenants incluidos escalan 1/3/12/ilimitado según el plan" y "la identidad de Auth0 es gratuita hasta que necesitas un segundo tenant". Añadido un bloque `> **Seguimiento 2026-11-04 (§14.1): este recuento de tenants queda en disputa.**` que reconcilia explícitamente con 5/10 Organizations, deja claro que el texto de §13.1 **no se reescribe** y remite a la fricción 43. La conclusión aritmética se corrige solo en la §14.1 y en la fricción 43.
- **Fricción 42 (el precio de lista no es el precio / lo que el proveedor no publica).** Añadido `> **Seguimiento 2026-11-04 (§14.3)**` con el caso de prueba de Twilio: la tercera renderización no muestra el Traffic Optimization Engine ni los descuentos comprometidos, y eso **no** los retira. Añadido un segundo `> **Seguimiento 2026-11-04 (§14.1)**` con el caso de Auth0 ($35/$240 bajo el encabezado B2B frente a $150/$800), que sí es contradicción y no simple ausencia.
- **Fricción 41 y 40 y 39.** Revisadas: no entran en contradicción con el material nuevo (41 trata de $0.0075 vs $0.0083 en Twilio; 40 trata del corpus de capturas de 5sim/PriceAI; 39 trata del sprintf de características de Clerk). Sin seguimiento añadido.
- **Fricciones 43 y 44.** Nuevas, en §13.5.
- **Fricción sobre el plan Scale de WorkOS** (pérdida de "Quarterly architecture review" y "End-user configuration support", [[2026-1102-workos-el-plan-scale-perdio-revision-trimestral-y-configuracion]]): el 2026-11-03 no aporta evidencia; queda registrada como **sin resolver** dentro de la fricción 44, sin tocar el átomo.

## Pending items (no resueltos, dejados explícitos en el hilo)

1. **Auth0 1/3/12/∞ vs 5/10 Organizations** — contradicción viva (fricción 43). El hilo usa "5 / 10 organizations, en disputa con el 1 / 3 del feature matrix" y no resuelve.
2. **Auth0 B2B $150/$800 vs $35/$240** — el átomo es `tentative`; la explicación (columna mal leída) es hipótesis, no texto de la fuente. Regla operativa adoptada: ningún precio de Auth0 se fija sin re-verificar contra la tabla completa.
3. **WorkOS plan Scale de $1.000/mes** — la composición sigue sin cotizar; el 2026-11-03 no trae la tabla de soporte.
4. **WorkOS $2.500/mes por millón adicional de MAU** — el 2026-11-03 no publica cifra alguna por encima de 1M de MAU; sigue `tentative`.
5. **Auth0 "Organizations ilimitadas" en B2B Essentials** — la tarjeta del 2026-11-03 muestra un tope de 10, incompatible con la lectura del feature matrix del 2026-11-01. No resuelto.
6. **Cifras por MAU y feature matrix de Auth0** — ausentes del render del 2026-11-03; no confirmables ni refutables con esta fuente.
7. **Ancho de banda de precios de Twilio por país** — sigue en `SMSPricing.csv`; no recuperada.
8. **Precio de almacenamiento de logs de Auth0** — la página publica el streaming pero no el almacenamiento; línea de consumo acumulativo sin cotizar.
9. **Descargo legal del recomendador de Twilio/OpenAI** — registrado como dato de página; el vault no ha evaluado el procesamiento de entradas de usuario (fuera de alcance de este encargo).
10. **Límites del plan Free de Auth0 para agentes (Actions/Forms, Token Vault, CIBA no disponible)** — el átomo lo deja como límite real del plan gratuito, distinto del add-on +50 %; no se ha integrado en la tabla de costes del producto (fuera del encargo).

## Errores y decisiones de proceso

- Ningún error de herramienta. Los `read_file`/`patch`/`terminal` terminaron con éxito.
- Un artefacto de edición: un párrafo de la §14.4 salió con un token corrupto ("由此") y otro con "nicotizado"; ambos corregidos con parche puntual. Verificado por grep de caracteres CJK en el hilo (las coincidencias restantes son el término legítimo "中转" de la nota de método preexistente).
- La nota de método de la octava tanda se movió al final del bloque "Nota de método" (detrás de la séptima tanda) para no romper el orden cronológico de las notas de tanda.
- No se modificó ningún archivo del vault fuera de `3-threads/economia-de-la-verificacion-y-reventa-de-cuentas.md` y esta nota de `1-desk/` (que house-rules marca como espacio de trabajo temporal). Fuentes y átomos: solo lectura.

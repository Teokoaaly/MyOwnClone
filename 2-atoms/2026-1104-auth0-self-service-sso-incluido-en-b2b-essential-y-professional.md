---
id: 2026-1104-auth0-self-service-sso-incluido-en-b2b-essential-y-professional
type: atom
certainty: solid
sources: [sources/2026-11-04-auth0-pricing.md]
links: ["[[2026-1101-auth0-sso-scim-en-free-pero-no-en-essentials-b2c]]", "[[2026-1101-auth0-addon-sso-enterprise-100-usd-por-conexion]]", "[[2026-1104-auth0-render-completo-restaurado-tras-el-reducido-del-11-03]]", "[[2026-1103-auth0-captura-reducida-sin-tablas-ni-feature-matrix]]"]
---

## Claim
En el feature matrix completo de Auth0, la fila **"Self-Service SSO"** tiene valores **distintos en B2C y en B2B**: en B2C es "Included | **Not available** | **Not available** | Select Enterprise Plans" (Free / Essentials / Professional / Enterprise), mientras que en **B2B es "Included | Included | Included | Select Enterprise Plans"**. La fila **"Inbound SCIM"** es **"Included" en las cuatro columnas en ambas matrices** (B2C y B2B), sin excepción. La única fila donde B2C pierde capacidad al subir de plan es **"Enterprise Connections"**: 1 (Free) → "Not available" (Essentials y Professional) → "Custom Tiers" (Enterprise); en B2B es 1 → "3 + ADD-ON" → "5 + ADD-ON" → "Custom Tiers".

## Why It Matters
El dato reordena la decisión Auth0-vs-otra-cosa para un producto multi-tenant. Self-Service SSO **no se pierde al subir de plan en B2B**: está incluido desde Essentials. Lo que sí se pierde, en B2C, son las **Enterprise Connections** (las integraciones con IdPs empresariales AD/LDAP/SAML) y el Self-Service SSO. Eso significa que la pregunta que el vault tenía abierta —"¿puedo tener SSO/SCIM sin pagar?"— tiene una respuesta mucho mejor que la registrada: **SCIM está en todas partes, incluido el Free; Self-Service SSO está incluido en todo B2B desde $150/mes; lo que cuesta dinero es conectar IdPs empresariales** ([[2026-1101-auth0-addon-sso-enterprise-100-usd-por-conexion]]). Para un SaaS que sirve a empresas y quiere que cada cliente traiga su Okta o Entra, la partida real es el **número de conexiones** ($100/mes cada una, máx. 30), no el precio del plan ni el del SSO. Y la lectura asimétrica B2C/B2B encaja con la estructura de coste ya documentada ([[2026-1101-auth0-b2b-essentials-escala-por-mau]]): el Premium B2B no es "más features" genérico, es "todo lo que un cliente corporativo necesita", mientras que B2C Essentials es un plan de consumo sin capacidad de identidad corporativa.

## [FRICTION]
> [[2026-1101-auth0-sso-scim-en-free-pero-no-en-essentials-b2c]] (escrita el 2026-11-01) afirma, entre otras cosas: "mientras que en **B2B** Essentials/Professional **Self-Service SSO también es 'Not available'**", y construye su Claim sobre la idea de que Self-Service SSO y SCIM se pierden al subir de plan.
> Este átomo presiona eso porque el feature matrix completo de la **misma página** dice, literalmente, "| Self-Service SSO | Included | Included | Included | Select Enterprise Plans |" en la matriz **B2B**, y "| Inbound SCIM | Included | Included | Included | Included |" en **ambas** matrices.
> Ambas no pueden ser completamente correctas: o el átomo viejo leyó la columna equivocada (la de B2C) como si fuera la de B2B, o la página cambió entre el 11-01 y el 11-04. La segunda opción queda desmentida por el material: la captura del 11-04 es **byte a byte idéntica** a la del 11-01 ([[2026-1104-auth0-render-completo-restaurado-tras-el-reducido-del-11-03]]), de modo que la lectura literal del 11-01 también daba "Included" en B2B. Marcado para juicio humano, no auto-resuelto: el átomo viejo conserva su `Claim` original sin reescribir, y su parte correcta (Enterprise Connections y SCIM como diferencias B2C/B2B) sigue en pie.

## Nota de verificación
Las cuatro filas son lectura literal de `sources/2026-11-04-auth0-pricing.md`: líneas 398-399 y 403 (matriz B2C) y 502-503 y 507 (matriz B2B). La ausencia de las filas en las capturas del 11-03 (render reducido sin feature matrix, ver [[2026-1103-auth0-captura-reducida-sin-tablas-ni-feature-matrix]]) explica por qué la distinción no se había detectado antes.

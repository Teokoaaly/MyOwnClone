---
id: 2026-1104-auth0-enterprise-mfa-incluido-en-b2c-essentials-pero-addon-en-b2b
type: atom
certainty: solid
sources: [sources/2026-11-04-auth0-pricing.md]
links: ["[[2026-1101-auth0-addon-sso-enterprise-100-usd-por-conexion]]", "[[2026-1103-auth0-professional-4-features-de-seguridad-enterprise]]", "[[2026-1104-auth0-self-service-sso-incluido-en-b2b-essential-y-professional]]", "[[2026-1104-auth0-guia-de-cotizacion-en-7-pasos-incorporada-a-la-pagina]]"]
---

## Claim
El feature matrix de Auth0 **cobra distinto el Enterprise MFA según la columna de uso**: la fila "Enterprise MFA Factors" es **"Not available | Included | Included | Included" en B2C** (Free / Essentials / Professional / Enterprise) pero **"Not available | ADD-ON | Included | Included" en B2B**. La sección de add-ons, **publicada solo bajo B2B**, fija el precio: "Enterprise MFA: **Essentials: $100/month ($1,100/year)**; Professional: Included". Es decir, el **Enterprise MFA va incluido en Essentials B2C y se cobra $100/mes en Essentials B2B**. La fila contigua "Pro MFA Factors" es "Not available | Included | Included | Included" en ambas matrices: el factor MFA es gratis en Essentials y el "Enterprise" es un peldaño de pago aparte.

## Why It Matters
Es una asimetría de precio por caso de uso que el vault no tenía registrada y que cambia la comparación entre columnas: **B2C Essentials a $35/mes incluye Enterprise MFA**, mientras que **B2B Essentials a $150/mes lo cobra como add-on de $100/mes** — con lo que un cliente B2B que quiera MFA empresarial paga $250/mes en el escalón de entrada, más los $100 de cada conexión Enterprise que necesite ([[2026-1101-auth0-addon-sso-enterprise-100-usd-por-conexion]]). La consecuencia operativa para el vault: el precio "de entrada" de Auth0 no es $35 ni $150, es un precio **en dos ejes** (plan × add-ons de identidad), y el eje B2B puede triplicar el total antes de hablar de un solo usuario adicional. Eso refuerza el patrón que el vault ya registra en otros proveedores: comparar solo el precio base no sirve ([[2026-1031-workos-pricing]] cobra por producto y API, [[2026-1031-clerk-pricing]] incluye todo sin gating) — en Auth0 hay que cotizar **plan + MFA + conexiones + tokens M2M**, exactamente los cuatro add-ons que enumera el paso 5 de la guía de cotización que publica la propia página ([[2026-1104-auth0-guia-de-cotizacion-en-7-pasos-incorporada-a-la-pagina]]).

## Nota de verificación
Las filas "Enterprise MFA Factors" y "Pro MFA Factors" son lectura literal de las líneas 447-448 (matriz B2C) y 551-552 (matriz B2B) de `sources/2026-11-04-auth0-pricing.md`. El precio del add-on ($100/mes / $1.100/año en Essentials, incluido en Professional) es lectura literal de la sección "Enterprise MFA" bajo "B2B Add-ons" (líneas 369-371). La suma de $150 + $100 = $250 es un cálculo de este átomo, no una frase de la fuente.

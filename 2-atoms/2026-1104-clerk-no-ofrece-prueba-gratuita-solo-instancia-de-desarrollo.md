---
id: 2026-1104-clerk-no-ofrece-prueba-gratuita-solo-instancia-de-desarrollo
type: atom
certainty: solid
sources: [sources/2026-11-04-clerk-pricing.md]
links: ["[[2026-1104-clerk-recomienda-supabase-y-firebase-para-consumo-gratuito]]", "[[2026-1101-clerk-gating-por-plan-contradice-atom-1031]]", "[[2026-1101-clerk-precios-base-hobby-pro-business]]"]
---

## Claim
Clerk **no ofrece prueba gratuita con límite de tiempo**: la FAQ "Is there a free trial?" responde que "All of our **Pro tier features are available to try in the development instance** of your application, allowing you to test the full functionality of Clerk **without being constrained by a traditional trial period**", y añade que "All features are properly tagged in the Dashboard, so you'll know if a specific feature requires an upgrade to use in production". No hay ni días de prueba, ni saldo, ni activación automática de plan.

## Why It Matters
Es un mecanismo de entrada **distinto del de todo el resto del corpus de proveedores del vault**, donde la prueba gratuita es casi siempre un temporizador o un abono (DigitalOcean con crédito promocional, Decodo con 7 o 3 días, Proton con 30 días, Hostkey con 7 días). Aquí la prueba **es el entorno de desarrollo**: es decir, **se puede construir y probar en local todo el plan Pro —incluido MFA, passkeys, SSO, bans, blocklist— sin gastar un céntimo y sin límite de calendario**, y lo único que se paga es el salto a producción cuando la feature lo requiere. La consecuencia práctica para MyOwnClone es doble y favorable: **el coste de evaluar Clerk es de tiempo de integración, no de suscripción**, lo que invierte la carga de la decisión (si la app no se integra bien en el SDK, se pierde el trabajo, no el dinero). Y el matiz que la página sí explicita —"features properly tagged in the Dashboard, so you'll know if a specific feature requires an upgrade to use in production"— es la confirmación de que **el gating por plan es algo que se descubre en producción**, no en el dashboard: por eso la matriz de features ([[2026-1101-clerk-gating-por-plan-contradice-atom-1031]]) hay que leerla antes de integrar, no después.

## Nota de verificación
Sección "Is there a free trial?" de `sources/2026-11-04-clerk-pricing.md`, verbatim. La comparación con los mecanismos de prueba de otros proveedores del vault es lectura operativa de este átomo a partir de átomos previos.

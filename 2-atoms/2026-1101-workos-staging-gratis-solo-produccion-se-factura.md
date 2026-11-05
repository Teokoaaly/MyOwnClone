---
id: 2026-1101-workos-staging-gratis-solo-produccion-se-factura
type: atom
certainty: solid
sources: [sources/2026-11-01-workos-pricing.md, sources/2026-11-03-workos-pricing.md]
links: ["[[2026-1101-auth0-plan-free-25000-mau-sin-tarjeta]]", "[[2026-1101-clerk-plan-gratuito-50000-mru-y-3-asientos]]", "[[2026-1031-workos-authkit-primer-millon-de-mau-gratis]]", "[[2026-1103-workos-captura-cruda-no-trae-tabla-de-soporte]]"]
---

## Claim
En WorkOS **los entornos de staging son gratuitos y solo se factura el entorno de producción**: "Staging environments: Free for testing. Only production environments are billed." Además, WorkOS **no exige tarjeta de crédito hasta que se pasa a producción**.

## Why It Matters
Es la condición que hace viable probar la integración de identidad sin gastar: MyOwnClone puede montar NextAuth/SSO contra WorkOS en staging, con todos los productos disponibles, y solo incurre en coste cuando entra tráfico real. Comparado con el benchmark, la diferencia no es el precio sino el **modo de cobro**: Auth0 ofrece un Free de 25.000 MAU sin tarjeta ([[2026-1101-auth0-plan-free-25000-mau-sin-tarjeta]]) y Clerk un Hobby de 50.000 MRU ([[2026-1101-clerk-plan-gratuito-50000-mru-y-3-asientos]]), pero en ambos el plan gratuito **sí limita** el uso; en WorkOS no hay cuota, hay una frontera explícita staging/producción. Consecuencia práctica para el eje del vault: se puede **desarrollar y validar la ruta SSO completa sin cargo**, y el primer euro aparece solo con el primer cliente en producción — lo que convierte la decisión "WorkOS vs Auth0 vs Clerk" en una decisión de **cuándo se cobra**, y por tanto en una decisión que se puede aplazar mientras no haya cliente enterprise. Nótese que en WorkOS ese primer euro tampoco es por usuarios: es por conexión ([[2026-1031-workos-authkit-primer-millon-de-mau-gratis]]).

## 2026-11-03 — re-verificación
La captura del 2026-11-03 confirma el FAQ "Can I try WorkOS before paying for it?" ("WorkOS is free to get started and you don't need to add a credit card until you are ready to move to production") y **añade un FAQ nuevo** que la captura del 11-01 no recogía: "What's the difference between Staging and Production?" — "The staging environment is made for testing your integrations, while the production environment is built for live applications that use real customer data. **All WorkOS products are available in staging to try at no cost.**" Esa última frase es el matiz nuevo y el más fuerte: no es solo que staging sea gratuito, sino que **todos los productos** (incluidos SSO, Directory Sync, Audit Logs y Radar) están disponibles en staging sin coste, lo que permite validar la ruta SSO/SCIM completa antes de tener ningún cliente enterprise y antes del primer euro ([[2026-1103-workos-captura-cruda-no-trae-tabla-de-soporte]]).

## Nota de verificación
Definiciones de la captura del 2026-11-01 ("Staging environments: Free for testing. Only production environments are billed.") y FAQ "Can I try WorkOS before paying for it?" de la captura del 2026-10-31 ("WorkOS is free to get started and you don't need to add a credit card until you are ready to move to production").

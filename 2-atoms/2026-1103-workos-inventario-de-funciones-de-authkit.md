---
id: 2026-1103-workos-inventario-de-funciones-de-authkit
type: atom
certainty: solid
sources: [sources/2026-11-03-workos-pricing.md]
links: ["[[2026-1031-workos-authkit-primer-millon-de-mau-gratis]]", "[[2026-1031-workos-custom-domain-99-al-mes]]", "[[2026-1101-workos-staging-gratis-solo-produccion-se-factura]]"]
---

## Claim
La calculadora de **AuthKit** enumera **diez capacidades** que se incluyen sin línea de precio propia: **Social Auth** ("Authentication with Microsoft, Google, and more" — **"Available for all accounts"**), **Email + Password** ("Automatic password strength and leak detection"), **Magic Auth** ("Passwordless auth using six digit codes sent via email"), **Multi-Factor Auth** ("Additional authentication with TOTP and SMS"), **Email verification** ("Verify user email addresses with magic codes"), **Organization auth policies** ("Restrict domains, MFA, and SSO per organization"), **Just-in-time (JIT) user provisioning** ("Automatic provisioning based on email or SSO"), **Biometric / Passkey Auth**, **Role-Based Access Control (RBAC)** y **CLI Authentication** ("Quickly add auth to your command-line tools").

## Why It Matters
Es el **inventario funcional** del producto de identidad de WorkOS en la captura del 2026-11-03, y en la práctica significa que el precio de AuthKit es un único número (MAU) que cubre un paquete de capacidades que en otros proveedores se cobran por separado (MFA, passkeys, social auth, verificación de email). Para MyOwnClone la lectura operativa es doble. Primera: **CLI Authentication** y **JIT provisioning** son las dos piezas que interestan a un producto de clones IA por API — CLI auth porque el producto se consume programáticamente y JIT porque evita aprovisionar a mano a cada tenant. Segunda: "Organization auth policies" (restringir dominios, MFA y SSO **por organización**) es la capacidad que hace de AuthKit un sustituto plausible de un IdP por tenant, es decir, encaja con un modelo multi-tenant donde cada cliente es una organización ([[2026-1022-costes-por-categoria-tenant]]).

Nótese el matiz de pricing de esta lista: **ninguna de estas capacidades tiene línea de precio separada** en la página; la única línea que las monetiza es el MAU ([[2026-1031-workos-authkit-primer-millon-de-mau-gratis]]), y la única que monetiza el *branding* es el dominio personalizado, que además cubre el "email sender address" ([[2026-1031-workos-custom-domain-99-al-mes]]).

## Nota de verificación
Lista de features bajo el bloque "### AuthKit" de sources/2026-11-03-workos-pricing.md, verbatim en cada descriptor. El único ítem con marca explícita de disponibilidad es "Social Auth — Available for all accounts"; los restantes se listan sin indicación de plan ni de precio.

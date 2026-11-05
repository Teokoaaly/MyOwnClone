---
id: 2026-1026-hero-sms-migracion-sms-activate-a-hero-sms
type: atom
certainty: solid
sources: [sources/2026-10-26-hero-sms-api-docs.md]
links: ["[[2026-1027-hero-sms-trece-operaciones-de-activacion]]", "[[2026-1027-hero-sms-openapi-3-2-0-con-api-key-en-la-cabecera-authorization]]"]
---

## Claim

HeroSMS publica un proceso de **4 pasos para migrar desde SMS-Activate**: (1) **elige cualquier software** que incluya SMS-Activate entre sus servicios de recepción de SMS, (2) **selecciona SMS-Activate** como el servicio para recibir SMS, (3) **reemplaza el host** de `https://api.sms-activate.ae/` a `https://hero-sms.com/` en la configuración de tu software, y (4) **ingresa la clave API** de tu cuenta HeroSMS (solicítala en nuestra web).

## Why It Matters

Este es el **camino oficial de onboarding para integradores** que migran del ecosistema SMS-Activate a HeroSMS. A diferencia de 5sim, donde la automatización está dentro del producto, HeroSMS coloca la responsabilidad en el integrador: el cambio de host es una configuración unificada y la clave API se obtiene fuera del panel, lo que hace que el coste de integración sea **distinto al de 5sim** —aunque la API de HeroSMS publica su contrato (OpenAPI 3.2.0, apiKeyAuth, trece operaciones), como se documenta en [[2026-1027-hero-sms-openapi-3-2-0-con-api-key-en-la-cabecera-authorization]].

## Nota de verificación

El proceso de 4 pasos —elige software SMS-Activate, selecciona el servicio, reemplaza el host a hero-sms.com, ingresa la clave API solicitada en la web— es **transcripción literal** de `sources/2026-10-26-hero-sms-api-docs.md` (líneas 21-24). La captura **no** publica: el flujo completo en la home, el precio de la clave API, los límites de llamadas, ni las condiciones comerciales del programa de partners.

## [FRICTION]

> [[2026-1023-herosms-api-y-partners-de-registro-masivo]] afirma que la home de HeroSMS ofrece el botón "Get API key" **sin publicar documento, endpoint, precio ni condiciones**, y de ahí diagnostica un **mayor coste de integración** que 5sim. La captura de la API `2026-10-26` contradice la premisa: **el documento de la API sí está publicado** en `hero-sms.com/en/api`, con OpenAPI 3.2.0 descargable, esquema de autenticación explícito y trece operaciones enumeradas. Lo que **sigue sin publicarse** son los precios y las condiciones comerciales —el 404 de `/pricing` se mantiene ([[2026-1024-herosms-url-de-precios-devuelve-404-y-no-publica-precios-propio]]). Ambas no pueden ser completamente correctas: o la API seguía sin documentar, o el coste de integración de HeroSMS es comparablemente bajo una vez leída la especificación. Marcado para juicio humano, no auto-resuelto.
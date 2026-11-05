---
id: 2026-1026-mailsac-los-buzones-publicos-son-legibles-por-cualquiera
type: atom
certainty: solid
sources: [sources/2026-10-25-mailsac-test-email.md]
links: ["[[2026-1024-chatgpt-creator-correo-temporal-y-otp-automatico-con-generator-email]]", "[[2026-1022-auth-magic-link-codigo-seis-digitos]]", "[[2026-1026-mailsac-correo-desechable-para-testing-de-qa-y-no-de-registro-masivo]]"]
---

## Claim
MailS.ac declara explícitamente que **cualquiera puede leer un buzón `@mailsac.com`**: "**Public and free:** anyone can read an @mailsac.com inbox, so use made-up data. **Private when it matters:** the free plan includes one private address, and paid plans from $18 a month add custom test domains that only your team can read". El FAQ lo repite con la misma estructura: "@mailsac.com inboxes are public, so use made-up data. For test mail that only your team can read, create a free account: it includes an API key and one private address, and paid plans add custom test domains". Y la respuesta a "Can other people see my email messages?" es: "Email messages are private to your account when using a custom domain or custom private forwarding address. Sending to any address @mailsac.com works, but it's public and subject to throttling".

## Why It Matters
Es la **regla de higiene del sector** que el vault no tenía enunciada por ningún proveedor: en la ruta pública del correo desechable, **la bandeja es un documento público**, y el único dato que el proveedor considera sensible es la recepción de un código. Es exactamente la forma del producto del vault: el magic link de 6 dígitos llega por email ([[2026-1022-auth-magic-link-codigo-seis-digitos]]).

La consequence is architectural and it cuts both ways: por un lado, MailS.ac **sí** ofrece la variante privada sin coste relevante —el plan gratuito incluye **una dirección privada** y una **API key**—, de modo que un equipo de QA puede tener una bandeja cerrada sin pagar. Por otro, el umbral que separa "buzón anónimo" de "buzón de equipo" está declarado en el propio texto: **no es el plan, es el nombre del dominio**.

## [FRICTION]
> [[2026-1024-chatgpt-creator-correo-temporal-y-otp-automatico-con-generator-email]] describe el flujo del bot de registro masivo como "**OTP Verification — Automatic email OTP retrieval and validation**", es decir, el bot **recoge el código del correo temporal por su cuenta** y lo teclea solo, con un buzón generado por `generator.email` y un código visible en la traza (`Validate OTP [483291] | 200`).
> Este átomo presiona esa creencia en un punto: **existe un proveedor del mismo sector que declara por escrito que su buzón desechable es legible por cualquiera**, y que solo un buzón privado o un dominio propio dan confidencialidad ([[2026-1026-mailsac-correo-desechable-para-testing-de-qa-y-no-de-registro-masivo]]). Si el buzón temporal del bot es del mismo tipo —público y anónimo—, entonces **el OTP que el bot teclea estaba, durante la ventana de espera, en una bandeja que podía leer un tercero**, y el vault no tiene ninguna evidencia en la fuente de que `generator.email` sea privado.
> Ambas no pueden ser completamente correctas: o el generador del bot produce buzones privados —y entonces su flujo es seguro por una propiedad que el README **no documenta**—, o produce buzones públicos y el flujo es inseguro por construcción. Marcado para juicio humano, no auto-resuelto: el README de `chatgpt-creator` no publica ni el modelo de privacidad ni los términos de `generator.email`.

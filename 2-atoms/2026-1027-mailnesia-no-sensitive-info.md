---
id: 2026-1027-mailnesia-no-sensitive-info
type: atom
certainty: solid
sources: [sources/2026-10-27-mailnesia.md]
links: ["[[2026-1027-mailnesia-disposable-without-registration]]", "[[2026-1026-mail-tm-la-promesa-de-captcha-solving-evitada-por-el-buzon]]"]
---

## Claim

Mailnesia warns users not to send any sensitive information (financial, online banking) because anyone could read it after guessing the mailbox name.

## Why It Matters

Mailnesia is a public temporary email service where any visitor who knows the recipient name can view incoming emails. This is not a private communication channel. Sending credentials, financial data, or OTP codes via Mailnesia exposes that information to anyone who discovers or guesses the mailbox name, creating a significant security risk for accounts and financial data.

## [FRICTION]

> [[2026-1026-mail-tm-la-promesa-de-captcha-solving-evitada-por-el-buzon]] (escrita hace ~4 semanas) afirma que el buzon como escudo evita captcha-solving. La advertencia de Mailnesia sobre información sensible y la nota de captcha operan en dominios separados: la primera es un aviso de seguridad sobre el modelo de amenaza (cualquier persona con el nombre de buzon puede leer), y la segunda es sobre la experiencia de registro (auto-clickeo de links de verificación). No hay conflicto directo, pero en un flujo de trabajo completo, un usuario podría sentirse seguro usando Mailnesia para verification codes y luego inadvertidamente enviar datos sensibles thinking que el "escudo" del buzón también protege contra el envío de información confidencial, cuando en realidad el modelo de amenaza es diferente: el riesgo no es la interceptación del codigo, sino el acceso no autorizado al buzón. Marcado para juicio humano, no auto-resuelto.
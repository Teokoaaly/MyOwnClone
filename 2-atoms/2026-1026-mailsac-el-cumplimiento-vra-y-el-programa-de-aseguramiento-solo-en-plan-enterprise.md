---
id: 2026-1026-mailsac-el-cumplimiento-vra-y-el-programa-de-aseguramiento-solo-en-plan-enterprise
type: atom
certainty: solid
sources: [sources/2026-10-25-mailsac-test-email.md]
links: ["[[2026-1024-1984-hosting-certificacion-iso-27001]]", "[[2026-1023-priceai-descargo-de-responsabilidad-sin-sla]]", "[[2026-1024-2captcha-solo-se-paga-por-captcha-resuelto]]"]
---

## Claim
MailS.ac publica un bloque de cumplimiento **explícito y con condiciones de tier**: "We have many customers in finance, government, scientific research, and the high tech industries. In these environments we can provide a copy of our **Information Assurance Program**, **security scanning results**, and help you complete a **Vendor Risk Assessment (VRA)**. Note: **only supported for our Enterprise plan tier**." El SSO está en la misma lógica de gating: "Single-sign-on is supported via SAML on the **Business, Business+ and Enterprise plans**. Users need to be added in mailsac first, by email address", y la facturación por orden de compra también: "Purchase order billing is supported on **annual Business+ and Enterprise plans**. We recommend a **2-year billing cycle**". El claim de clientela: "About half of mailsac's customers are enterprise scale."

## Why It Matters
Es el **único proveedor de correo desechable del corpus que publica un artefacto de cumplimiento**, y lo hace con la variable de tier explícita: la VRA y el Information Assurance Program son **Enterprise**, el SSO es **Business y upwards**, y la orden de compra es **Business+ anual y Enterprise**. La composición de la base de clientes ("about half ... are enterprise scale") explica por qué el gating esBusiness-heavy: el producto de consumo gratuito no sostiene el coste de cumplimiento.

El contraste con el resto del sector del vault es instructivo. En el hosting, la norma del sector es **certificación publicada y verificable** —ISO/IEC 27001, GDPR, BSI C5 en el caso de Hetzner ([[2026-1024-1984-hosting-certificacion-iso-27001]]). En el mercado de la verificación y el elusión, la norma es el **descargo de responsabilidad** ([[2026-1023-priceai-descargo-de-responsabilidad-sin-sla]]) o el "paga solo por lo resuelto" sin SLA contractual ([[2026-1024-2captcha-solo-se-paga-por-captcha-resuelto]]). MailS.ac introduce una **tercera forma**: no hay SLA de servicio ni certificación, pero hay un **proceso deDue diligence** que el proveedor admite y que el cliente ejecuta.

## [FRICTION]
> [[2026-1023-priceai-descargo-de-responsabilidad-sin-sla]] y el resto del corpus del thread sostienen la tesis de que **el mercado de la verificación no tiene contrato**: ni SLA, ni cumplimiento auditable, ni continuidad de contraparte — la §5 del thread contrapone ese perfil con el de Hetzner, "el único sitio de la captura donde el número y el contrato son la misma cosa".
> Este átomo presiona esa tesis en un punto: **MailS.ac sí tiene contrato**, y tiene un proceso de cumplimiento, solo que en forma de **cambio de manos en vez de documento** —el proveedor entrega el Information Assurance Program, los resultados del escaneo de seguridad y ayuda a completar la VRA, pero el artefacto de cumplimiento es del cliente y el derecho a obtenerlo está atado a un tier de pago. Es decir, o "el mercado de la verificación no tiene contrato" describe **al mercado de la reventa de cuentas y los números**, en cuyo caso hay que excluir explícitamente a MailS.ac, o la tesis es falsa tal como está redactada porque ya existe un contraejemplo en el mismo sector.
> Marcado para juicio humano, no auto-resuelto: la captura **no** publica ni el contenido del Information Assurance Program, ni los resultados del escaneo, ni el precio del tier Enterprise, así que no se puede verificar el alcance real del cumplimiento.

Nota de verificación: las condiciones de tier están transcritas literalmente; no se ha contactado con `support@team.mailsac.com` ni solicitado ningún documento.

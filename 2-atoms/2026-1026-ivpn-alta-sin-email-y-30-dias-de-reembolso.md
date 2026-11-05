---
id: 2026-1026-ivpn-alta-sin-email-y-30-dias-de-reembolso
type: atom
certainty: solid
sources: [sources/2026-10-25-ivpn-pricing.md]
links: ["[[2026-1024-mullvad-garantia-de-reembolso-14-dias-excepto-efectivo-por-aml]]", "[[2026-1024-proton-30-dias-de-dinero-devuelto-y-cambio-de-plan-con-credito-prorrateado]]", "[[2026-1024-mullvad-pago-en-efectivo-por-sobre-con-token-aleatorio]]"]
---

## Claim
IVPN publica tres condiciones comerciales de alta en su página de precios, en tres líneas: **«No email required for signup»**, **«30-day refund window»** y **«Cash, Monero, Bitcoin accepted»**. Es decir, **el alta no pide correo electrónico**, la ventana de reembolso es de **30 días**, y entre los métodos de pago figura el **efectivo**.

## Why It Matters
«No email required for signup» es una **claim de_surface de la página de precios**, no una cláusula, y es el dato más operativo de la captura para un vault que usa el correo como punto de apoyo de identidad ([[2026-1023-hero-sms-numeros-de-un-solo-uso-y-recuperacion-por-email]]): si el alta no exige correo, el identificador de la cuenta del VPN **no nace como una dirección**, y por tanto el vector de correlación entre "servicio de salida" y "cuenta de correo" del producto propio se reduce. La ventana de **30 días** empata con la de Proton y duplica la de Mullvad, y el hecho de que IVPN la publique **junto a la aceptación de efectivo sin ninguna excepción** es exactamente el punto que hay que mirar, porque en Mullvad esa excepción existe y está justificada por AML ([[2026-1024-mullvad-garantia-de-reembolso-14-dias-excepto-efectivo-por-aml]]).

## [FRICTION]
> [[2026-1024-mullvad-garantia-de-reembolso-14-dias-excepto-efectivo-por-aml]] (escrita el 2026-10-24) afirma, interpretando a Mullvad, que "**el pago más anónimo es el único irreembolsable**, y la razón que da el proveedor es normativa (AML), no comercial", y generaliza: "todo es reembolsable salvo el modo que no deja rastro".
> Este átomo presiona eso porque IVPN publica **«30-day refund window»** y **«Cash ... accepted»** en la misma página **sin ninguna exclusión**: o el patrón de Mullvad es una **idiosincrasia de ese proveedor** y no la norma del sector —en cuyo caso el "efectivo no reembolsable" no puede usarse como regla general del vault—, o el efectivo de IVPN **no es el efectivo anónimo** de Mullvad (sobre con token aleatorio, [[2026-1024-mullvad-pago-en-efectivo-por-sobre-con-token-aleatorio]]) sino una vía de pago identificable, y entonces "acepta efectivo" no dice nada sobre anonimato.
> Ambas no pueden ser completamente correctas. Marcado para juicio humano, no auto-resuelto: la captura **no especifica el mecanismo del pago en efectivo de IVPN** (ni si es postal, ni si exige referencia), de modo que la comparación no puede cerrarse.

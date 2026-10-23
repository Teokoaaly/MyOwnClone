---
id: 2026-1023-sms-activate-retiradas-hasta-el-5-de-febrero
type: atom
certainty: solid
sources: [sources/2026-10-22-sms-activate-closed.md]
links: ["[[2026-1023-hero-sms-modelo-pay-per-use-y-tabla-real-vs-virtual]]", "[[2026-1023-hero-sms-reembolso-si-no-llega-sms-en-20-minutos]]", "[[2026-1023-sms-activate-cierra-total-el-22-de-diciembre]]"]
---

## Claim
La ventana de **retirada de fondos ("вывод средств")** estuvo disponible **hasta el 5 de febrero** y después se cerró. SMS-Activate afirma que lo notificó "a cada usuario por email y en el bot" y añade el motivo del cierre de la vía: "К сожалению, больше некому обрабатывать ваши запросы" — después de esa fecha **ya no hay nadie que gestione las solicitudes**. Es decir, el saldo retenido después del 5 de febrero no tenía ni operación ni interlocutor.

## Why It Matters
Este es el **rastro de saldos** del modelo prepago que el vault viene documentando en los proveedores vivos: prepago sobre saldo sin suscripción ([[2026-1023-hero-sms-modelo-pay-per-use-y-tabla-real-vs-virtual]]), con reembolso automático al saldo si la unidad no cumple ([[2026-1023-hero-sms-reembolso-si-no-llega-sms-en-20-minutos]]). El aviso de SMS-Activate es el **caso terminal** de ese modelo: cuando el operador se apaga, el saldo deja de ser un crédito exigible y pasa a ser dinero atrapado. La fecha del 5 de febrero marca la frontera exacta entre "saldo retirable" y "saldo perdido".
Para el vault, esto convierte el prepago sobre saldo en un riesgo con dos capas: el riesgo ya conocido (la unidad no cumple, se reembolsa) y un riesgo nuevo y mayor (**la desaparición del operador**, del que la garantía de reembolso no protege). Cualquier comparación de coste entre proveedores debe incluir quién responde si el proveedor cierra.

## [FRICTION]
> [[2026-1023-hero-sms-reembolso-si-no-llega-sms-en-20-minutos]] (escrita hoy, desde la home de HeroSMS) trata la garantía "No SMS received within 20 minutes? Get an instant automatic refund to your balance" como un **compromiso comercial auditable**, con el riesgo financiero asumido por el proveedor limitado al "tiempo de saldo bloqueado".
> Este átomo presiona esa creencia porque la otra mitad del modelo no está en ninguna de las dos páginas: en HeroSMS **no existe vía de retirada de fondos**. El reembolso automático solo es exigible mientras la empresa exista y su bot siga vivo; el precedente de SMS-Activate (saldo sin poder sacarse tras el 5 de febrero) muestra que el mecanismo de protección se evapora con el proveedor, y no está cubierto por ninguna cláusula.
> Ambas no pueden ser completamente correctas: o el reembolso automático es una garantía efectiva y transferible —en cuyo caso falta documentar qué la respalda—, o es una promesa operativa que solo existe mientras el proveedor siga operando. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
El aviso no publica el número de cuentas afectadas, ni el saldo agregado pendiente, ni el motivo por el que el cierre fue "total" pero las retiradas tuvieran un mes y medio de margen extra. La notificación "por email y en el bot" es una declaración del operador, no verificable desde la captura.

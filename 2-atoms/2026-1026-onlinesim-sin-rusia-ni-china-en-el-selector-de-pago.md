---
id: 2026-1026-onlinesim-sin-rusia-ni-china-en-el-selector-de-pago
type: atom
certainty: solid
sources: [sources/2026-10-25-onlinesim-virtual-sms.md]
links: ["[[2026-1023-herosms-20-paises-enumerados-contra-180-declarados]]", "[[2026-1023-sms-activate-cierra-total-el-22-de-diciembre]]", "[[2026-1023-5sim-catalogo-153-paises-contra-180-de-la-home]]"]
---

## Claim
El selector de países del pie de OnlineSim enumera **107 entradas** con prefijo y **no incluye ni Rusia (+7) ni China (+86)**, aunque sí incluye **Belarus +375, Ucrania +380, Kazajistán +77, Kirguistán +996 y Uzbekistán +998**, además de **Irán +98, Taiwan +886 y Hong Kong +852**. El módulo de números gratuitos, con **132 páginas**, **sí ofrece China** (`/free_numbers/china`) y **`belorussia`**, pero **tampoco ofrece Rusia**.

Comparado nombre a nombre, el conjunto de 107 del pie es un **subconjunto estricto** del gratuito de 132: **no hay ni un solo país del pie que falte en el gratuito**, y los **25 exclusivos del gratuito** son Afghanistan, Azerbaiyán, Camboya, China, Cuba, República Dominicana, Ecuador, Etiopía, Gibraltar, Guinea, Honduras, Irak, Israel, Jordania, Mónaco, Nepal, Nicaragua, Pakistan, Paraguay, Senegal, Sri Lanka, Tayikistán, Togo, Túnez y Venezuela. Es decir: **el gratuito tiene 25 países que el de pago no**, y el de pago ninguno que el gratuito no tenga.

Errores de rotulación que aparecen **en ambas listas**: **"Sierre Lyone+232"** (que es el prefijo de Sierra Leona) y, en el gratuito, **"Canada +1000"** y **"Dominican Republic +1001"** —dos países NANP con prefijos de cuatro dígitos inventados, frente al **"USA +1"** correcto de la misma lista.

## Why It Matters
La dirección del subconjunto es el dato: **lo que se puede comprar es un recorte de lo que se puede tener gratis**, y el recorte no elimina los países "exóticos" sino un conjunto concreto —los mismos que el resto del corpus del thread identifica como los de mayor riesgo regulatorio o de menor cobertura en otros proveedores: Cuba, Israel, Irak, Tayikistán, Cambodia, Pakistan, Senegal, Honduras. La ausencia de **Rusia** con presencia simultánea de **Bielorrusia, Ucrania, Kazajistán, Kirguistán y Uzbekistán** es una pista fuerte sobre el linaje del inventario: el operador rusófono que el vault ya documentó (SMS-Activate, cerrado; HeroSMS como heredero technology-wise, [[2026-1023-sms-activate-cierra-total-el-22-de-diciembre]]) sirve números de **esos** países y no del suyo. Un proveedor que **hereda** ese pool y **excluye precisamente el mercado doméstico del emisor** no puede ser su simple fachada: o son dos pools distintos, o la herencia no es el mecanismo.
Sobre China, el desajuste entre lo que el pie de pago ofrece y lo que el gratuito sí ofrece es exactamente la forma que tiene la cobertura como **propiedad del producto** y no del proveedor: no es que falte el país, es que falta el **stock pagable**.
Y los tres errores de rotulación ("Sierre Lyone", "Canada +1000", "Dominican Republic +1001") confirman que las dos listas son **copias manuales curadas**, no tablas generadas — lo que las hace documentos que sí se pueden leer y auditar, a diferencia de los contadores de marketing ([[2026-1026-onlinesim-cifras-de-cobertura-98-107-110-y-132]]).

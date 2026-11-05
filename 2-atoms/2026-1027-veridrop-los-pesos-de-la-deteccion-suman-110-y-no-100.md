---
id: 2026-1027-veridrop-los-pesos-de-la-deteccion-suman-110-y-no-100
type: atom
certainty: tentative
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-pesos-de-los-11-detectores-y-el-contexto-largo-de-pago]]", "[[2026-1027-veridrop-los-tres-modos-de-deteccion-y-sus-conteos-no-coinciden-entre-paginas]]", "[[2026-1024-veridrop-metodo-de-la-puntuacion-mediana-publica]]"]
---

## Claim
Sumando los once pesos que la FAQ publica — 25 + 15 + 12 + 10 + 10 + 10 + 8 + 5 + 5 + 5 + 5 — se obtiene **110 %**, no 100 %. Los once pesos corresponden a los once detectores nombrados ("11 项常规检测"), así que **cada detector tiene un peso nominal y el total no está normalizado a 100**. La lectura más probable es que los pesos sean **relativos** (una escala de importance interna) y que el score final se normalice aparte; pero la captura **no publica la fórmula de agregación**, de modo que el vault no puede confirmar que el scorePublished sea una media ponderada normalizada.

## Why It Matters
El vault ya tiene una friction abierta exactamente de esta forma: el "公开检测综合中位分 99/100" se publica **sin definir cómo se agrega** ([[2026-1024-veridrop-metodo-de-la-puntuacion-mediana-publica]]), y aquí aparece la pieza que faltaba — **la tabla de pesos sí está publicada, pero no su normalización**. Es decir: la detección interna de una fila puede ser reproducible, pero el **número de 0 a 100 que se muestra sigue sin fórmula publicada**, y por tanto sin ser auditable.
La consecuencia práctica es una caution que aplica a cualquier integración de este tipo: **un score con tabla de pesos publicada no es necesariamente un score reproducible**, y la diferencia entre las dos cosas es justamente lo que un verificador independiente necesita. Si el vault construyera su propia métrica de proveedor, tendría que **publicar el denominador y la normalización** — que es el requisito que este detector, en su parte pública, todavía no cumple.

## Nota de verificación
La suma es un cálculo del vault sobre los pesos literales de la FAQ (110 de un total nominal de 100). La inferencia "pesos relativos" es **tentativa**: la captura no publica la fórmula. Ver también [[2026-1027-veridrop-los-tres-modos-de-deteccion-y-sus-conteos-no-coinciden-entre-paginas]], que es otra inconsistencia interna de la misma página.

## [FRICTION]
> [[2026-1024-veridrop-metodo-de-la-puntuacion-mediana-publica]] (escrita el 2026-10-24, captura `sources/2026-10-23-veridrop-relays.md`) afirma que el "公开检测综合中位分 99/100" se publica **sin definir cómo se agrega** y que la puntuación proviene de **agregación de informes públicos**, fuera del control directo de VeriDrop. Esta nota presiona esa creencia porque la FAQ de VeriDrop afirma lo contrario en dos puntos: **"代码完全开源(AGPL-3.0),评分公式公开,可逐行审计"** y **"检测算法对所有中转站一视同仁"**. El conflicto no es de mauvaise fe sino de alcance: **la fórmula puede ser pública y auditable línea a línea sin que la agregación a mediana de informes públicos esté definida**, y los pesos publicados que suman 110 % son exactamente el tipo de hueco que la auditoría línea a línea no cierra. Ambas no pueden ser completamente correctas: o la fórmula del score individual es reproducible (y entonces la mediana es solo una agregación simple) o no lo es. Marcado para juicio humano, no auto-resuelto.

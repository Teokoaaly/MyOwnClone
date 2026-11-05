---
id: 2026-1026-brightdata-limite-de-1000-requests-por-minuto-en-cuenta-sin-fondos
type: atom
certainty: solid
sources: [sources/2026-10-25-brightdata-free-tier.md]
links: ["[[2026-1026-brightdata-5000-creditos-gratis-al-mes-para-cuentas-nuevas]]", "[[2026-1024-brightdata-suspender-pierde-las-ips-y-limite-de-uso-por-zona]]", "[[2026-1024-brightdata-ancho-de-banda-contado-en-dos-sentidos-con-cabeceras]]"]
---

## Claim
Las cuentas **sin fondos depositados** (free tier puro) están sujetas a un **límite de tasa por defecto de 1.000 requests por minuto**, transversal a **SERP API, Web Unlocker API y productos proxy**: *"Accounts operating on the free tier (unfunded) are restricted to a default rate limit of 1,000 requests per minute across the SERP API, Web Unlocker API and Proxy products."* El límite **se elimina automáticamente en cuanto se añaden fondos**, y se consulta en el Control Panel, en *zone's Overview tab > Access details*.

## Why It Matters
Es un límite **por ventana de tiempo**, no por saldo ni por zona, y es el único límite de cadencia que el vault ha encontrado publicado en el sector de scraping. Se combina con el límite de gasto por zona que el vault ya tenía registrado —"usage spend limit" por bytes o por dólares, recalculado **cada 15 minutos**, con suspension automática de la zona ([[2026-1024-brightdata-suspender-pierde-las-ips-y-limite-de-uso-por-zona]])— para formar un **doble techo**: uno de ritmo y otro de volumen.
La lectura operativa es contra-intuitiva: **funded = más límites, unfunded = menos servicios pero ritmo suficiente**. Con 1.000 requests/minuto, el free tier no es un modo de crippled para un pipeline: es un modo con **más cadencia que cualquier presupuesto pequeño se vería obligado a contratar**. Lo que sí limita de verdad el free tier es el **número total de créditos al mes** (5.000), no el ritmo.
Y hay un detalle que importa para el modelado de ancho de banda: como el tráfico se factura **en dos sentidos y con cabeceras** ([[2026-1024-brightdata-ancho-de-banda-contado-en-dos-sentidos-con-cabeceras]]), los 1.000 requests/minuto son también la cota superior del tráfico que un free tier puede absorber antes de agotar los 1.000 MB de Browser API.

## Nota de verificación
Texto transcrito literalmente. La captura **no** publica: el límite de tasa de una cuenta funded, si el límite de 1.000/min es por cuenta o por zona, ni si las peticiones fallidas cuentan para el rate limit.

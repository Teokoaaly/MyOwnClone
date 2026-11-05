---
id: 2026-1026-serverhunter-anuncio-patrocinado-en-la-tabla-y-bloque-de-contabo
type: atom
certainty: solid
sources: [sources/2026-10-25-serverhunter-cheap-vps.md]
links: ["[[2026-1024-veridrop-home-los-parametros-pos-y-slot-revelan-el-bloque-patrocinado]]", "[[2026-1023-priceai-transit-patrocinadores-y-ranking-en-la-misma-pagina]]", "[[2026-1026-serverhunter-88559-servidores-de-971-proveedores]]"]
---

## Claim
La captura de ServerHunter contiene **dos superficies comerciales dentro de la página de resultados**. La primera es una **fila etiquetada "Ad" que ocupa la posición 1 de la tabla**, por encima de las ofertas de $0.29: es el **"AMD Ryzen 5600X Dedicated Server | 64GB RAM | 500GB NVMe (LAX)" de Ignero Corp a $99.00**, con "0/5 (0 reviews)" y Free setup. La segunda es un **bloque de banner al pie**, con enlace de seguimiento propio (`/offer/contabo-advertisement/visit/?ad=true`): *"Contabo offers 4 CPU cores, 8 GB of RAM, and 50 GB of NVMe SSD space for less than $6/month."* En ambos casos el contenido comercial es **una fila más de la misma tabla de precios**, no un bloque separado.

## Why It Matters
Es el **patrón que el vault ya catalogó dos veces en IA, ahora en infraestructura**: en PriceAI los patrocinadores están fusionados dentro de la propia tabla de precios ([[2026-1023-priceai-transit-patrocinadores-y-ranking-en-la-misma-pagina]]), y en VeriDrop el bloque pagado está separado y etiquetado con `sponsored=1`, `slot` y `pos` ([[2026-1024-veridrop-home-los-parametros-pos-y-slot-revelan-el-bloque-patrocinado]]). ServerHunter es el caso **sin etiqueta**: la fila "Ad" está **dentro de la tabla** y es la primera, de modo que un scraper que tomase "la primera fila = la más barata" se llevaría un dedicado de $99 en lugar de un VPS de $0,29. Y el precio del banner de Contabo es el dato nuevo: **4 cores, 8 GB de RAM y 50 GB NVMe por menos de $6/mes** — la primera cifra del vault para Contabo, y con specs declaradas.

## [FRICTION]
> [[2026-1024-veridrop-home-los-parametros-pos-y-slot-revelan-el-bloque-patrocinado]] sostiene que "lo que se ve en la home no es la cabeza del ranking, es **un bloque comprado y renumerado**", y su [FRICTION] método apunta que el parámetro `pos` empieza en 11 porque **el Top 10 no contiene a los diez mejores**.
> ServerHunter aplica un modelo **distinto**: el patrocinio no renumera ni desplaza un ranking con plazas numeradas, sino que **inserta una fila arriba del todo** de una tabla ordenada por precio, con una etiqueta "Ad" y un enlace de visita con UTM propio (`?ad=true`). Es decir: el veridrop usa *plazas compradas dentro de un ranking*; ServerHunter usa *una fila comprada antes del ranking*.
> Las dos afirmaciones no pueden ser a la vez el criterio del vault de "cómo se detecta el patrocinio en un agregador": o toda posición sponsored es visible por una etiqueta estructural (`slot`/`pos`), o **la etiqueta es la única marca y basta con que exista para contaminar el scraper**. Marcado para juicio humano, no auto-resuelto: la captura no publica si la fila "Ad" es fija o rotatoria, ni cuántas hay, ni sutarifa.

## Nota de verificación
El texto de Contabo, sus specs y el enlace con `?ad=true` están transcritos literalmente. El precio de la fila de Ignero Corp ($99.00) también. La captura **no** publica el número de anuncios, su precio ni el criterio de rotación, y **no** permite saber si la fila "Ad" está incluida en el recuento de 88.559 ofertas.

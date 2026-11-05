---
id: 2026-1104-digitalocean-afirma-ser-mas-barato-que-aws-ec2-y-gce-sin-publicar-precios-de-comparacion
type: atom
certainty: tentative
sources: [sources/2026-11-04-digitalocean-droplets-pricing.md]
links: ["[[2026-1104-digitalocean-captura-vuelve-a-render-completo-tras-el-render-reducido-del-3-nov]]", "[[2026-1102-digitalocean-la-pagina-de-droplets-no-publica-precios-de-volumes-ni-de-bases-de-datos-ni-de-gpu]]", "[[2026-1031-digitalocean-entrada-basic-512-mib-4-dolares-al-mes]]"]
---

## Claim
La FAQ de droplets de la captura del **2026-11-04** incluye dos comparativas con los hiperescaladores y, en la primera, una afirmación de precio: "In terms of pricing, DigitalOcean is generally more affordable for comparable resources" frente a **AWS EC2**, y para **Google Compute Engine** solo el encuadre de plataforma ("a more enterprise-focused platform with a vast array of services", con DO "known for their straightforward pricing and ease of use"). La página **no publica ninguna cifra de EC2 ni de GCE**, ni una tabla comparativa, ni los precios de los "comparable resources" que usa como referencia. La misma FAQ sí clasifica a Droplets como **IaaS** ("Infrastructure-as-a-Service") y aclara que el nombre "Droplet" es la marca de DigitalOcean para un **VPS** ("essentially, they are the same thing").

## Why It Matters
Es un **claim de marketing del proveedor, no una medición**, y hay que archivarlo como tal: la página afirma ser más barato que EC2 sin publicar ni un solo precio de EC2, así que **la afirmación no es verificable con esta fuente** — el vault no puede construir una comparación DO-vs-EC2 a partir de ella, ni siquiera como cota. El riesgo concreto para el vault es el mismo que ya está documentado con la tabla de BuyVM: cuando un tercero (o el propio proveedor) afirma un precio o una superioridad de precio, la cifra hay que buscarla **fila a fila en el catálogo del fabricante**, y aquí la única tabla publicada es la de DO, no la del competidor.

Lo que sí es aprovechable es el reverso: la propia página se define como **IaaS no gestionado** ("you are responsible for managing the server"), lo que confirma que el precio del Droplet es **solo el coste de la máquina** y no incluye parcheo, backups gestionados ni availability. Refuerza la lectura que ya tenía el átomo de ausencias: **la página de droplets no es un catálogo de coste total**, y la afirmación "más barato que AWS" se mueve en un terreno que el vault no puede cotizar porque el otro lado de la comparación no está publicado en ninguna parte de la fuente. Ver [[2026-1102-digitalocean-la-pagina-de-droplets-no-publica-precios-de-volumes-ni-de-bases-de-datos-ni-de-gpu]].

## Nota de verificación
Ambas respuestas de la FAQ transcritas literalmente de `sources/2026-11-04-digitalocean-droplets-pricing.md`. "DigitalOcean is generally more affordable for comparable resources" es una **afirmación del proveedor** ("generally", sin criterio ni fuente ni condición); no se contrasta con ningún precio de EC2 porque la captura **no contiene ninguno**. La equivalencia "Droplet = VPS" y la clasificación IaaS son definiciones del proveedor, no mediciones del vault. Este átomo está en `tentative` por el carácter del claim, no por dudas sobre la transcripción.

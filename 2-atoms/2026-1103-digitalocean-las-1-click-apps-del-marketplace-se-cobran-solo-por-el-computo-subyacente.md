---
id: 2026-1103-digitalocean-las-1-click-apps-del-marketplace-se-cobran-solo-por-el-computo-subyacente
type: atom
certainty: solid
sources: [sources/2026-11-03-digitalocean-droplets-pricing.md]
links: ["[[2026-1102-digitalocean-la-pagina-de-droplets-no-publica-precios-de-volumes-ni-de-bases-de-datos-ni-de-gpu]]", "[[2026-1031-digitalocean-droplets-pricing]]", "[[2026-1101-digitalocean-v5-droplets-precios-por-hora-y-sin-techo-de-672-horas]]"]
---

## Claim
La FAQ de precios de DigitalOcean afirma, sobre el **Marketplace de 1-Click Apps**: "We charge you for the underlying compute on which the 1-Click Apps runs". Es decir, **no hay una tarifa de licencia ni de marketplace por encima del Droplet**: el coste de una app preconfigurada es exactamente el coste del Droplet que la ejecuta. La captura **no publica** el catálogo de 1-Click Apps, ni sus precios, ni si hay apps de pago.

## Why It Matters
Resuelve una duda que el vault tenía abierta desde la captura del 2026-10-31 (donde la FAQ listaba "pre-configured 1-Click Apps for LAMP, Docker, WordPress, and more" sin decir nada de su coste) y que las capturas del 11-01/11-02 habían dejado sin cotizar: **las 1-Click Apps no son una partida de coste propia**. Para MyOwnClone esto significa que un stack LAMP/Docker desplegado por marketplace **no encarece el presupuesto**, siempre que se elija el Droplet más barato que lo soporte — y ese Droplet sigue siendo el Basic de $4.00/mes ([[2026-1031-digitalocean-droplets-pricing]]). Es el mismo patrón de "el software no se cobra, la máquina sí" que caracteriza al modelo v5, donde también solo se paga por los recursos configurados ([[2026-1101-digitalocean-v5-droplets-precios-por-hora-y-sin-techo-de-672-horas]]), y refuerza el patrón ya registrado de que esta página **no publica ninguna tarifa de producto adyacente** ([[2026-1102-digitalocean-la-pagina-de-droplets-no-publica-precios-de-volumes-ni-de-bases-de-datos-ni-de-gpu]]): lo único que hay que cotizar en DO es el Droplet.

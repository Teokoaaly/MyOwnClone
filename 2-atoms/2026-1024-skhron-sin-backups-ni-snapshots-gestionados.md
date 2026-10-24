---
id: 2026-1024-skhron-sin-backups-ni-snapshots-gestionados
type: atom
certainty: solid
sources: [sources/2026-10-23-skhron-bitcoin-vps.md]
links: ["[[2026-1024-evoxt-backup-semanal-offsite-gratuito]]", "[[2026-1024-hostbrr-backups-como-addon-opcional-con-gfs]]", "[[2026-1024-skhron-sin-ddos-por-cliente-ni-garantia]]"]
---

## Claim
Skhron declara: **"We don't offer managed backups or snapshots. Keeping backups of your data is your own responsibility – we recommend keeping regular off-server copies of anything important."**

## Why It Matters
Contraste directo con los otros dos proveedores del vault: Evoxt incluye **backup offsite semanal automático a coste cero** ([[2026-1024-evoxt-backup-semanal-offsite-gratuito]]) y HostBrr lo vende como **add-on opcional con GFS** ([[2026-1024-hostbrr-backups-como-addon-opcional-con-gfs]]); Skhron no ofrece ninguna de las dos cosas y transfiere la responsabilidad al cliente. Para MyOwnClone, que sirve inferencia y guarda conocimiento por tenant, la ausencia de snapshots significa que **cada despliegue de versión es una operación de riesgo sin red**: hay que hacer copia fuera del servidor antes de actualizar, lo que añade un coste operativo recurrente que no aparece en el precio del VPS. Es otro caso donde la privacidad y el precio bajo se pagan con servicios que el cliente debe construir.

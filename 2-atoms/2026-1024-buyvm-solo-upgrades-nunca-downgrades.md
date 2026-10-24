---
id: 2026-1024-buyvm-solo-upgrades-nunca-downgrades
type: atom
certainty: solid
sources: [sources/2026-10-23-buyvm-kvm-slices.md]
links: ["[[2026-1024-extravm-upgrade-con-prorrateo-pero-sin-downgrade]]", "[[2026-1024-buyvm-block-storage-slabs-1-25-por-256gb-y-migrables-sin-downtime]]", "[[2026-1024-buyvm-escalera-de-precios-slices-24-al-ano-a-15-al-mes]]"]
---
## Claim
La FAQ de BuyVM fija una política de ciclo de vida de **solo ampliación**: "Can I upgrade or downgrade your KVM Slice Server? **We only allow upgrading to a bigger plan. Downgrading can lead to data loss if the drive shrink fails and no one wants that.**" La página **no** publica: prorrateo, crédito por el tiempo no usado, ni mecanismo de cancelación o reembolso.

## Why It Matters
Es la misma política que ya tenía documentada ExtraVM ("upgrade con prorrateo pero sin downgrade", [[2026-1024-extravm-upgrade-con-prorrateo-pero-sin-downgrade]]), y por tanto **el patrón "crecer es libre, encoger no" ya no es una rareza de ExtraVM sino una convención del eje de hosting barato**. Para MyOwnClone, cuyo despliegue vivo es un nginx autoalojado ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]) y cuyo producto puede necesitar reducir footprint si la demanda cae, esa restricción implica **que el dimensionado inicial es irreversible**: el slice se paga para siempre o se abandona y se paga otro. La mitigación que ofrece la propia página es el almacenamiento en bloque migrable sin downtime ([[2026-1024-buyvm-block-storage-slabs-1-25-por-256gb-y-migrables-sin-downtime]]): los datos se pueden mover a un plan más pequeño **sin encoger el disco** — lo que hace la política mucho menos grave de lo que suena, siempre que el storage esté en slab y no en el disco del plan.

## Nota de verificación
Cita transcrita literalmente de la FAQ. La captura **no** publica política de cancelación, reembolso, ni prorrateo en el upgrade.

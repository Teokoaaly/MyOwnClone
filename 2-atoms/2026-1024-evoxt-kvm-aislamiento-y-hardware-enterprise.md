---
id: 2026-1024-evoxt-kvm-aislamiento-y-hardware-enterprise
type: atom
certainty: solid
sources: [sources/2026-10-23-evoxt-vms.md]
links: ["[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]", "[[2026-1024-evoxt-firewall-capa-3-sin-conexion-al-servidor]]", "[[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]", "[[2026-1024-evoxt-faq-vpn-personal-y-multiples-sitios]]"]
---

## Claim
Evoxt declara usar **hipervisores KVM** ("we use KVM hypervisors so you get the best performance and security"), **hardware de grado enterprise** ("we use enterprise grade hardware for increased performance and reliability") y un **entorno de VM aislado** que "previene el acceso no autorizado a tu servidor", con el dato de que "tus datos permanecerán en tu propio entorno seguro y aislado y en ningún otro sitio". En la misma sección de seguridad añade **protección DDoS** vía el firewall de capa 3.

## Why It Matters
El aislamiento es un argumento de venta que el vault puede contrastar con lo que el producto real hoy es: un nginx autoalojado en una IP concreta ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]), sin aislamiento de tenant documentado. KVM (frente a containers) implica que cada VM es una máquina dedicada con su propio kernel, lo que aísla el ruido entre tenants pero multiplica el coste de memoria frente a una arquitectura de contenedores en un mismo host — el trade-off real entre aislamiento y coste que el vault ya tiene documentado en la elección compartido/dedicado de Hetzner ([[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]). Para un SaaS multi-tenant de clones, el "aislamiento por VM" es un argumento de venta defendible y también una decisión de coste por tenant.

## Nota de verificación
La captura **no** publica el hardware concreto (modelo de CPU, RAM, tipo de disco), el tipo de almacenamiento, ni si el aislamiento es de proceso, de red o de credenciales. "Enterprise grade" es la formulación del proveedor, sin especificación.

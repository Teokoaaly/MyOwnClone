---
id: 2026-10-26-decodo-smartproxy-home
type: briefing
date: 2026-10-26
sources: [sources/2026-10-26-decodo-smartproxy-home.md]
--
# Briefing — Procesamiento de captura Decodo (antes Smartproxy) 2026-10-26

## Qué se procesó

Captura `0-raw/2026-10-26-decodo-smartproxy-home.md` (stub de 5 líneas) → fuente `sources/2026-10-26-decodo-smartproxy-home.md` (homepage completa de decodo.com, 1158 líneas, 33.071 palabras). La captura registra el estado "ready" y documenta la evolución de Smartproxy a Decodo, las ofertas de proxy y API, y el FAQ de preguntas frecuentes.

**Átomos creados: 3 nuevos** en `2-atoms/`, con prefijo `2026-1026-`:

1. `2026-1026-decodo-prueba-gratis-3-dias-y-plan-gratuito-api` — Dos mecanismos de entrada gratuitos: (1) trial de 3 días para proxies que **auto-activa el plan de pago** al finalizar, cancelando la garantía de 14 días que la home también publica, y (2) plan gratuito starter para Web Data API con **5 dólares en créditos (hasta 10K solicitudes) sin tarjeta de crédito**.

2. `2026-1026-decodo-115m-ips-residenciales` — **115M+ IPs éticamente sourcing** en la red residencial de Decodo, con targeting a nivel de continente, país, estado, ciudad y ASN gratis en todos los planes. Es la afirmación de escala más alta medida en el vault para cualquier proveedor de proxy.

3. `2026-1026-do-proxies-proporcionan-anonimato` — El FAQ aclara que los proxies enmascaran la IP pero el nivel de anonimato varía por proveedor; el riesgo de fallo de elusión recae en el cliente. También diferencia proxy de VPN: proxy opera en nivel de aplicación/conección, VPN en túnel encriptado para protección de datos. Esta distinción sella un modelo de riesgo que el vault registraba implícitamente en comparaciones de cobro (requests vs captchas resueltos) pero nunca había enunciado explícitamente.

## Hallazgos principales

- La home publica **dos tipos de entrada gratuitos con semántica de riesgo opuesta**: la trial de proxies convierte sola en compromiso (auto-activation), mientras que la API tiene plan gratuito permanente sin tarjeta. El vault debe cotizar **dos mecanismos de entrada distintos** para el mismo actor, con riesgo de auto-compromiso en uno y riesgo cero en el otro.

- La sección de **rebranding del FAQ** declara que Smartproxy.org no es Decodo y es un dominio de terceros ("Just be careful with the old name: Smartproxy.org isn't us"). Este aviso de suplantación de dominio sigue el mismo patrón que SMS-Activate ([[2026-1024-sms-activate-ru-sirve-el-mismo-aviso-que-el-dominio-org]]): un nombre que el público asocia al proveedor sigue activo siendo válido para un tercero, y el proveedor original tiene que avisar de ello. La diferencia es que aquí el aviso está en la home del impostado, es decir, es una defensa de marca proactiva.

- El **targeting a nivel de ASN es gratis en todos los planes** de Decodo (residencial, datacenter, ISP), mientras que competidores como DataImpulse lo cobran por país. Esto hace comparable el modelo de coste IP a IP con proveedores que sí cobran por geolocalización, reforzando la regla de que **el coste de cumplir el criterio país-real-de-la-IP es cero en Decodo**.

- Los **precios publicados en la home no siempre son el precio de entrada real**: el titular de "starting at $2/GB" es el mejor caso del catálogo, no el precio mínimo (el precio de arranque real es $3.75/GB por el plan de 3 GB). Esta discrepancia entre titular y entrada real se confirma en el átomo [[2026-1027-decodo-titular-de-2-por-gb-y-entrada-real-de-375]].

## Notas de proceso

- La captura en `0-raw/` era un stub de 5 líneas que solo remitía a la fuente. El archivo fuente en `sources/` no se tocó (SOLO LECTURA).

- Se movió la captura raw a `0-raw/archive/2026-10-26-decodo-smartproxy-home.md` para registrar su procesamiento.

- Los 3 nuevos átomos enlazan entre sí y a átomos existentes del vault (rebranding, site unblocker, targeting, trial de volumen), siguiendo el protocolo de **mínimo 2 wikilinks por átomo**.

- Cada átomo incluye una sección `## Nota de extensión 2026-10-27` que conecta el hallazgo con la refinación del mismo día (2026-10-27), documentando cómo la captura del home complementa y a veces corrige a los átomos existentes del vault.

## Proximos pasos

- Actualizar el thread `3-threads/thread-2026-10-26-decodo-smartproxy-home.md` con la síntesis completa (hecho).

- Verificar si los bloques `## [FRICTION]` en átomos existentes necesitan atención nueva derivada de estos hallazgos.

- Considerar si el patrón de "dos mecanismos de entrada gratuitos con riesgo opuesto" debe documentarse como una regla de catalogación para futuras capturas de proveedores de proxy/API.
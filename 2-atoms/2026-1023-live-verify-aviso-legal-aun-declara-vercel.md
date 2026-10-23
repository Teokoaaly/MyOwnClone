---
id: 2026-1023-live-verify-aviso-legal-aun-declara-vercel
type: atom
certainty: solid
sources: [0-raw/archive/2026-10-23-2026-10-22-myownclone-live-reverification.md]
links: ["[[2026-1022-live-verify-identidad-legal-y-diseno-reconstruidos]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]", "[[2026-1022-live-verify-alta-y-precios-ya-publicos]]"]
---

## Claim
El Aviso Legal publicado en `/legal` de [[myownclone]] **contradice el hosting real**: la sección "III. Hosting y prestadores de servicio" afirma que "El Sitio Web está alojado en **Vercel Inc.** (440 N Barranca Ave #4133, Covina, CA 91723)" y que la base de datos está "operada por **Neon Inc.**", mientras que la medición en vivo del 2026-10-22 demuestra que el sitio lo sirve **nginx 1.28.3 autoalojado** en `212.227.169.99` con certificado Let's Encrypt emitido el 2026-10-14. El documento se fecha el 11 de mayo de 2026, pero el texto de hosting sigue apuntando a la topología anterior. El resto del aviso sí está actualizado en su capa de identidad: entidad **Myownclone llc** (LLC de Wyoming), domicilio **30 N Gould St, Ste R, Sheridan, WY 82801**, representante legal **Jacinto Guzman II**, contactos `contacto@myownclone.com` y `privacy@myownclone.com`.

## Why It Matters
Es una inconsistencia legal viva, no una curiosidad de OSINT: el aviso legal declara un encargado de hosting que ya no aloja el sitio, y por tanto el texto de cumplimiento de la LSSI-CE (sección III) nombra un prestador de servicio que no es el real. Cualquier auditoría de GDPR, contractual o de cumplimiento que se apoye en el `/legal` público heredará el error. También matiza la conclusión "la capa legal ha sido reconstruida" de [[2026-1022-live-verify-identidad-legal-y-diseno-reconstruidos]]: la identidad se reconstruyó, el clausulado de infraestructura no se tocó.

## [FRICTION]
> [[2026-1022-live-verify-identidad-legal-y-diseno-reconstruidos]] afirma que "la capa legal y de marca de [[myownclone]] ha sido reconstruida" y describe el Aviso Legal como una página de diez secciones actualizada con entidad nueva (Myownclone llc, Jacinto Guzman II).
> Este átomo presiona esa creencia porque la sección de hosting de ese mismo documento sigue afirmando Vercel Inc. como prestador del sitio, lo que es incompatible con el nginx autoalojado verificado en [[2026-1022-live-verify-deployment-migrada-a-vps-nginx]].
> Ambas no pueden ser simultáneamente la descripción completa: la identidad legal se actualizó, la declaración de hosting no. La explicación más consistente es que el documento legal se editó a finales de mayo de 2026 (de ahí la fecha de "última actualización") y no se volvió a tocar tras la migración de octubre.
> Marcado para juicio humano, no auto-resuelto.

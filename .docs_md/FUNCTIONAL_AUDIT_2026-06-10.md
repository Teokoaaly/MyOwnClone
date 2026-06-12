# Functional Audit — 2026-06-10

> Objetivo: evaluar el producto como app usable, no solo como repositorio que compila.

---

## 1. Alcance de esta pasada

Se ha auditado:

- arranque local del frontend
- rutas publicas principales
- flujo de acceso visible
- comportamiento de redirects/i18n
- lectura funcional de pantallas clave del dashboard desde codigo

Limitacion importante:

- la validacion automatizada autenticada no pudo completarse con las credenciales antiguas que aparecen en `SESSION_LOG_2026-06-10.md`; esas credenciales ya no son fiables para la automatizacion.
- el usuario confirmo que **si puede entrar manualmente**, asi que el bloqueo no es del producto en si, sino de la automatizacion con credenciales desactualizadas.

---

## 2. Validado en runtime

### Publico

Validado con servidor local levantado en `http://127.0.0.1:3000`:

- `/` redirige correctamente a `/en`
- `/en` carga correctamente
- `/en/login` carga correctamente
- `/en/registro` carga correctamente
- `registro` ya no hereda el layout del dashboard
- `Sign in` ya muestra acceso con Google
- el bucle de redirects del proxy esta resuelto

### Build / calidad base

Validado:

- `npm run typecheck` OK
- `npm run build` OK
- `next dev` OK

---

## 3. Hallazgos funcionales confirmados

## F-001. Credenciales del log de sesion obsoletas

Severidad: **P1**

Hallazgo:

- las credenciales historicas del log (`admin@myownclone.com` / `admin123`) no sirven para la automatizacion actual
- el documento de sesion no debe tratarse como fuente de verdad operativa

Impacto:

- dificulta QA automatizada reproducible
- induce a error al intentar validar flujos autenticados

Accion:

- documentar credenciales locales de QA o crear fixture de acceso reproducible

---

## F-002. Billing es fragil ante fallo parcial de backend

Severidad: **P1**

Archivo:

- `src/app/(dashboard)/facturacion/page.tsx`

Hallazgo:

- la pagina falla completa si cualquiera de estas dos llamadas falla:
  - `/api/clone/plans`
  - `/api/clone/billing`

Codigo relevante:

- si una falla, se lanza `Could not load billing information`
- no hay degradacion parcial

Impacto:

- aunque solo falle portal/billing status, el usuario pierde toda la vista de planes

Accion:

- separar carga de `plans` y `billing`
- renderizar planes aunque falle billing status
- dar error localizado para la parte rota

---

## F-003. Onboarding no garantiza cierre robusto del flujo

Severidad: **P1**

Archivo:

- `src/app/(dashboard)/onboarding/page.tsx`

Hallazgos:

- tras crear clon hace `router.push("/resumen")`
- no confirma clon activo ni estado final del setup
- no hay verificacion posterior del recurso creado

Impacto:

- puede terminar en resumen sin estado consistente si la API crea parcialmente o si falta resolver clon activo

Accion:

- tras crear clon, refrescar estado de clones
- asegurar seleccion/activacion del clon creado
- solo despues redirigir

---

## F-004. Biblioteca nuevo contenido tiene manejo de error demasiado silencioso

Severidad: **P1**

Archivo:

- `src/app/(dashboard)/biblioteca/nuevo/page.tsx`

Hallazgos:

- si el `POST /api/clone/sources` falla, no se muestra mensaje especifico
- el `catch` queda silencioso
- solo se cambia `loading`

Impacto:

- el usuario puede enviar contenido y no entender si fallo, por que fallo o que hacer despues

Accion:

- mostrar error visible
- distinguir validacion, backend y timeout
- mostrar feedback por tipo de contenido

---

## F-005. AI interview sigue siendo placeholder visible

Severidad: **P2**

Archivo:

- `src/app/(dashboard)/biblioteca/nuevo/page.tsx`

Hallazgo:

- `tipo === "interview"` muestra literalmente `Coming soon`
- no existe flujo funcional real

Impacto:

- la app expone una capacidad no disponible en una ruta ya navegable

Accion:

- o esconder la opcion temporalmente
- o marcarla claramente como beta/no disponible desde el listado previo

---

## F-006. Inbox tiene acciones, pero feedback funcional minimo

Severidad: **P2**

Archivo:

- `src/app/(dashboard)/inbox/page.tsx`

Hallazgos:

- generar draft, guardar draft, enviar y descartar existen
- los errores son genericos
- no hay estados de exito claros
- se depende de `confirm()` nativo para algunas acciones

Impacto:

- flujo usable pero poco fiable para operacion real

Accion:

- añadir feedback de exito
- mejorar mensajes de error
- sustituir `confirm()` por modal de confirmacion consistente

---

## F-007. Copys y flujo de acceso siguen mezclando estados de producto

Severidad: **P2**

Hallazgo:

- ya se mejoro `Get started`, pero quedan decisiones de producto abiertas:
  - destino de `Watch demo`
  - copy entre login/registro/onboarding
  - landing con CTAs adaptadas pero sin recorrido demo real

Impacto:

- la app entra, pero no cuenta una historia de uso totalmente coherente

Accion:

- decidir un funnel unico:
  - visitante
  - usuario autenticado sin clon
  - usuario con clon
  - admin

---

## 4. Estado por area funcional

| Area | Estado | Nota |
|---|---|---|
| Landing | Verde | publica, usable |
| Login | Verde | incluye Google |
| Registro | Verde | ya no cuelga del dashboard |
| Redirects/i18n | Verde | sin loop |
| Onboarding | Amarillo | requiere cierre robusto |
| Resumen | Amarillo | base util, falta validar con datos reales |
| Biblioteca | Amarillo | flujos existen, errores flojos |
| Cerebro | Amarillo | requiere validar efecto real |
| Inbox | Amarillo | acciones existen, feedback flojo |
| Productos | Amarillo | requiere validar consumo real |
| Reuniones | Amarillo | requiere validar booking real |
| Facturacion | Amarillo/Rojo | fragil ante error parcial |
| Admin | Amarillo | requiere QA autenticada reproducible |

---

## 5. Plan inmediato recomendado

## Ola 1 — cerrar flujo principal

1. onboarding robusto
2. biblioteca con errores visibles
3. resumen coherente tras crear clon

## Ola 2 — cerrar operaciones del workspace

1. inbox
2. cerebro
3. productos
4. reuniones

## Ola 3 — cerrar negocio e integraciones

1. facturacion Stripe
2. admin secundario
3. booking publico

---

## 6. Tareas concretas siguientes

- [ ] Crear credenciales de QA reproducibles o fixture de sesion
- [ ] Endurecer `facturacion` con carga parcial tolerante a fallos
- [ ] Cerrar onboarding con activacion real del clon
- [ ] Añadir errores visibles en `biblioteca/nuevo`
- [ ] Ocultar o etiquetar claramente `AI interview`
- [ ] Mejorar feedback de `inbox`
- [ ] Definir destino real de `Watch demo`

---

## 7. Conclusión

La app ya no esta en fase "rota". Esta en fase **parcialmente conectada**.

El siguiente trabajo no es rehacer arquitectura, sino **cerrar interacciones**:

- asegurar que cada CTA importante termina una accion real
- degradar bien cuando una integracion falla
- quitar o marcar lo que aun es placeholder

Ese es el camino mas corto para convertir el proyecto en un producto demostrable y operable.

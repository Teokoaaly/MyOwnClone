# Master Functional Completion Plan

> Fecha: 2026-06-10  
> Estado base: acceso, routing, build y dev server funcionales  
> Objetivo: pasar de "app que arranca y deja entrar" a "producto usable end-to-end"

---

## 1. Resumen ejecutivo

La base tecnica principal ya esta encendida:

- login y registro funcionan
- i18n base con prefijo funciona
- proxy sin bucles de redirect
- build y typecheck pasan
- landing, login y registro ya no dependen visualmente del dashboard

El cuello de botella actual ya no es de infraestructura. Es de **completitud funcional**:

- hay pantallas parcialmente conectadas
- hay flujos que abren UI pero no terminan la accion
- varias integraciones existen a nivel de estructura, pero no estan cerradas end-to-end
- hay estados UX sin pulir para error, vacio, loading y confirmacion

La prioridad correcta ahora es una **fase de cierre funcional** en 4 bloques:

1. flujo principal usuario
2. workspace/dashboard
3. integraciones de negocio
4. endurecimiento y QA

---

## 2. Estado actual por superficie

### A. Acceso y entrada

Estado: **funcional**

- landing publica operativa
- login operativo
- Google presente en sign in y register
- registro fuera del dashboard
- CTA de landing adaptado segun sesion

Pendientes:

- validar Google end-to-end con credenciales reales
- decidir destino final tras login social y magic link
- unificar idioma/copy entre login, registro y onboarding

### B. Onboarding

Estado: **parcial**

- existe UI de onboarding
- crea clon via API
- ya se usa como siguiente paso para usuario autenticado

Pendientes:

- confirmar que siempre existe el clon activo tras creacion
- revisar redirects finales
- validar errores de creacion y reintento
- unificar onboarding `/onboarding` y legacy `/es/onboarding`

### C. Dashboard / resumen

Estado: **parcial**

- shell y navegacion existen
- varias cards y accesos ya funcionan
- carga overview, inbox y clones

Pendientes:

- revisar cards con copy demasiado "demo"
- asegurar que todos los CTA llevan a pantallas realmente usables
- confirmar comportamiento cuando no existe clon

### D. Biblioteca / fuentes

Estado: **parcial**

- listar fuentes funciona
- formulario nuevo existe
- alta de contenido existe para varios tipos

Pendientes:

- confirmar ingestion real por tipo (`pdf`, `web`, `youtube`, `text`)
- validar estados `processing`, `ready`, `error`
- revisar feedback visual tras subida
- confirmar trazabilidad hasta chunks/RAG

### E. Cerebro / memories / templates

Estado: **parcial**

- CRUD UI existe
- tabs y formularios existen

Pendientes:

- confirmar persistencia real en backend
- verificar uso real por el modelo en respuestas
- revisar diferencias entre memory, signature y template

### F. Inbox

Estado: **parcial**

- lista, detalle, draft y acciones existen

Pendientes:

- confirmar generacion real de draft
- confirmar guardar/enviar/descartar en backend
- validar clasificacion y estados

### G. Productos

Estado: **parcial**

- listado y alta existen

Pendientes:

- confirmar que el modo sales realmente consume productos
- validar prioridad, estado y render en conversaciones

### H. Reuniones / bookings

Estado: **parcial**

- UI de meeting types y availability existe
- schemas y naming ya estan mejor alineados

Pendientes:

- validar APIs reales de create/list/update
- comprobar flujo publico de booking
- revisar conflictos horarios y persistencia de reservas

### I. Facturacion / Stripe

Estado: **parcial**

- UI lista
- webhook ya no rompe build

Pendientes:

- validar checkout real
- validar portal de billing
- validar sincronizacion `tenant plan/status`

### J. Admin

Estado: **funcional / parcial**

- resumen, tenants y detail existen
- crear tenant existe

Pendientes:

- revisar feedback, audit, courtesy, impersonation end-to-end
- confirmar protecciones de rol y errores

---

## 3. Prioridades reales

### P0. Producto navegable sin sorpresas

Objetivo: que una persona pueda entrar, crear su espacio y no chocar con placeholders.

Tareas:

1. validar login credenciales, Google y magic link
2. validar landing -> registro -> onboarding -> resumen
3. validar redirects segun sesion y rol
4. eliminar o redirigir rutas legacy que dupliquen flujo

### P1. Workspace util de verdad

Objetivo: que el dashboard no solo se vea bien, sino que haga trabajo real.

Tareas:

1. cerrar biblioteca
2. cerrar inbox
3. cerrar memories/templates
4. cerrar productos
5. cerrar reuniones/bookings

### P2. Monetizacion e integraciones

Objetivo: que Stripe, email y booking dejen de ser superficie "parcial".

Tareas:

1. checkout Stripe
2. portal billing
3. webhook real
4. email generation/send
5. booking publico

### P3. Pulido y calidad

Objetivo: coherencia visual, copy, errores, loading y confianza.

Tareas:

1. unificar idiomas
2. revisar estados vacios
3. revisar errores y confirmaciones
4. revisar naming del dashboard
5. tests funcionales

---

## 4. Plan por fases

## Fase 1. Cierre del flujo de acceso

Meta:

- entrar sin friccion
- ver CTA coherentes
- llegar a onboarding o dashboard correcto

Tareas:

- verificar Google end-to-end
- verificar Resend/magic link
- revisar login admin vs login normal
- decidir si `Watch demo` va a dashboard, demo real o login
- limpiar rutas legacy de acceso

Salida esperada:

- acceso consistente y comprensible

## Fase 2. Cierre del flujo principal usuario

Meta:

- usuario crea clon
- sube contenido
- llega a resumen

Tareas:

- revisar onboarding completo
- garantizar clon activo tras creacion
- revisar `CloneIdResolver`
- revisar bibliotecas vacias vs primer contenido

Salida esperada:

- primer recorrido de producto completo

## Fase 3. Cierre del workspace

Meta:

- las secciones del sidebar hacen trabajo real

Tareas:

- biblioteca: ingestion y estados
- cerebro: persistencia y efecto real
- inbox: drafts y acciones
- productos: persistencia y consumo
- reuniones: CRUD + booking
- analiticas: datos reales y mensajes adecuados

Salida esperada:

- dashboard util, no solo navegable

## Fase 4. Integraciones de negocio

Meta:

- facturacion y operaciones externas cerradas

Tareas:

- checkout Stripe
- portal billing
- webhook real
- validacion de estados de tenant
- correo operativo
- bookings operativos

Salida esperada:

- monetizacion y automatizaciones listas para pruebas serias

## Fase 5. QA funcional y endurecimiento

Meta:

- reducir roturas y zonas ambiguas

Tareas:

- matriz de pruebas por pantalla
- smoke tests E2E del flujo principal
- estados error/loading/empty
- copy coherente
- limpieza de placeholders visibles

Salida esperada:

- producto defendible en demo interna

---

## 5. Backlog ejecutable

## Bloque A. Acceso

- [ ] Validar login credentials
- [ ] Validar login Google
- [ ] Validar login magic link
- [ ] Validar redirect usuario normal
- [ ] Validar redirect admin
- [ ] Decidir destino de `Watch demo`

## Bloque B. Onboarding

- [ ] Crear clon desde onboarding
- [ ] Confirmar clon activo
- [ ] Confirmar redirect a resumen
- [ ] Revisar errores y retry

## Bloque C. Biblioteca

- [ ] Subida texto
- [ ] Subida web
- [ ] Subida PDF
- [ ] Estado processing/ready/error
- [ ] Consumo posterior en RAG

## Bloque D. Cerebro

- [ ] Crear memory
- [ ] Editar memory
- [ ] Borrar memory
- [ ] Confirmar efecto real en respuestas

## Bloque E. Inbox

- [ ] Listar correos
- [ ] Abrir detalle
- [ ] Generar draft
- [ ] Guardar draft
- [ ] Enviar
- [ ] Descartar

## Bloque F. Productos

- [ ] Crear producto
- [ ] Ver persistencia
- [ ] Confirmar uso en modo sales

## Bloque G. Reuniones

- [ ] Crear meeting type
- [ ] Crear availability
- [ ] Validar booking publico
- [ ] Validar conflictos

## Bloque H. Facturacion

- [ ] Cargar planes
- [ ] Iniciar checkout
- [ ] Confirmar webhook
- [ ] Confirmar plan actualizado
- [ ] Abrir portal billing

## Bloque I. Admin

- [ ] Crear tenant
- [ ] Ver tenant detail
- [ ] Courtesy account
- [ ] Impersonation
- [ ] Audit log
- [ ] Feedback

---

## 6. Orden recomendado de ejecucion

### Semana 1

- acceso
- onboarding
- resumen
- registro / login / Google

### Semana 2

- biblioteca
- cerebro
- inbox

### Semana 3

- productos
- reuniones
- analiticas
- admin secundario

### Semana 4

- Stripe
- bookings reales
- QA funcional
- copy y pulido

---

## 7. Criterio de "producto usable"

Considerar esta fase cerrada cuando:

1. un usuario nuevo puede registrarse o entrar con Google
2. puede crear clon
3. puede subir contenido
4. puede volver al dashboard y ver estado coherente
5. inbox, memories y productos no parecen placeholders
6. facturacion no rompe el flujo
7. admin puede crear y revisar tenants
8. no hay redirects rotos ni pantallas colgadas del layout incorrecto

---

## 8. Siguiente accion recomendada

La siguiente accion de mayor valor es:

**hacer una auditoria funcional ejecutada pantalla por pantalla y convertir cada hallazgo en tareas cerrables**

Orden:

1. acceso
2. onboarding
3. resumen
4. biblioteca
5. cerebro
6. inbox
7. productos
8. reuniones
9. facturacion
10. admin

---

*Documento vivo. Actualizar al cerrar cada bloque funcional.*

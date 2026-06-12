# CONTRIBUTING.md

## Flujo de trabajo

1. Crear rama desde `main`.
2. Mantener cambios pequenos y revisables.
3. Anadir o actualizar tests junto al cambio.
4. Ejecutar checks locales antes de pedir review.
5. Documentar cambios de env, migraciones o contratos API.

## Convencion de commits

Usar Conventional Commits:

- `feat(scope): descripcion`
- `fix(scope): descripcion`
- `chore(scope): descripcion`
- `docs(scope): descripcion`
- `test(scope): descripcion`
- `refactor(scope): descripcion`

## Checks obligatorios

Frontend:

```powershell
cd MyOwnClone
npm run lint
npm run typecheck
npm run build
npm run test
```

Backend:

```powershell
pytest -q
```

Seguridad:

```powershell
cd MyOwnClone
npm audit --omit=dev
```

E2E cuando toque flujos de usuario:

```powershell
cd MyOwnClone
npm run test:e2e
```

## Migraciones

- No modificar schema sin migracion.
- Indicar si el cambio pertenece a Alembic o Drizzle.
- Probar migracion desde DB vacia y desde estado anterior.
- No usar `db:push` para produccion.

## Seguridad

- No commitear `.env`, claves, tokens ni dumps.
- No habilitar `dev-api-key-for-proxy` en staging/prod.
- Toda ruta admin debe validar rol.
- Toda ruta tenant debe validar ownership.
- Webhooks deben validar firma/secreto e idempotencia.

## Pull request

Cada PR debe incluir:

- Resumen del cambio.
- Riesgo y plan de rollback.
- Checks ejecutados.
- Screenshots si toca UI.
- Migraciones/env vars nuevas si aplica.

## Definition of Done

- Tests relevantes pasan.
- Build pasa.
- Sin vulnerabilidades nuevas.
- Sin warnings nuevos.
- Documentacion actualizada.
- Logs/errores son accionables.


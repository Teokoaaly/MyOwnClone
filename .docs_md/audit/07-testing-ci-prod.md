# Auditoria 100% - Testing, CI y Produccion (2026-06-11)

## Resumen

- **Estado:** Rojo hasta que Vitest vuelva a verde.
- **Riesgo principal:** los comandos por defecto no cubren todo el backend y los tests frontend fallan en el estado actual.
- **Veredicto:** no aceptar mas cambios de UI/backend sin una puerta minima: typecheck + vitest + pytest raiz + pytest api.

## Verificaciones

| Comando | Estado | Detalle |
|---|---|---|
| `npm run typecheck` | OK | Sin errores TS. |
| `npm test` | FAIL | 10 fallos en `ChatPanel`, 2 en `facturacion`. |
| `pytest -q` | OK | Ejecuta solo `tests/` por `pytest.ini`. |
| `pytest api\tests -q` | OK parcial | 14 passed, 12 skipped. |

## Fallos actuales

| ID | Prioridad | Fallo | Evidencia | Fix |
|---|---|---|---|---|
| T11-001 | P1 | `ChatPanel` asume `scrollTo` en jsdom. | `MyOwnClone/src/components/chat/ChatPanel.tsx:70` | Guard o mock global en setup. Mejor guard en componente. |
| T11-002 | P1 | Tests de billing esperan copy anterior. | `facturacion.test.tsx:123`, `:188` | Actualizar tests al contrato final o revertir copy si era accidental. |
| T11-003 | P1 | Pytest raiz no ejecuta `api/tests`. | `pytest.ini:2` | Incluir `api/tests` en `testpaths` o anadir comando CI dedicado. |
| T11-004 | P1 | Muchas pruebas backend criticas saltadas. | `pytest api\tests -q`: 12 skipped | Revisar fixtures DB/env para ejecutarlas en CI. |

## Gate recomendado

Antes de marcar cualquier tarea como terminada:

```powershell
cd MyOwnClone
npm run typecheck
npm test
cd ..
pytest -q
pytest api\tests -q
```

Para cambios visuales en dashboard/landing:

```powershell
cd MyOwnClone
npm run dev
```

y validar con Browser/Playwright la ruta afectada, al menos desktop y altura 900px.

## E2E minimo pendiente

1. Login -> resumen.
2. Crear clone -> queda seleccionado.
3. Subir fuente -> pasa por ingestion -> aparece ready/error real.
4. Preguntar al clone -> respuesta usa contexto.
5. Upgrade -> billing -> checkout session o error controlado.
6. Settings y API Keys son rutas separadas y coherentes.

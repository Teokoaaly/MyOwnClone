# 🌍 Master Plan: Internacionalización 50 Idiomas

> **Objetivo**: Traducir todo MyOwnClone a 50 idiomas con mantenimiento mínimo,
> integración automática por IA, y sin afectar el rendimiento.

---

## 📋 Tabla de Contenidos

1. [Estado Actual](#1-estado-actual)
2. [Arquitectura Propuesta](#2-arquitectura-propuesta)
3. [Pipeline de Traducción Automática](#3-pipeline-de-traducción-automática)
4. [Lista de 50 Idiomas](#4-lista-de-50-idiomas)
5. [Plan de Implementación por Fases](#5-plan-de-implementación-por-fases)
6. [Estructura de Archivos](#6-estructura-de-archivos)
7. [Sistema de Fallback](#7-sistema-de-fallback)
8. [UI Language Switcher](#8-ui-language-switcher)
9. [Rendimiento y Carga Diferida](#9-rendimiento-y-carga-diferida)
10. [CI/CD y Mantenimiento](#10-cicd-y-mantenimiento)
11. [Script de Auto-Traducción](#11-script-de-auto-traducción)
12. [Métricas y Calidad](#12-métricas-y-calidad)

---

## 1. Estado Actual

| Aspecto | Estado |
|---|---|
| Librería | `next-intl` v4.13.0 instalada |
| Idiomas | `en` y `es` |
| Archivos de traducción | `en.json` (2832 bytes), `es.json` (2973 bytes) |
| Cobertura | Solo meta, nav, auth, onboarding — parcial |
| Ruteo por locale | ❌ No implementado |
| next-intl plugin | ❌ No configurado en `next.config.ts` |
| Detección de idioma | ❌ Hardcoded `locale = "en"` en layout |
| next.config.ts | Sin plugin de next-intl |
| Locale routing | `routing.ts` define los locales pero no se usa |

### Diagnóstico

El sistema actual tiene next-intl instalado pero **no está conectado**. No hay ruteo
por idioma, no hay detección automática, y solo 2 archivos parciales.

---

## 2. Arquitectura Propuesta

```
┌─────────────────────────────────────────────────────────────┐
│                  🌐 Usuario                                  │
│  Accept-Language: fr / ?hl=es / cookie: locale=de          │
└─────────────────────────┬───────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────┐
│           next-intl Middleware (detección automática)        │
│                                                             │
│  1. Lee cookie (NEXT_LOCALE) → prioridad                    │
│  2. Lee query param (?hl=...)                                │
│  3. Lee Accept-Language header                              │
│  4. Fallback al defaultLocale (en)                          │
│  5. Redirige a /fr/dashboard o /es/dashboard               │
└─────────────────────────┬───────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────┐
│           App Router con segmento [locale]                  │
│                                                             │
│  /[locale]/resumen       /[locale]/biblioteca              │
│  /[locale]/admin/tenants /[locale]/login                   │
│  /[locale]/api/...       (API no necesita locale)          │
└─────────────────────────┬───────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────┐
│           next-intl Plugin (next.config.ts)                  │
│                                                             │
│  - Genera rutas localizadas automáticamente                 │
│  - Maneja la detección de locale en el middleware           │
│  - Proporciona useTranslations() hook                       │
│  - Carga diferida de mensajes por idioma                   │
└─────────────────────────────────────────────────────────────┘
```

### Flujo de petición

```
1. Usuario visita → myownclone.com
2. Middleware detecta idioma (cookie → header → default)
3. Redirige a → myownclone.com/en/dashboard
4. next-intl carga solo los mensajes de ese idioma
5. useTranslations() renderiza todo en el idioma detectado
6. El usuario puede cambiar desde un selector en la UI
7. Al cambiar, se escribe cookie y se recarga la página
```

### Diferencias clave vs estado actual

| Concepto | Ahora | Con el plan |
|---|---|---|
| Ruteo | Sin locale en URL | `/[locale]/...` |
| Middleware | Solo proxy API | Proxy + detección de idioma |
| Layout | Hardcoded `locale = "en"` | Dinámico desde params |
| Carga de mensajes | Manual en request.ts | Automática por next-intl |
| Traducciones | 2 archivos parciales | 50 archivos completos |
| Traducción automática | No | Script AI vía OpenAI/DeepL |

---

## 3. Pipeline de Traducción Automática

Para mantener 50 idiomas sin morir en el intento, la clave es un
**pipeline automático de traducción**:

```
 ┌──────────┐
 │  en.json │ ← Fuente de verdad (la edita el desarrollador)
 └─────┬────┘
       │
       ▼
 ┌──────────────────┐
 │  translate.js    │ ← Script Node.js que orquesta la traducción
 │  (npm run i18n)  │
 └──────────────────┘
       │
       ├────────────────┬────────────────┬────────────────┐
       ▼                ▼                ▼                ▼
 ┌──────────┐   ┌──────────┐    ┌──────────┐    ┌──────────┐
 │  es.json │   │  fr.json │    │  de.json │    │  ja.json │  ... (50)
 └──────────┘   └──────────┘    └──────────┘    └──────────┘
       │                │                │                │
       ▼                ▼                ▼                ▼
 ┌─────────────────────────────────────────────────────────┐
 │              Validación automática                       │
 │  - Verificar que todas las keys existen                 │
 │  - Detectar placeholders faltantes (%s, {name})         │
 │  - Reportar traducciones con baja confianza             │
 └─────────────────────────────────────────────────────────┘
```

### Estrategia de traducción

```
Opción recomendada: OpenAI (GPT-4o-mini) — más barato, traduce bien
                     y entiende contexto mejor que motores de traducción puros.

Alternativa: DeepL API — mejor para textos literales, peor con contexto.

Caso de uso: Traducción por lotes de archivos JSON completos.
             Cada key se traduce en su contexto (el value completo).
             Las keys se mantienen iguales en todos los idiomas.
```

### Configuración del script

```bash
# Comandos
npm run i18n:translate    # Traduce en.json a todos los idiomas
npm run i18n:translate fr # Traduce solo a francés
npm run i18n:check        # Verifica consistencia de keys
npm run i18n:missing      # Reporta keys faltantes por idioma
```

---

## 4. Lista de 50 Idiomas

| # | Código | Idioma | Prioridad |
|---|---|---|---|
| 1 | `en` | English (source) | 🌟 |
| 2 | `es` | Español | 🟢 |
| 3 | `fr` | Français | 🟢 |
| 4 | `de` | Deutsch | 🟢 |
| 5 | `pt` | Português | 🟢 |
| 6 | `it` | Italiano | 🟢 |
| 7 | `nl` | Nederlands | 🟢 |
| 8 | `pl` | Polski | 🟢 |
| 9 | `ru` | Русский | 🟢 |
| 10 | `ja` | 日本語 | 🟢 |
| 11 | `ko` | 한국어 | 🟢 |
| 12 | `zh-CN` | 简体中文 | 🟢 |
| 13 | `zh-TW` | 繁體中文 | 🟡 |
| 14 | `ar` | العربية | 🟡 |
| 15 | `tr` | Türkçe | 🟡 |
| 16 | `vi` | Tiếng Việt | 🟡 |
| 17 | `th` | ไทย | 🟡 |
| 18 | `sv` | Svenska | 🟡 |
| 19 | `da` | Dansk | 🟡 |
| 20 | `fi` | Suomi | 🟡 |
| 21 | `nb` | Norsk Bokmål | 🟡 |
| 22 | `cs` | Čeština | 🔵 |
| 23 | `hu` | Magyar | 🔵 |
| 24 | `ro` | Română | 🔵 |
| 25 | `uk` | Українська | 🔵 |
| 26 | `el` | Ελληνικά | 🔵 |
| 27 | `he` | עברית | 🔵 |
| 28 | `hi` | हिन्दी | 🔵 |
| 29 | `id` | Bahasa Indonesia | 🔵 |
| 30 | `ms` | Bahasa Melayu | 🔵 |
| 31 | `bn` | বাংলা | 🔵 |
| 32 | `ta` | தமிழ் | 🔵 |
| 33 | `te` | తెలుగు | 🔵 |
| 34 | `mr` | मराठी | 🔵 |
| 35 | `pa` | ਪੰਜਾਬੀ | 🔵 |
| 36 | `gu` | ગુજરાતી | 🔵 |
| 37 | `kn` | ಕನ್ನಡ | 🔵 |
| 38 | `ml` | മലയാളം | 🔵 |
| 39 | `si` | සිංහල | 🔵 |
| 40 | `km` | ភាសាខ្មែរ | 🔵 |
| 41 | `lo` | ລາວ | 🔵 |
| 42 | `my` | မြန်မာဘာသာ | 🔵 |
| 43 | `ne` | नेपाली | 🔵 |
| 44 | `am` | አማርኛ | 🔵 |
| 45 | `sw` | Kiswahili | 🔵 |
| 46 | `af` | Afrikaans | 🔵 |
| 47 | `ca` | Català | 🔵 |
| 48 | `gl` | Galego | 🔵 |
| 49 | `eu` | Euskara | 🔵 |
| 50 | `tl` | Filipino | 🔵 |

**Prioridades:**
- 🟢 **Fase 1** (10 idiomas) — Los más hablados + mercado objetivo
- 🟡 **Fase 2** (10 idiomas) — Segunda oleada
- 🔵 **Fase 3** (30 idiomas) — Cobertura global

---

## 5. Plan de Implementación por Fases

### Fase 0: Preparación (1-2 días)

- [ ] Configurar `next-intl/plugin` en `next.config.ts`
- [ ] Reestructurar layout para usar `NextIntlClientProvider`
- [ ] Configurar middleware de next-intl para detección de idioma
- [ ] Crear estructura `messages/{locale}.json`
- [ ] Mover traducciones existentes al nuevo formato
- [ ] Verificar que las rutas con `[locale]` funcionan

### Fase 1: Core funcional (3-5 días)

- [ ] Completar `en.json` con TODAS las claves del sitio
- [ ] Crear script `scripts/translate.js` con OpenAI
- [ ] Traducir primeros 10 idiomas
- [ ] Implementar `LanguageSwitcher` componente
- [ ] Integrar selector en sidebar y landing
- [ ] Probar ruteo completo con 3 idiomas

### Fase 2: Expansión (2-3 días)

- [ ] Traducir 10 idiomas más (Fase 2)
- [ ] Implementar lazy loading por idioma
- [ ] Añadir detección RTL para árabe/hebreo
- [ ] Probar todas las rutas en 5 idiomas
- [ ] Añadir flag icons al selector

### Fase 3: Escala global (3-5 días)

- [ ] Traducir 30 idiomas restantes
- [ ] Implementar `i18n:check` en CI
- [ ] Añadir métricas de cobertura
- [ ] Cache de traducciones en CDN
- [ ] Documentación final

---

## 6. Estructura de Archivos

### Antes
```
src/i18n/
├── en.json        ← parcial
├── es.json        ← parcial
├── request.ts     ← no conectado
└── routing.ts     ← define locales pero no se usa
```

### Después
```
src/i18n/
├── locales/                     ← Traducciones planas (una por idioma)
│   ├── en.json                  ← Fuente de verdad (completo)
│   ├── es.json                  ← Traducido automáticamente
│   ├── fr.json
│   ├── de.json
│   └── ... (50 archivos)
├── request.ts                   ← next-intl config (locale → messages)
├── routing.ts                   ← defineRouting con 50 locales
└── index.ts                     ← Re-exportaciones útiles

scripts/
└── translate.js                 ← Script de auto-traducción (Node.js)

src/components/ui/
└── LanguageSwitcher.tsx         ← Selector de idioma global
└── LanguageSwitcher.module.css
```

### Formato de mensajes

Usamos **formato plano por namespace** para mantenerlo simple y traducible:

```json
{
  "meta.title": "MyOwnClone - Multiply Yourself",
  "meta.description": "Create an AI clone trained with your content.",
  "nav.login": "Sign in",
  "nav.register": "Sign up",
  "nav.dashboard": "Dashboard",
  "nav.logout": "Sign out",
  "auth.loginTitle": "Sign in to MyOwnClone",
  "auth.emailLabel": "Email address",
  "auth.emailPlaceholder": "you@email.com",
  "auth.sendLink": "Send magic link",
  "onboarding.title": "Set up your MyOwnClone",
  "onboarding.slugLabel": "Choose your subdomain",
  "dashboard.resumen.title": "Command Center",
  "dashboard.resumen.subtitle": "Train your AI clone, manage its knowledge...",
  "dashboard.sidebar.overview": "Overview",
  "dashboard.sidebar.search": "Search",
  "dashboard.sidebar.crawl": "Crawl",
  "chat.inputPlaceholder": "Write your question...",
  "chat.thinking": "Thinking...",
  "chat.helpTitle": "How can I help?",
  "chat.helpSubtitle": "Ask anything about the creator's content",
  "admin.title": "Platform Admin",
  "admin.tenants.title": "Tenants",
  "admin.tenants.new": "+ New tenant",
  "common.loading": "Loading...",
  "common.error": "Something went wrong",
  "common.retry": "Try again",
  "common.save": "Save",
  "common.cancel": "Cancel",
  "common.delete": "Delete",
  "common.search": "Search...",
  "common.noResults": "No results found",
  "plan.trial": "Trial",
  "plan.basic": "Basic",
  "plan.pro": "Pro",
  "plan.scale": "Scale",
  "plan.enterprise": "Enterprise",
  "errors.notFound": "Page not found",
  "errors.unauthorized": "You don't have access to this page",
  "errors.backendUnavailable": "Backend unavailable"
}
```

> Las claves planas (separadas por `.`) son más fáciles de traducir automáticamente
> que los objetos anidados. El script de traducción procesa cada valor individual.

---

## 7. Sistema de Fallback

next-intl maneja el fallback automáticamente, pero hay que configurarlo
correctamente para 50 idiomas:

```ts
// src/i18n/request.ts
import { getRequestConfig } from "next-intl/server";

export default getRequestConfig(async ({ requestLocale }) => {
  const locale = await requestLocale;
  const baseLocale = locale.split("-")[0]; // zh-CN → zh

  try {
    return {
      locale,
      messages: (await import(`./locales/${locale}.json`)).default,
      // Si un key falta en fr.json, next-intl busca en en.json automáticamente
      timeZone: "UTC",
      now: new Date(),
    };
  } catch {
    // Fallback: si el archivo no existe, cargar inglés
    return {
      locale,
      messages: (await import(`./locales/en.json`)).default,
    };
  }
});
```

### Cadena de resolución

```
1. Busca key en el locale solicitado (ej: fr.json)
2. Si no existe → en.json (default locale)
3. Si no existe en en.json → devuelve el key name (visible para debug)
```

### Manejo de placeholders

```json
{
  "welcome.message": "Welcome back, {name}!",
  "inbox.unread": "You have {count} unread messages"
}
```

next-intl maneja `{name}` y `{count}` automáticamente con `t("welcome.message", { name: user.name })`.

---

## 8. UI Language Switcher

### Componente

```tsx
// src/components/ui/LanguageSwitcher.tsx
"use client";

import { usePathname, useRouter } from "@/i18n/routing";
import { useLocale } from "next-intl";
import { useTransition } from "react";

const LANGUAGES = [
  { code: "en", name: "English", flag: "🇬🇧" },
  { code: "es", name: "Español", flag: "🇪🇸" },
  { code: "fr", name: "Français", flag: "🇫🇷" },
  { code: "de", name: "Deutsch", flag: "🇩🇪" },
  { code: "pt", name: "Português", flag: "🇵🇹" },
  { code: "it", name: "Italiano", flag: "🇮🇹" },
  { code: "nl", name: "Nederlands", flag: "🇳🇱" },
  { code: "pl", name: "Polski", flag: "🇵🇱" },
  { code: "ru", name: "Русский", flag: "🇷🇺" },
  { code: "ja", name: "日本語", flag: "🇯🇵" },
  { code: "ko", name: "한국어", flag: "🇰🇷" },
  { code: "zh-CN", name: "简体中文", flag: "🇨🇳" },
  // ... resto de idiomas
];

export default function LanguageSwitcher() {
  const locale = useLocale();
  const router = useRouter();
  const pathname = usePathname();
  const [isPending, startTransition] = useTransition();

  const handleChange = (nextLocale: string) => {
    startTransition(() => {
      router.replace(pathname, { locale: nextLocale });
    });
  };

  return (
    <select
      value={locale}
      onChange={(e) => handleChange(e.target.value)}
      disabled={isPending}
      aria-label="Select language"
    >
      {LANGUAGES.map((lang) => (
        <option key={lang.code} value={lang.code}>
          {lang.flag} {lang.name}
        </option>
      ))}
    </select>
  );
}
```

### Integración en la UI

| Ubicación | Tipo | Visible en |
|---|---|---|
| Sidebar (abajo del usuario) | Select compacto | Dashboard, Admin |
| Landing page nav | Select con flags | Landing |
| Login/Register | Select pequeño | Auth pages |
| Footer global | Links de idioma | Todas |

### Persistencia

La selección se guarda en:
1. **Cookie** `NEXT_LOCALE` — el middleware la lee primero
2. **localStorage** — respaldo cuando no hay cookie
3. **Prefs de usuario** — en la tabla `users` para usuarios logueados

---

## 9. Rendimiento y Carga Diferida

Para que 50 idiomas no afecten el bundle:

```ts
// next.config.ts
import createNextIntlPlugin from "next-intl/plugin";

const withNextIntl = createNextIntlPlugin("./src/i18n/request.ts");

const nextConfig = {
  // ... resto de config
};

export default withNextIntl(nextConfig);
```

### Técnicas de optimización

| Técnica | Cómo |
|---|---|
| **Carga diferida** | `() => import(\`./locales/${locale}.json\`)` — solo carga el idioma activo |
| **Code splitting** | next-intl divide los mensajes por locale automáticamente |
| **Caché del mensaje** | Los archivos JSON se cachean por el navegador (Next.js static import) |
| **Precarga** | Precargar el idioma más probable (Accept-Language) |
| **CDN** | Los JSON de traducción pueden servirse desde CDN en producción |

### Impacto estimado

| Métrica | Valor |
|---|---|
| Tamaño por archivo | ~3-5 KB por idioma (gzip) |
| Total 50 idiomas | ~200 KB (solo 1 se carga) |
| Tiempo de carga extra | ~5-10 ms (carga de JSON local) |
| Impacto en bundle | 0 (lazy loaded) |

---

## 10. CI/CD y Mantenimiento

### GitHub Actions workflow

```yaml
# .github/workflows/i18n.yml
name: i18n Translation Check
on:
  pull_request:
    paths:
      - "src/i18n/locales/en.json"

jobs:
  translate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npm run i18n:check   # Verificar consistencia
      - run: npm run i18n:translate  # Auto-traducir idiomas faltantes
      - uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore(i18n): auto-translate after en.json update"
```

### Mantenimiento diario

| Acción | Frecuencia | Automático |
|---|---|---|
| Traducir nuevas claves | Cuando se añaden al código | ✅ Script |
| Verificar consistencia | Cada PR | ✅ CI |
| Actualizar 50 idiomas | Tras cambios en `en.json` | ✅ Script |
| Revisar traducciones manuales | Semanal | ❌ Humano |
| Añadir nuevo idioma | Bajo demanda | ✅ Script |

### Cómo añadir un nuevo idioma

```bash
npm run i18n:add sw     # Crea messages/sw.json auto-traducido
```

Esto:
1. Añade el locale a `routing.ts`
2. Genera `locales/sw.json`
3. Añade la bandera al `LanguageSwitcher`
4. Verifica que todas las keys existen

---

## 11. Script de Auto-Traducción

### Pseudocódigo del core

```js
// scripts/translate.js
import OpenAI from "openai";
import fs from "fs/promises";
import path from "path";

const LOCALES_DIR = "src/i18n/locales";
const SOURCE_LOCALE = "en";

const TARGET_LOCALES = [
  "es", "fr", "de", "pt", "it", "nl", "pl", "ru", "ja", "ko",
  "zh-CN", "zh-TW", "ar", "tr", "vi", "th", "sv", "da", "fi", "nb",
  "cs", "hu", "ro", "uk", "el", "he", "hi", "id", "ms",
  // ... resto hasta 50
];

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

async function translateLocale(sourceJson, targetLang, localeCode) {
  const entries = Object.entries(sourceJson);
  const batchSize = 30; // Traducir en lotes
  const result = {};

  for (let i = 0; i < entries.length; i += batchSize) {
    const batch = entries.slice(i, i + batchSize);
    
    const prompt = `Translate these UI strings to ${targetLang} (${localeCode}).
Keep all placeholders ({name}, {count}, %s, etc.) intact.
Respond with valid JSON only, no markdown.

Input:
${JSON.stringify(Object.fromEntries(batch), null, 2)}`;

    const response = await openai.chat.completions.create({
      model: "gpt-4o-mini",
      messages: [{ role: "user", content: prompt }],
      response_format: { type: "json_object" },
      temperature: 0.3,
    });

    const translated = JSON.parse(response.choices[0].message.content);
    Object.assign(result, translated);
  }

  return result;
}

// CLI: node scripts/translate.js [locale]
//   node scripts/translate.js         → todos los idiomas
//   node scripts/translate.js fr de   → solo francés y alemán
async function main() {
  const args = process.argv.slice(2);
  const locales = args.length > 0 ? args : TARGET_LOCALES;
  
  const sourcePath = path.join(LOCALES_DIR, `${SOURCE_LOCALE}.json`);
  const source = JSON.parse(await fs.readFile(sourcePath, "utf-8"));

  for (const locale of locales) {
    if (locale === SOURCE_LOCALE) continue;
    
    console.log(`⏳ Translating to ${locale}...`);
    const translated = await translateLocale(source, locale, locale);
    
    const targetPath = path.join(LOCALES_DIR, `${locale}.json`);
    await fs.writeFile(targetPath, JSON.stringify(translated, null, 2));
    console.log(`✅ ${locale} done (${Object.keys(translated).length} keys)`);
  }
}

main().catch(console.error);
```

### Package.json scripts

```json
{
  "scripts": {
    "i18n:translate": "node scripts/translate.js",
    "i18n:check": "node scripts/check-keys.js",
    "i18n:missing": "node scripts/missing-keys.js",
    "i18n:add": "node scripts/add-locale.js"
  }
}
```

### Script de verificación de keys

```js
// scripts/check-keys.js
// Verifica que todos los archivos tengan las mismas keys que en.json
const en = JSON.parse(fs.readFileSync("src/i18n/locales/en.json"));
const enKeys = Object.keys(en).sort();

let errors = 0;
for (const file of fs.readdirSync("src/i18n/locales")) {
  if (file === "en.json") continue;
  const translations = JSON.parse(fs.readFileSync(`src/i18n/locales/${file}`));
  const fileKeys = Object.keys(translations).sort();
  
  const missing = enKeys.filter(k => !fileKeys.includes(k));
  const extra = fileKeys.filter(k => !enKeys.includes(k));
  
  if (missing.length > 0) {
    console.error(`❌ ${file}: missing keys: ${missing.join(", ")}`);
    errors++;
  }
  if (extra.length > 0) {
    console.warn(`⚠️  ${file}: extra keys: ${extra.join(", ")}`);
  }
}
```

---

## 12. Métricas y Calidad

### Dashboard de cobertura

```bash
npm run i18n:check
```

Output:
```
📊 i18n Coverage Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
en  → ✅ 124/124 keys (source)
es  → ✅ 124/124 keys
fr  → ✅ 124/124 keys
de  → ⚠️  120/124 keys (4 missing)
ja  → ✅ 124/124 keys
ar  → ✅ 124/124 keys (RTL)
...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total: 50/50 locales — 96.8% coverage
```

### Control de calidad

| Check | Descripción | Fail if |
|---|---|---|
| **Key consistency** | Mismas keys que `en.json` | Cualquier key faltante |
| **Placeholder match** | `{name}` existe en todas las traducciones | Placeholder faltante |
| **Empty values** | Valores no vacíos | String vacío |
| **HTML tags** | Tags HTML preservados | Tag faltante/extra |
| **RTL detection** | `dir="rtl"` para ar, he, etc. | No configurado |

### Proceso de revisión humana

Para los primeros 10 idiomas (Fase 1), recomiendo revisión humana:
1. Script traduce automáticamente → genera PR
2. Revisor humano revisa las traducciones → corrige si es necesario
3. Se mergea a master

Para Fase 2 y 3, si la calidad del AI es buena (>95%), se puede automatizar completamente.

---

## Resumen de Carga de Trabajo

| Fase | Tarea | Días estimados | Dependencias |
|---|---|---|---|
| **F0** | Configurar next-intl plugin + middleware | 1 | — |
| **F0** | Reestructurar layout con [locale] | 0.5 | F0 |
| **F0** | Completar en.json con todas las keys | 1 | — |
| **F1** | Script de traducción automática | 1 | F0 |
| **F1** | Traducir 10 idiomas (auto) | 0.5 | F1 |
| **F1** | LanguageSwitcher componente | 0.5 | F0 |
| **F1** | Probar ruteo completo | 1 | F1 |
| **F2** | Traducir 10 idiomas más | 0.5 | F1 |
| **F2** | Soporte RTL | 0.5 | F0 |
| **F2** | CI/CD i18n workflow | 0.5 | F1 |
| **F3** | Traducir 30 idiomas restantes | 1 | F2 |
| **F3** | Cache + optimizaciones | 1 | F2 |
| **F3** | Documentación | 0.5 | — |
| **Total** | **~9 días** | | |

---

<p align="center">
  <strong>MyOwnClone</strong> — 50 idiomas, un solo mantenimiento.
  <br />
  <a href="../README.md">Volver al README</a>
</p>

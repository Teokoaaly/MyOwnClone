import { defineRouting } from "next-intl/routing";

export const routing = defineRouting({
  locales: ["es", "en"],
  defaultLocale: "en",
  localePrefix: "as-needed",
});

export function resolveLocale(locale: string | null | undefined) {
  return routing.locales.includes(locale as "es" | "en")
    ? (locale as (typeof routing.locales)[number])
    : routing.defaultLocale;
}

import { getRequestConfig } from "next-intl/server";

export default getRequestConfig(async ({ request }) => {
  const acceptLanguage = request.headers.get("accept-language") || "";

  // Parse Accept-Language header
  const languages = acceptLanguage
    .split(",")
    .map((lang) => {
      const [code, q] = lang.trim().split(";q=");
      return { code: code.split("-")[0].toLowerCase(), q: parseFloat(q) || 1 };
    })
    .sort((a, b) => b.q - a.q);

  const preferredLang = languages[0]?.code || "es";
  const locale = ["es", "en"].includes(preferredLang) ? preferredLang : "es";

  return {
    locale,
    messages: (await import(`../i18n/${locale}.json`)).default,
  };
});
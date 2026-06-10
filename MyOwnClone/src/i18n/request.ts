import { getRequestConfig } from "next-intl/server";
import { headers } from "next/headers";
import { resolveLocale } from "./routing";

export default getRequestConfig(async () => {
  const headerStore = await headers();
  const locale = resolveLocale(headerStore.get("x-locale"));

  return {
    locale,
    messages: (await import(`./${locale}.json`)).default,
  };
});

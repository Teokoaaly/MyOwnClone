import { getRequestConfig } from "next-intl/server";

export default getRequestConfig(async () => {
  // The app uses a hardcoded lang="es" in the root layout.
  // This i18n module is not wired up to any route.
  return {
    locale: "es",
    messages: (await import("./es.json")).default,
  };
});

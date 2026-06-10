import { getRequestConfig } from "next-intl/server";

export default getRequestConfig(async () => {
  // The app uses English as the default product language until the runtime
  // language switcher is wired into every user-facing route.
  // This i18n module is not wired up to any route.
  return {
    locale: "en",
    messages: (await import("./en.json")).default,
  };
});

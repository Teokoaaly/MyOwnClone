import { cookies } from "next/headers";
import { redirect } from "next/navigation";
import { routing, resolveLocale } from "@/i18n/routing";

export const dynamic = "force-dynamic";

/**
 * Legacy /registro alias kept for backwards compatibility with old
 * landing-page links. Reads the visitor's preferred locale from the
 * ``moc_locale`` cookie (set by the manual locale selector or the
 * backend's /api/me/locale endpoint) and redirects to the localized
 * signup page.
 */
export default async function RegistroRedirectPage() {
  const store = await cookies();
  const cookieLocale = store.get("moc_locale")?.value;
  const locale = resolveLocale(cookieLocale);
  const prefix = locale === routing.defaultLocale ? "" : `/${locale}`;
  redirect(`${prefix}/signup`);
}
import type { Session } from "next-auth";
import { isPlatformAdminSession } from "@/lib/platform-admin";

export function getPostAuthHref(session: Session | null | undefined) {
  if (isPlatformAdminSession(session)) {
    return "/admin/resumen";
  }

  return session?.user ? "/onboarding" : "/registro";
}

export function getSessionAwareNav(session: Session | null | undefined) {
  if (isPlatformAdminSession(session)) {
    return {
      signInHref: "/admin/resumen",
      signInLabel: "Admin",
      primaryHref: "/admin/resumen",
      primaryLabel: "Open admin",
    };
  }

  if (session?.user) {
    return {
      signInHref: "/resumen",
      signInLabel: "Dashboard",
      primaryHref: "/onboarding",
      primaryLabel: "Continue setup",
    };
  }

  return {
    signInHref: "/login",
    signInLabel: "Sign in",
    primaryHref: "/registro",
    primaryLabel: "Get started",
  };
}

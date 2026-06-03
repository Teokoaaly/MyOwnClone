"use server";

import { auth, signIn, signOut } from "@/lib/auth";

export async function devLogin(email: string) {
  "use server";

  // Directly sign in with credentials - bypasses CSRF issues with App Router
  const result = await signIn("credentials", {
    email,
    redirect: false,
  });

  return result;
}

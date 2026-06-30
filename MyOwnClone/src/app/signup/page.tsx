import { SignupForm } from "./signup-form";
import AnimatedLogoMark from "@/components/ui/AnimatedLogoMark";
import { LanguageSelector } from "@/components/ui/LanguageSelector";
import { auth } from "@/lib/auth";
import { getPostAuthHref } from "@/lib/session-routing";
import { redirect } from "next/navigation";

export const dynamic = "force-dynamic";

export default async function SignupPage() {
  const session = await auth();

  if (session?.user) {
    redirect(getPostAuthHref(session));
  }

  return (
    <main
      className="flex min-h-screen items-center justify-center px-4 py-12"
      style={{
        background: `
          radial-gradient(circle at 12% 8%, rgba(234, 88, 12, 0.18), transparent 36%),
          radial-gradient(circle at 88% 90%, rgba(219, 39, 119, 0.14), transparent 36%),
          var(--bg-page)
        `,
      }}
    >
      <div className="absolute right-4 top-4">
        <LanguageSelector variant="header" />
      </div>
      <div className="w-full max-w-md">
        <div
          className="mx-auto overflow-hidden rounded-[20px] border border-[var(--border-soft)] bg-[var(--bg-shell)]"
          style={{
            boxShadow:
              "0 1px 2px rgba(15, 23, 42, 0.04), 0 24px 64px rgba(15, 23, 42, 0.10)",
          }}
        >
          <div className="flex flex-col items-center px-8 pt-8 pb-2 text-center">
            <AnimatedLogoMark size={40} />
            <h1 className="mt-4 text-xl font-semibold text-[var(--text-primary)]">
              MyOwnClone
            </h1>
            <p className="mt-1 text-sm text-[var(--text-muted)]">
              Create your account and start scaling yourself
            </p>
          </div>
          <div className="px-8 pb-8 pt-4">
            <SignupForm />
          </div>
        </div>
      </div>
    </main>
  );
}
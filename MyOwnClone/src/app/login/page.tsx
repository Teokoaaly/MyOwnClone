import { LoginForm } from "./login-form";
import AnimatedLogoMark from "@/components/ui/AnimatedLogoMark";

export default function LoginPage() {
  return (
    <main className="auth-shell auth-shell-login flex min-h-screen items-center justify-center px-4 py-12">
      <div className="w-full max-w-md">
        <div
          className="mx-auto overflow-hidden rounded-[20px] border border-[var(--border-soft)] bg-[var(--bg-shell)]"
          style={{
            boxShadow:
              "0 1px 2px rgba(15, 23, 42, 0.04), 0 24px 64px rgba(15, 23, 42, 0.10)",
          }}
        >
          <div className="flex flex-col items-center px-8 pt-8 pb-2 text-center">
            <AnimatedLogoMark size={40} forceMotion />
            <h1 className="mt-4 text-xl font-semibold text-[var(--text-primary)]">
              MyOwnClone
            </h1>
            <p className="mt-1 text-sm text-[var(--text-muted)]">
              Sign in to manage your clone
            </p>
          </div>
          <div className="px-8 pb-8 pt-4">
            <LoginForm />
          </div>
        </div>
      </div>
    </main>
  );
}

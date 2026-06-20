import { LoginForm } from "./login-form";
import { Link } from "@/i18n/navigation";

export default function LoginPage() {
  return (
    <main className="flex min-h-[100dvh] items-center justify-center px-4 py-12 bg-stone-50">
      <div className="w-full max-w-md">
        {/* Header */}
        <div className="text-center mb-8">
          <Link href="/" className="inline-flex items-center gap-2 mb-6">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" aria-hidden="true">
              <rect x="2" y="2" width="9" height="9" rx="4" fill="#1c1917" />
              <rect x="13" y="2" width="9" height="9" rx="4" fill="#292524" />
              <rect x="2" y="13" width="9" height="9" rx="4" fill="#292524" />
              <rect x="13" y="13" width="9" height="9" rx="4" fill="#1c1917" />
            </svg>
            <span className="text-lg font-bold tracking-tight text-stone-900">MyOwnClone</span>
          </Link>
          <h1 className="text-2xl font-bold tracking-tight text-stone-900">
            Welcome back
          </h1>
          <p className="mt-1 text-sm text-stone-500">
            Sign in to manage your clone
          </p>
        </div>

        {/* Form card */}
        <div className="rounded-2xl border border-stone-200 bg-white p-6 shadow-sm">
          <LoginForm />
        </div>

        <p className="mt-6 text-center text-sm text-stone-500">
          Don&apos;t have an account?{" "}
          <Link
            href="/registro"
            className="font-semibold text-orange-600 hover:text-orange-700"
          >
            Create one
          </Link>
        </p>
      </div>
    </main>
  );
}

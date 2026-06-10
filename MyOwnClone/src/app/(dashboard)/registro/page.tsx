import { RegisterForm } from "./register-form";

export default function RegisterPage() {
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
      <div className="w-full max-w-md">
        <div
          className="mx-auto overflow-hidden rounded-[20px] border border-[var(--border-soft)] bg-[var(--bg-shell)]"
          style={{
            boxShadow:
              "0 1px 2px rgba(15, 23, 42, 0.04), 0 24px 64px rgba(15, 23, 42, 0.10)",
          }}
        >
          <div className="flex flex-col items-center px-8 pt-8 pb-2 text-center">
            <div
              aria-hidden="true"
              className="flex h-10 w-10 items-center justify-center rounded-xl text-sm font-bold"
              style={{ background: "var(--text-primary)", color: "var(--bg-shell)" }}
            >
              M
            </div>
            <h1 className="mt-4 text-xl font-semibold text-[var(--text-primary)]">
              MyOwnClone
            </h1>
            <p className="mt-1 text-sm text-[var(--text-muted)]">
              Create your account and start scaling yourself
            </p>
          </div>
          <div className="px-8 pb-8 pt-4">
            <RegisterForm />
          </div>
        </div>
      </div>
    </main>
  );
}

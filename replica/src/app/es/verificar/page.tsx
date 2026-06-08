import Link from "next/link";

interface Props {
  searchParams: Promise<{ email?: string }>;
}

export default async function VerificarPage({ searchParams }: Props) {
  const { email } = await searchParams;

  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-gray-50 dark:bg-gray-950 px-4">
      <div className="w-full max-w-md bg-white dark:bg-gray-900 rounded-2xl shadow-lg p-8 text-center">
        <div className="w-16 h-16 mx-auto mb-4 rounded-full bg-purple-100 dark:bg-purple-900 flex items-center justify-center">
          <svg className="w-8 h-8 text-purple-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
          </svg>
        </div>
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
          Revisa tu email
        </h1>
        <p className="mt-2 text-gray-500 dark:text-gray-400">
          Te hemos enviado un enlace mágico para acceder a tu cuenta.
        </p>
        {email && (
          <p className="mt-4 text-sm text-gray-600 dark:text-gray-300 bg-purple-50 dark:bg-purple-950 rounded-lg py-2 px-4">
            Enviado a: <strong>{email}</strong>
          </p>
        )}
        <p className="mt-4 text-xs text-gray-400">
          Si no ves el email, revisa la carpeta de spam o{" "}
          <Link href="/login" className="text-purple-600 hover:text-purple-500 underline">
            vuelve a intentarlo
          </Link>
          .
        </p>
        <Link
          href="/login"
          className="mt-6 inline-block px-6 py-3 bg-purple-600 text-white font-medium rounded-xl hover:bg-purple-700 transition-colors"
        >
          Volver al inicio
        </Link>
      </div>
    </div>
  );
}

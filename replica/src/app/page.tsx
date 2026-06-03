import Link from "next/link";

export default function LandingPage() {
  return (
    <div className="flex flex-col flex-1 items-center justify-center min-h-screen bg-gradient-to-br from-purple-50 via-white to-amber-50 dark:from-gray-900 dark:via-gray-900 dark:to-purple-950">
      <header className="w-full max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
        <span className="text-xl font-bold text-purple-600">Réplica</span>
        <div className="flex gap-4">
          <Link
            href="/login"
            className="px-4 py-2 text-sm font-medium text-gray-700 dark:text-gray-300 hover:text-purple-600 transition-colors"
          >
            Iniciar sesión
          </Link>
          <Link
            href="/registro"
            className="px-4 py-2 text-sm font-medium text-white bg-purple-600 rounded-lg hover:bg-purple-700 transition-colors"
          >
            Comenzar gratis
          </Link>
        </div>
      </header>

      <main className="flex-1 flex flex-col items-center justify-center text-center px-6 max-w-3xl mx-auto">
        <h1 className="text-5xl font-extrabold tracking-tight sm:text-6xl bg-gradient-to-r from-purple-600 to-amber-500 bg-clip-text text-transparent">
          Multiplícate
        </h1>
        <p className="mt-6 text-xl leading-relaxed text-gray-600 dark:text-gray-400 max-w-xl">
          Crea un clon de IA que atiende, vende y enseña por ti las 24 horas del día. Entrenado con tu propio contenido.
        </p>
        <div className="mt-10 flex flex-col sm:flex-row gap-4">
          <Link
            href="/registro"
            className="px-8 py-3 text-lg font-semibold text-white bg-purple-600 rounded-xl hover:bg-purple-700 transition-colors shadow-lg shadow-purple-500/25"
          >
            Crear mi Réplica gratis
          </Link>
          <Link
            href="/login"
            className="px-8 py-3 text-lg font-semibold text-purple-600 border-2 border-purple-200 dark:border-purple-800 rounded-xl hover:bg-purple-50 dark:hover:bg-purple-950 transition-colors"
          >
            Ya tengo cuenta
          </Link>
        </div>
        <p className="mt-4 text-sm text-gray-400">Prueba gratuita de 14 días. Sin tarjeta.</p>
      </main>

      <footer className="w-full max-w-6xl mx-auto px-6 py-8 text-center text-sm text-gray-400">
        Réplica — Clones de IA para infoproductores
      </footer>
    </div>
  );
}

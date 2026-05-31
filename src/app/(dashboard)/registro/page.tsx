import { RegisterForm } from "./register-form";

export default function RegisterPage() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-gray-50 dark:bg-gray-950 px-4">
      <div className="w-full max-w-md">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-purple-600">Réplica</h1>
          <p className="mt-2 text-gray-600 dark:text-gray-400">
            Crea tu cuenta y empieza a multiplicarte
          </p>
        </div>
        <RegisterForm />
      </div>
    </div>
  );
}

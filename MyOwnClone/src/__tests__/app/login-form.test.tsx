import { describe, it, expect, vi, beforeEach, afterAll, afterEach } from "vitest"
import { cleanup, fireEvent, render, screen, waitFor } from "@testing-library/react"
import { LoginForm } from "@/app/login/login-form"

const mockSignIn = vi.hoisted(() => vi.fn())
const mockGetSession = vi.hoisted(() => vi.fn())

vi.mock("next-auth/react", () => ({
  signIn: mockSignIn,
  getSession: mockGetSession,
}))

describe("LoginForm", () => {
  const originalLocation = window.location

  beforeEach(() => {
    vi.clearAllMocks()
    Object.defineProperty(window, "location", {
      configurable: true,
      value: { href: "" },
    })
  })

  afterEach(() => {
    cleanup()
  })

  afterAll(() => {
    Object.defineProperty(window, "location", {
      configurable: true,
      value: originalLocation,
    })
  })

  it("redirige admins al dashboard admin tras login correcto", async () => {
    mockSignIn.mockResolvedValue({ ok: true })
    mockGetSession.mockResolvedValue({ user: { role: "platform_admin" } })

    render(<LoginForm />)

    fireEvent.change(screen.getByLabelText(/correo electrónico/i), {
      target: { value: "admin@myownclone.com" },
    })
    fireEvent.change(screen.getByLabelText(/contraseña/i), {
      target: { value: "secret" },
    })
    fireEvent.submit(screen.getByRole("button", { name: /iniciar sesión/i }))

    await waitFor(() => {
      expect(mockSignIn).toHaveBeenCalledWith("credentials", {
        email: "admin@myownclone.com",
        password: "secret",
        redirect: false,
        callbackUrl: "/resumen",
      })
      expect(window.location.href).toBe("/admin/resumen")
    })
  })

  it("muestra error si next-auth devuelve error", async () => {
    mockSignIn.mockResolvedValue({ error: "CredentialsSignin" })

    render(<LoginForm />)

    fireEvent.change(screen.getByLabelText(/correo electrónico/i), {
      target: { value: "admin@myownclone.com" },
    })
    fireEvent.change(screen.getByLabelText(/contraseña/i), {
      target: { value: "bad" },
    })
    fireEvent.submit(screen.getByRole("button", { name: /iniciar sesión/i }))

    await waitFor(() => {
      expect(screen.getByRole("alert").textContent).toContain(
        "Email o contraseña incorrectos.",
      )
    })
  })
})

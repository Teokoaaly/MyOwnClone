import { describe, it, expect, vi, beforeEach, afterAll, afterEach } from "vitest"
import { cleanup, fireEvent, render, screen, waitFor } from "@testing-library/react"
import { LoginForm } from "@/app/login/login-form"

const mockSignIn = vi.hoisted(() => vi.fn())
const mockGetSession = vi.hoisted(() => vi.fn())
const mockReplace = vi.hoisted(() => vi.fn())

vi.mock("next-auth/react", () => ({
  signIn: mockSignIn,
  getSession: mockGetSession,
}))

vi.mock("@/i18n/navigation", () => ({
  Link: ({ children, ...props }: any) => <a {...props}>{children}</a>,
  useRouter: () => ({ replace: mockReplace, push: vi.fn(), back: vi.fn(), refresh: vi.fn() }),
}))

describe("LoginForm", () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  afterEach(() => {
    cleanup()
  })

  afterAll(() => {})

  it("redirects admins to admin dashboard after successful login", async () => {
    mockSignIn.mockResolvedValue({ ok: true })
    mockGetSession.mockResolvedValue({ user: { role: "platform_admin" } })

    render(<LoginForm />)

  ***REMOVED***reEvent.change(screen.getByLabelText(/email/i), {
      target: { value: "admin@myownclone.com" },
    })
  ***REMOVED***reEvent.change(screen.getByLabelText(/password/i), {
      target: { value: "secret" },
    })
  ***REMOVED***reEvent.submit(screen.getByRole("button", { name: /sign in/i }))

    await waitFor(() => {
      expect(mockSignIn).toHaveBeenCalledWith("credentials", {
        email: "admin@myownclone.com",
        password: "secret",
        redirect: false,
        callbackUrl: "/resumen",
      })
      expect(mockReplace).toHaveBeenCalledWith("/admin/resumen")
    })
  })

  it("shows error if next-auth returns error", async () => {
    mockSignIn.mockResolvedValue({ error: "CredentialsSignin" })

    render(<LoginForm />)

  ***REMOVED***reEvent.change(screen.getByLabelText(/email/i), {
      target: { value: "admin@myownclone.com" },
    })
  ***REMOVED***reEvent.change(screen.getByLabelText(/password/i), {
      target: { value: "bad" },
    })
  ***REMOVED***reEvent.submit(screen.getByRole("button", { name: /sign in/i }))

    await waitFor(() => {
      expect(screen.getByRole("alert").textContent).toContain(
        "Invalid email or password.",
      )
    })
  })
})

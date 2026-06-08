import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest'
import { render, screen, fireEvent, waitFor, cleanup } from '@testing-library/react'
import { RegisterForm } from '@/app/(dashboard)/registro/register-form'

// Mock next-auth/react — hoisted so vi.mock can reference it
const mockSignIn = vi.hoisted(() => vi.fn())
vi.mock('next-auth/react', () => ({ signIn: mockSignIn }))

// Mock next/navigation — hoisted
const mockPush = vi.hoisted(() => vi.fn())
vi.mock('next/navigation', () => ({ useRouter: () => ({ push: mockPush, back: vi.fn() }) }))

describe('RegisterForm', () => {
  beforeEach(() => {
    vi.clearAllMocks()
    document.body.innerHTML = ''
  })

  afterEach(() => {
    cleanup()
  })

  it('renders both labels', () => {
    render(<RegisterForm />)
    expect(screen.getByLabelText('Nombre completo')).toBeDefined()
    expect(screen.getByLabelText('Correo electrónico')).toBeDefined()
  })

  it('renders both inputs', () => {
    render(<RegisterForm />)
    expect(screen.getByPlaceholderText('Tu nombre')).toBeDefined()
    expect(screen.getByPlaceholderText('tu@email.com')).toBeDefined()
  })

  it('renders submit button with "Crear cuenta" text initially', () => {
    render(<RegisterForm />)
    const button = screen.getByRole('button', { name: 'Crear cuenta' })
    expect(button).toBeDefined()
    expect(button).not.toBeDisabled()
  })

  it('submit happy path → success state', async () => {
    mockSignIn.mockResolvedValueOnce({ error: null })
    render(<RegisterForm />)

  ***REMOVED***reEvent.change(screen.getByPlaceholderText('Tu nombre'), { target: { value: 'Test User' } })
  ***REMOVED***reEvent.change(screen.getByPlaceholderText('tu@email.com'), { target: { value: 'test@example.com' } })
  ***REMOVED***reEvent.click(screen.getByRole('button', { name: 'Crear cuenta' }))

    await waitFor(() => {
      expect(screen.getByText('Revisa tu correo')).toBeDefined()
    })
  })

  it('submit error state (signIn returns error)', async () => {
    mockSignIn.mockResolvedValueOnce({ error: 'some-error' })
    render(<RegisterForm />)

  ***REMOVED***reEvent.change(screen.getByPlaceholderText('Tu nombre'), { target: { value: 'Test User' } })
  ***REMOVED***reEvent.change(screen.getByPlaceholderText('tu@email.com'), { target: { value: 'test@example.com' } })
  ***REMOVED***reEvent.click(screen.getByRole('button', { name: 'Crear cuenta' }))

    await waitFor(() => {
      expect(screen.getByRole('alert')).toHaveTextContent('Error al enviar el enlace. Intenta de nuevo.')
    })
  })

  it('submit throws → catches and shows error', async () => {
    mockSignIn.mockRejectedValueOnce(new Error('network'))
    render(<RegisterForm />)

  ***REMOVED***reEvent.change(screen.getByPlaceholderText('Tu nombre'), { target: { value: 'Test User' } })
  ***REMOVED***reEvent.change(screen.getByPlaceholderText('tu@email.com'), { target: { value: 'test@example.com' } })
  ***REMOVED***reEvent.click(screen.getByRole('button', { name: 'Crear cuenta' }))

    await waitFor(() => {
      expect(screen.getByRole('alert')).toHaveTextContent('Error de conexión. Intenta de nuevo.')
    })
  })

  it('loading state disables submit button', () => {
    mockSignIn.mockImplementation(() => new Promise(() => {}))
    render(<RegisterForm />)

  ***REMOVED***reEvent.change(screen.getByPlaceholderText('Tu nombre'), { target: { value: 'Test User' } })
  ***REMOVED***reEvent.change(screen.getByPlaceholderText('tu@email.com'), { target: { value: 'test@example.com' } })
  ***REMOVED***reEvent.click(screen.getByRole('button', { name: 'Crear cuenta' }))

    const button = screen.getByRole('button', { name: 'Enviando...' })
    expect(button).toBeDisabled()
  })

  it('Google button calls signIn with google and callbackUrl /resumen', () => {
    render(<RegisterForm />)
  ***REMOVED***reEvent.click(screen.getByRole('button', { name: 'Continuar con Google' }))
    expect(mockSignIn).toHaveBeenCalledWith('google', { callbackUrl: '/resumen' })
  })

  it('Inicia sesión link routes to /login', () => {
    render(<RegisterForm />)
  ***REMOVED***reEvent.click(screen.getByRole('button', { name: 'Inicia sesión' }))
    expect(mockPush).toHaveBeenCalledWith('/login')
  })
})
import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest'
import { render, screen, fireEvent, waitFor, cleanup } from '@testing-library/react'
import { RegisterForm } from '@/app/registro/register-form'

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
    expect(screen.getByLabelText('Full name')).toBeDefined()
    expect(screen.getByLabelText('Email address')).toBeDefined()
  })

  it('renders both inputs', () => {
    render(<RegisterForm />)
    expect(screen.getByPlaceholderText('Your name')).toBeDefined()
    expect(screen.getByPlaceholderText('you@email.com')).toBeDefined()
  })

  it('renders submit button with "Create account" text initially', () => {
    render(<RegisterForm />)
    const button = screen.getByRole('button', { name: 'Create account' })
    expect(button).toBeDefined()
    expect(button).not.toBeDisabled()
  })

  it('submit happy path → success state', async () => {
    mockSignIn.mockResolvedValueOnce({ error: null })
    render(<RegisterForm />)

  ***REMOVED***reEvent.change(screen.getByPlaceholderText('Your name'), { target: { value: 'Test User' } })
  ***REMOVED***reEvent.change(screen.getByPlaceholderText('you@email.com'), { target: { value: 'test@example.com' } })
  ***REMOVED***reEvent.click(screen.getByRole('button', { name: 'Create account' }))

    await waitFor(() => {
      expect(screen.getByText('Check your email')).toBeDefined()
    })
  })

  it('submit error state (signIn returns error)', async () => {
    mockSignIn.mockResolvedValueOnce({ error: 'some-error' })
    render(<RegisterForm />)

  ***REMOVED***reEvent.change(screen.getByPlaceholderText('Your name'), { target: { value: 'Test User' } })
  ***REMOVED***reEvent.change(screen.getByPlaceholderText('you@email.com'), { target: { value: 'test@example.com' } })
  ***REMOVED***reEvent.click(screen.getByRole('button', { name: 'Create account' }))

    await waitFor(() => {
      expect(screen.getByRole('alert')).toHaveTextContent('Error sending the link. Try again.')
    })
  })

  it('submit throws → catches and shows error', async () => {
    mockSignIn.mockRejectedValueOnce(new Error('network'))
    render(<RegisterForm />)

  ***REMOVED***reEvent.change(screen.getByPlaceholderText('Your name'), { target: { value: 'Test User' } })
  ***REMOVED***reEvent.change(screen.getByPlaceholderText('you@email.com'), { target: { value: 'test@example.com' } })
  ***REMOVED***reEvent.click(screen.getByRole('button', { name: 'Create account' }))

    await waitFor(() => {
      expect(screen.getByRole('alert')).toHaveTextContent('Connection error. Try again.')
    })
  })

  it('loading state disables submit button', () => {
    mockSignIn.mockImplementation(() => new Promise(() => {}))
    render(<RegisterForm />)

  ***REMOVED***reEvent.change(screen.getByPlaceholderText('Your name'), { target: { value: 'Test User' } })
  ***REMOVED***reEvent.change(screen.getByPlaceholderText('you@email.com'), { target: { value: 'test@example.com' } })
  ***REMOVED***reEvent.click(screen.getByRole('button', { name: 'Create account' }))

    const button = screen.getByRole('button', { name: 'Sending...' })
    expect(button).toBeDisabled()
  })

  it('Google button calls signIn with google and callbackUrl /resumen', () => {
    render(<RegisterForm />)
  ***REMOVED***reEvent.click(screen.getByRole('button', { name: 'Continue with Google' }))
    expect(mockSignIn).toHaveBeenCalledWith('google', { callbackUrl: '/resumen' })
  })

  it('Sign in link routes to /login', () => {
    render(<RegisterForm />)
  ***REMOVED***reEvent.click(screen.getByRole('button', { name: 'Sign in' }))
    expect(mockPush).toHaveBeenCalledWith('/login')
  })
})

import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, fireEvent, waitFor } from '@testing-library/react'

vi.mock('next-auth/react', () => ({ useSession: vi.fn() }))
vi.mock('next/navigation', () => ({ useRouter: vi.fn() }))

import FacturacionPage from '@/app/(dashboard)/facturacion/page'
import { useSession } from 'next-auth/react'
import { useRouter } from 'next/navigation'

const mockUseSession = vi.mocked(useSession)
const mockUseRouter = vi.mocked(useRouter)
const mockFetch = vi.fn()
global.fetch = mockFetch as any

const fourPlans = [
  {
    id: 'plan-free',
    name: 'Free',
    price_cents: 0,
    price_display: 'Gratis',
    words_training_limit: 1000,
    responses_month_limit: 50,
    modes_active: 1,
    email_triage: false,
    booking: false,
    api_access: false,
    multi_clone: false,
    whitelabel: false,
  },
  {
    id: 'plan-basic',
    name: 'Básico',
    price_cents: 2900,
    price_display: '$29/mes',
    words_training_limit: 5000,
    responses_month_limit: 500,
    modes_active: 2,
    email_triage: false,
    booking: false,
    api_access: false,
    multi_clone: false,
    whitelabel: false,
  },
  {
    id: 'plan-pro',
    name: 'Pro',
    price_cents: 7900,
    price_display: '$79/mes',
    words_training_limit: 50000,
    responses_month_limit: 5000,
    modes_active: 5,
    email_triage: true,
    booking: true,
    api_access: true,
    multi_clone: false,
    whitelabel: false,
  },
  {
    id: 'plan-enterprise',
    name: 'Enterprise',
    price_cents: 19900,
    price_display: '$199/mes',
    words_training_limit: 500000,
    responses_month_limit: 50000,
    modes_active: 10,
    email_triage: true,
    booking: true,
    api_access: true,
    multi_clone: true,
    whitelabel: true,
  },
]

beforeEach(() => {
  vi.clearAllMocks()
  mockUseSession.mockReturnValue({ status: 'authenticated', data: { user: {} } } as any)
  mockUseRouter.mockReturnValue({ push: vi.fn(), back: vi.fn() } as any)
  mockFetch.mockReset()
})

// 1. renders header "Facturación" + "Plan actual: básico" default
describe('FacturacionPage', () => {
  it('renders header "Facturación" + "Plan actual: básico" default', async () => {
    mockFetch.mockResolvedValueOnce({
      ok: true,
      json: async () => fourPlans,
    } as any)
    mockFetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ has_stripe: false, plan: null, subscription_status: null, portal_url: null }),
    } as any)

    render(<FacturacionPage />)

    await waitFor(() => {
      expect(screen.getByText('Facturación')).toBeDefined()
    })
    expect(screen.getByText('Plan actual:')).toBeDefined()
    // Use exact match to avoid matching "Básico" plan card name
    const planSpan = screen.getByText('básico')
    expect(planSpan).toBeDefined()
    expect(planSpan.className).toContain('capitalize')
  })

  // 2. renders LoadingState initially
  it('renders LoadingState initially', async () => {
    mockFetch.mockImplementation(() => new Promise(() => {})) // never resolves

    render(<FacturacionPage />)

    expect(screen.getByText('Cargando planes…')).toBeDefined()
  })

  // 3. renders ErrorState when fetch fails
  it('renders ErrorState when fetch fails', async () => {
    // Both resolve but ok=false triggers the throw in load()
    mockFetch.mockResolvedValueOnce({
      ok: false,
      json: async () => ({}),
    } as any)
    mockFetch.mockResolvedValueOnce({
      ok: false,
      json: async () => ({}),
    } as any)

    render(<FacturacionPage />)

    await waitFor(() => {
      expect(screen.getByText('No se pudo cargar la información de facturación')).toBeDefined()
    })
  })

  // 4. renders 4 plan cards when fetch returns 4 plans
  it('renders 4 plan cards when fetch returns 4 plans', async () => {
    mockFetch.mockResolvedValueOnce({
      ok: true,
      json: async () => fourPlans,
    } as any)
    mockFetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ has_stripe: false, plan: null, subscription_status: null, portal_url: null }),
    } as any)

    render(<FacturacionPage />)

    await waitFor(() => {
      expect(screen.getByText('Free')).toBeDefined()
    })
    expect(screen.getByText('Básico')).toBeDefined()
    expect(screen.getByText('Pro')).toBeDefined()
    expect(screen.getByText('Enterprise')).toBeDefined()
  })

  // 5. current plan card has aria-current="true"
  it('current plan card has aria-current="true"', async () => {
    mockFetch.mockResolvedValueOnce({
      ok: true,
      json: async () => fourPlans,
    } as any)
    mockFetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ has_stripe: true, plan: 'pro', subscription_status: 'active', portal_url: null }),
    } as any)

    render(<FacturacionPage />)

    await waitFor(() => {
      expect(screen.getByText('Pro')).toBeDefined()
    })

    const proButtons = screen.getAllByRole('button', { name: 'Plan actual' })
    expect(proButtons.length).toBe(1)
    expect(proButtons[0].getAttribute('aria-current')).toBe('true')
  })

  // 6. Pro plan card shows "Recomendado" badge
  it('Pro plan card shows "Recomendado" badge', async () => {
    mockFetch.mockResolvedValueOnce({
      ok: true,
      json: async () => fourPlans,
    } as any)
    mockFetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ has_stripe: false, plan: null, subscription_status: null, portal_url: null }),
    } as any)

    render(<FacturacionPage />)

    await waitFor(() => {
      expect(screen.getByText('Pro')).toBeDefined()
    })

    const badge = screen.getByText('Recomendado')
    expect(badge).toBeDefined()
    expect(badge.className).toContain('badge-violet')
  })

  // 7. "Gestionar suscripción" link has sr-only "se abre en una pestaña nueva"
  it('"Gestionar suscripción" link has sr-only "se abre en una pestaña nueva"', async () => {
    mockFetch.mockResolvedValueOnce({
      ok: true,
      json: async () => fourPlans,
    } as any)
    mockFetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ has_stripe: true, plan: 'pro', subscription_status: 'active', portal_url: 'https://stripe.com/portal' }),
    } as any)

    render(<FacturacionPage />)

    await waitFor(() => {
      expect(screen.getByText('Gestionar suscripción')).toBeDefined()
    })

    const link = screen.getByRole('link', { name: /Gestionar suscripción/i })
    expect(link).toBeDefined()
    expect(link.getAttribute('href')).toBe('https://stripe.com/portal')

    const srOnly = screen.getByText('(se abre en una pestaña nueva)')
    expect(srOnly).toBeDefined()
    expect(srOnly.className).toContain('sr-only')
  })
})

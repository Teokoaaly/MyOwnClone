import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest'
import { render, screen, waitFor, cleanup } from '@testing-library/react'

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
    price_display: '$0/mes',
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
    name: 'Basic',
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

afterEach(() => {
  cleanup()
})

describe('FacturacionPage', () => {
  it('renders header "Billing" + "Current plan: basic" default', async () => {
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
      expect(screen.getByText('Billing')).toBeDefined()
    })
    expect(screen.getByText('Current plan:')).toBeDefined()
    const planSpan = screen.getByText('basic')
    expect(planSpan).toBeDefined()
    expect(planSpan.className).toContain('capitalize')
  })

  it('renders LoadingState initially', async () => {
    mockFetch.mockImplementation(() => new Promise(() => {}))

    render(<FacturacionPage />)

    expect(screen.getByText('Loading plans...')).toBeDefined()
  })

  it('renders ErrorState when fetch fails', async () => {
    mockFetch.mockResolvedValueOnce({ ok: false, json: async () => ({}) } as any)
    mockFetch.mockResolvedValueOnce({ ok: false, json: async () => ({}) } as any)

    render(<FacturacionPage />)

    await waitFor(() => {
      expect(screen.getByText('Could not load billing information')).toBeDefined()
    })
  })

  it('renders 4 plan cards when fetch returns 4 plans', async () => {
    mockFetch.mockResolvedValueOnce({ ok: true, json: async () => fourPlans } as any)
    mockFetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ has_stripe: false, plan: null, subscription_status: null, portal_url: null }),
    } as any)

    render(<FacturacionPage />)

    await waitFor(() => {
      expect(screen.getAllByText('Free').length).toBeGreaterThanOrEqual(1)
    })
    expect(screen.getAllByText('Basic').length).toBeGreaterThanOrEqual(1)
    expect(screen.getAllByText('Pro').length).toBeGreaterThanOrEqual(1)
    expect(screen.getAllByText('Enterprise').length).toBeGreaterThanOrEqual(1)
  })

  it('current plan card has aria-current="true"', async () => {
    mockFetch.mockResolvedValueOnce({ ok: true, json: async () => fourPlans } as any)
    mockFetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ has_stripe: true, plan: 'pro', subscription_status: 'active', portal_url: null }),
    } as any)

    render(<FacturacionPage />)

    await waitFor(() => {
      expect(screen.getAllByText('Pro').length).toBeGreaterThanOrEqual(1)
    })

    const proButtons = screen.getAllByRole('button', { name: 'Current plan' })
    expect(proButtons.length).toBe(1)
    expect(proButtons[0].getAttribute('aria-current')).toBe('true')
  })

  it('Pro plan card shows "Recommended" badge', async () => {
    mockFetch.mockResolvedValueOnce({ ok: true, json: async () => fourPlans } as any)
    mockFetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ has_stripe: false, plan: null, subscription_status: null, portal_url: null }),
    } as any)

    render(<FacturacionPage />)

    await waitFor(() => {
      expect(screen.getAllByText('Pro').length).toBeGreaterThanOrEqual(1)
    })

    const badge = screen.getByText('Recommended')
    expect(badge).toBeDefined()
    expect(badge.className).toContain('badge-violet')
  })

  it('"Manage subscription" link has sr-only "(opens in a new tab)"', async () => {
    mockFetch.mockResolvedValueOnce({ ok: true, json: async () => fourPlans } as any)
    mockFetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ has_stripe: true, plan: 'pro', subscription_status: 'active', portal_url: 'https://stripe.com/portal' }),
    } as any)

    render(<FacturacionPage />)

    await waitFor(() => {
      expect(screen.getByText('Manage subscription')).toBeDefined()
    })

    const link = screen.getByRole('link', { name: /Manage subscription/i })
    expect(link).toBeDefined()
    expect(link.getAttribute('href')).toBe('https://stripe.com/portal')

    const srOnly = screen.getByText('(opens in a new tab)')
    expect(srOnly).toBeDefined()
    expect(srOnly.className).toContain('sr-only')
  })
})

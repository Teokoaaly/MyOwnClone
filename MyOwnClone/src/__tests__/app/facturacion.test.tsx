import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest'
import { fireEvent, render, screen, waitFor, cleanup } from '@testing-library/react'

vi.mock('next-auth/react', () => ({ useSession: vi.fn() }))
vi.mock('@/i18n/navigation', () => ({ useRouter: vi.fn() }))

import FacturacionPage from '@/app/(dashboard)/facturacion/page'
import { useSession } from 'next-auth/react'
import { useRouter } from '@/i18n/navigation'

const mockUseSession = vi.mocked(useSession)
const mockUseRouter = vi.mocked(useRouter)
const mockFetch = vi.fn()
const push = vi.fn()

global.fetch = mockFetch as any

beforeEach(() => {
  vi.clearAllMocks()
  mockUseSession.mockReturnValue({ status: 'authenticated', data: { user: {} } } as any)
  mockUseRouter.mockReturnValue({ push, back: vi.fn() } as any)
  mockFetch.mockImplementation((url: string) => {
    if (url.includes('/api/clone/plans')) {
      return Promise.resolve({
        ok: true,
        json: async () => [
          { id: 'basic', name: 'Basic', price_cents: 0, stripe_price_id: null },
          { id: 'pro', name: 'Pro', price_cents: 6490, stripe_price_id: 'price_pro' },
        ],
      } as any)
    }
    return Promise.resolve({
      ok: true,
      json: async () => ({
        has_stripe: false,
        plan: null,
        subscription_status: null,
        portal_url: null,
        payment_history: [],
        voucher_records: [],
      }),
    } as any)
  })
})

afterEach(() => {
  cleanup()
})

describe('FacturacionPage', () => {
  it('renders the balance screen', async () => {
    render(<FacturacionPage />)

    await waitFor(() => {
      expect(screen.getByRole('heading', { name: 'Balance' })).toBeDefined()
    })

    expect(screen.getAllByText('$0.00').length).toBeGreaterThan(0)
    expect(screen.getAllByText('Select plan').length).toBeGreaterThan(0)
    expect(screen.getByRole('heading', { name: 'Choose your plan' })).toBeDefined()
    expect(screen.getByText('Payment History')).toBeDefined()
    expect(screen.getByText('No local payment records yet. Stripe invoices will appear through the billing portal when configured.')).toBeDefined()
  })

  it('renders loading skeleton while billing loads', () => {
    mockFetch.mockImplementation(() => new Promise(() => {}))

    render(<FacturacionPage />)

    expect(document.querySelector('.animate-pulse')).toBeTruthy()
  })

  it('opens voucher records tab', async () => {
    render(<FacturacionPage />)

    await waitFor(() => {
      expect(screen.getByText('Voucher Records')).toBeDefined()
    })

    fireEvent.click(screen.getByText('Voucher Records'))

    expect(screen.getByText('No voucher records yet.')).toBeDefined()
  })

  it('navigates to API keys from Get API Key', async () => {
    render(<FacturacionPage />)

    await waitFor(() => {
      expect(screen.getByText('Get API Key')).toBeDefined()
    })

    fireEvent.click(screen.getByText('Get API Key'))

    expect(push).toHaveBeenCalledWith('/configuracion')
  })

  it('shows Stripe portal action only when available', async () => {
    mockFetch.mockImplementation((url: string) => {
      if (url.includes('/api/clone/plans')) {
        return Promise.resolve({ ok: true, json: async () => [] } as any)
      }
      return Promise.resolve({
        ok: true,
        json: async () => ({
          has_stripe: true,
          plan: 'pro',
          subscription_status: 'active',
          portal_url: 'https://stripe.example/portal',
        }),
      } as any)
    })

    render(<FacturacionPage />)

    await waitFor(() => {
      expect(screen.getByText('View Stripe Portal')).toBeDefined()
    })
  })

  it('starts checkout for the selected plan', async () => {
    mockFetch.mockImplementation((url: string, init?: RequestInit) => {
      if (url.includes('/api/clone/plans')) {
        return Promise.resolve({
          ok: true,
          json: async () => [
            { id: 'pro', name: 'Pro', price_cents: 6490, stripe_price_id: 'price_pro' },
          ],
        } as any)
      }
      if (url.includes('/api/clone/stripe/checkout')) {
        expect(JSON.parse(String(init?.body))).toMatchObject({ plan_id: 'pro' })
        return Promise.resolve({ ok: true, json: async () => ({ url: 'https://stripe.example/checkout' }) } as any)
      }
      return Promise.resolve({
        ok: true,
        json: async () => ({
          has_stripe: false,
          plan: null,
          subscription_status: null,
          portal_url: null,
          payment_history: [],
          voucher_records: [],
        }),
      } as any)
    })
    vi.stubGlobal('location', { assign: vi.fn() })

    render(<FacturacionPage />)

    await waitFor(() => {
      expect(screen.getByRole('heading', { name: 'Choose your plan' })).toBeDefined()
    })

    fireEvent.click(screen.getAllByText('Select plan').at(-1)!)

    await waitFor(() => {
      expect(window.location.assign).toHaveBeenCalledWith('https://stripe.example/checkout')
    })
  })
})

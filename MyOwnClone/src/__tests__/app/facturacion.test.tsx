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
  mockFetch.mockResolvedValue({
    ok: true,
    json: async () => ({ has_stripe: false, plan: null, subscription_status: null, portal_url: null, payment_history: [], voucher_records: [] }),
  } as any)
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
    expect(screen.getByText('Recharge')).toBeDefined()
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
    mockFetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({
        has_stripe: true,
        plan: 'pro',
        subscription_status: 'active',
        portal_url: 'https://stripe.example/portal',
      }),
    } as any)

    render(<FacturacionPage />)

    await waitFor(() => {
      expect(screen.getByText('View Stripe Portal')).toBeDefined()
    })
  })
})

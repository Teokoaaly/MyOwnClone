import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest'
import { render, screen, fireEvent, cleanup } from '@testing-library/react'
import { useState } from 'react'

// Track the URL passed to useAdminFetch so we can assert filter changes
const mockUseAdminFetch = vi.fn()
vi.mock('@/components/admin/useAdminFetch', () => ({
  useAdminFetch: (...args: any[]) => mockUseAdminFetch(...args),
}))

import AdminAuditPage from '@/app/admin/audit/page'

function buildResponse(overrides: { data?: object; loading?: boolean; error?: string | null; reload?: () => void } = {}) {
  return {
    data: {
      items: [],
      pagination: { page: 1, limit: 20, total: 0, pages: 0 },
      ...overrides.data,
    },
    loading: false,
    error: null,
    reload: vi.fn(),
    ...overrides,
  }
}

describe('AdminAuditPage', () => {
  beforeEach(() => {
    vi.clearAllMocks()
    mockUseAdminFetch.mockReturnValue(buildResponse())
  })

  afterEach(() => {
    cleanup()
  })

  // 1. renders header: "Audit log" + "0 acciones registradas en la plataforma" subtitle (when data is empty)
  it('renders header with audit log title and total count', () => {
    render(<AdminAuditPage />)
    expect(screen.getByText('Audit log')).toBeTruthy()
    expect(screen.getByText('0 acciones registradas en la plataforma')).toBeTruthy()
  })

  // 2. renders LoadingState when loading=true
  it('renders LoadingState when loading is true', () => {
    mockUseAdminFetch.mockReturnValue({
      data: null,
      loading: true,
      error: null,
      reload: vi.fn(),
    })
    render(<AdminAuditPage />)
    expect(screen.getByText('Loading audit log...')).toBeTruthy()
  })

  // 3. renders ErrorState + Retry button when error
  it('renders ErrorState with message and retry button when error occurs', () => {
    mockUseAdminFetch.mockReturnValue({
      data: null,
      loading: false,
      error: 'Network error',
      reload: vi.fn(),
    })
    render(<AdminAuditPage />)
    expect(screen.getByText('Error cargando audit log')).toBeTruthy()
    expect(screen.getByText('Network error')).toBeTruthy()
    expect(screen.getByText('Reintentar')).toBeTruthy()
  })

  // 4. renders EmptyState when data has 0 items
  it('renders EmptyState when items array is empty', () => {
    mockUseAdminFetch.mockReturnValue({
      data: { items: [], pagination: { page: 1, limit: 20, total: 0, pages: 0 } },
      loading: false,
      error: null,
      reload: vi.fn(),
    })
    render(<AdminAuditPage />)
    expect(screen.getByText('No entries')).toBeTruthy()
  })

  // 5. renders table row with badge when data has items
  it('renders table row with action badge when data has items', () => {
    const mockItem = {
      id: '1',
      actor_id: '12345678-1234-1234-1234-123456789012',
      action: 'impersonation_started',
      target_type: 'user',
      target_id: '87654321-4321-4321-4321-210987654321',
      reason: 'Testing',
      metadata: null,
      ip_address: null,
      user_agent: null,
      created_at: '2024-01-01T12:00:00Z',
    }
    mockUseAdminFetch.mockReturnValue({
      data: { items: [mockItem], pagination: { page: 1, limit: 20, total: 1, pages: 1 } },
      loading: false,
      error: null,
      reload: vi.fn(),
    })
    render(<AdminAuditPage />)
    const badge = document.querySelector('.badge-warning')
    expect(badge).toBeTruthy()
    expect(badge?.textContent).toBe('impersonation_started')
  })

  // 6. renders filter bar with 3 Fields
  it('renders filter bar with all three field labels', () => {
    render(<AdminAuditPage />)
    expect(screen.getByText('Acción')).toBeTruthy()
    expect(screen.getByText('Actor ID')).toBeTruthy()
    expect(screen.getByText('Target ID')).toBeTruthy()
  })

  // 7. clicking Acción filter updates the URL in useAdminFetch
  it('updates URL when Acción filter is changed', () => {
    const reloadMock = vi.fn()
    mockUseAdminFetch.mockReturnValue({
      data: { items: [], pagination: { page: 1, limit: 20, total: 0, pages: 0 } },
      loading: false,
      error: null,
      reload: reloadMock,
    })
    render(<AdminAuditPage />)

    const select = screen.getByRole('combobox') as HTMLSelectElement
    fireEvent.change(select, { target: { value: 'tenant_updated' } })

    // Assert that useAdminFetch was called with a URL containing action=tenant_updated
    const calls = mockUseAdminFetch.mock.calls
    const lastCall = calls[calls.length - 1]
    expect(lastCall[0]).toContain('action=tenant_updated')
  })

  // 8. Pagination renders when pages > 1
  it('renders Pagination component when there are multiple pages', () => {
    const mockItem = {
      id: '1',
      actor_id: '12345678-1234-1234-1234-123456789012',
      action: 'impersonation_started',
      target_type: 'user',
      target_id: '87654321-4321-4321-4321-210987654321',
      reason: 'Testing',
      metadata: null,
      ip_address: null,
      user_agent: null,
      created_at: '2024-01-01T12:00:00Z',
    }
    mockUseAdminFetch.mockReturnValue({
      data: {
        items: Array(20).fill(mockItem),
        pagination: { page: 1, limit: 20, total: 100, pages: 5 },
      },
      loading: false,
      error: null,
      reload: vi.fn(),
    })
    render(<AdminAuditPage />)
    // Pagination renders prev/next buttons
    const prevButtons = document.querySelectorAll('button')
    const hasPrev = Array.from(prevButtons).some(b => b.textContent === 'Previous')
    const hasNext = Array.from(prevButtons).some(b => b.textContent === 'Next')
    expect(hasPrev || hasNext).toBeTruthy()
  })
})
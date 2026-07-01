import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest'
import { render, screen, fireEvent, waitFor, cleanup } from '@testing-library/react'
import { Suspense } from 'react'
import NuevoPage from '@/app/(dashboard)/biblioteca/nuevo/page'

const { useSession } = vi.hoisted(() => ({ useSession: vi.fn() }))
const { useRouter, useSearchParams } = vi.hoisted(() => ({
  useRouter: vi.fn(),
  useSearchParams: vi.fn(),
}))

vi.mock('next-auth/react', () => ({ useSession }))
vi.mock('next/navigation', () => ({ useSearchParams }))
vi.mock('@/i18n/navigation', () => ({ useRouter }))

function renderWithSuspense(searchParams: URLSearchParams = new URLSearchParams()) {
  useSearchParams.mockReturnValue(searchParams as any)
  return render(
    <Suspense fallback={<div>Loading...</div>}>
      <NuevoPage />
    </Suspense>
  )
}

describe('NuevoContentPage', () => {
  beforeEach(() => {
    vi.clearAllMocks()
    useSession.mockReturnValue({
      status: 'authenticated',
      data: { user: { name: 'Test', email: 'test@test.com' } },
    } as any)
    useRouter.mockReturnValue({ push: vi.fn(), back: vi.fn() } as any)
    global.fetch = vi.fn()
  })

  afterEach(() => {
    cleanup()
  })

  it('renders text type by default', async () => {
    renderWithSuspense()

    await waitFor(() => {
      expect(screen.getByText('Write text')).toBeDefined()
    })
    expect(screen.getByLabelText('Content')).toBeDefined()
  })

  it('renders pdf type', async () => {
    renderWithSuspense(new URLSearchParams('?tipo=pdf'))

    await waitFor(() => {
      expect(screen.getByText('Upload PDF')).toBeDefined()
    })
    expect(screen.getByLabelText('PDF file')).toBeDefined()
  })

  it('renders youtube type', async () => {
    renderWithSuspense(new URLSearchParams('?tipo=youtube'))

    await waitFor(() => {
      expect(screen.getByText('YouTube link')).toBeDefined()
    })
    const inputs = screen.getAllByLabelText('URL')
    expect(inputs.length).toBeGreaterThanOrEqual(1)
    expect(inputs[0].getAttribute('placeholder')).toBe('https://youtube.com/watch?v=...')
  })

  it('renders interview type', async () => {
    renderWithSuspense(new URLSearchParams('?tipo=interview'))

    await waitFor(() => {
      const status = screen.getByRole('status')
      expect(status).toBeDefined()
      expect(screen.getByText(/The AI interview is a conversation/)).toBeDefined()
    })
    const btn = screen.getByRole('button', { name: 'Coming soon' })
    expect(btn).toBeDisabled()
  })

  it('silo radiogroup has 3 buttons with correct labels', async () => {
    renderWithSuspense()

    await waitFor(() => {
      const groups = screen.getAllByRole('radiogroup', { name: 'Content silo' })
      expect(groups.length).toBeGreaterThanOrEqual(1)
      expect(screen.getByText('Teaching')).toBeDefined()
      expect(screen.getByText('Support')).toBeDefined()
      expect(screen.getByText('Sales')).toBeDefined()
    })
  })

  it('silo default is teach (Teaching)', async () => {
    renderWithSuspense()

    await waitFor(() => {
      const btns = screen.getAllByRole('radio', { name: 'Teaching' })
      expect(btns.length).toBeGreaterThanOrEqual(1)
      expect(btns[0].getAttribute('aria-checked')).toBe('true')
    })
  })

  it('clicking Support silo updates aria-checked', async () => {
    renderWithSuspense()

    await waitFor(() => {
      expect(screen.getAllByRole('radio', { name: 'Teaching' }).length).toBeGreaterThanOrEqual(1)
    })

    const supportBtns = screen.getAllByRole('radio', { name: 'Support' })
    fireEvent.click(supportBtns[0])

    await waitFor(() => {
      const teachBtn = screen.getAllByRole('radio', { name: 'Teaching' })[0]
      const supportBtn = screen.getAllByRole('radio', { name: 'Support' })[0]
      expect(teachBtn.getAttribute('aria-checked')).toBe('false')
      expect(supportBtn.getAttribute('aria-checked')).toBe('true')
    })
  })

  it('submit text type happy path', async () => {
    ;(global.fetch as any).mockResolvedValueOnce({ ok: true })

    renderWithSuspense()

    await waitFor(() => {
      expect(screen.getByLabelText('Content')).toBeDefined()
    })

    fireEvent.change(screen.getByLabelText('Content'), {
      target: { value: 'Este es mi contenido de prueba' },
    })
    const addBtns = screen.getAllByRole('button', { name: 'Add content' })
    fireEvent.click(addBtns[0])

    await waitFor(() => {
      expect(screen.getByText('Content added')).toBeDefined()
    })
  })

  it('submit loading state', async () => {
    let resolveFetch: (v: unknown) => void
    ;(global.fetch as any).mockImplementation(
      () =>
        new Promise((res) => {
          resolveFetch = res as any
        })
    )

    renderWithSuspense()

    await waitFor(() => {
      expect(screen.getByLabelText('Content')).toBeDefined()
    })

    fireEvent.change(screen.getByLabelText('Content'), {
      target: { value: 'Content' },
    })
    const addBtns = screen.getAllByRole('button', { name: 'Add content' })
    fireEvent.click(addBtns[0])

    await waitFor(() => {
      const btns = screen.getAllByRole('button', { name: 'Processing...' })
      expect(btns.length).toBeGreaterThanOrEqual(1)
      expect(btns[0]).toBeDisabled()
    })

    resolveFetch!({ ok: true })
  })

  it('back button uses history.back() if history.length > 1', async () => {
    Object.defineProperty(window, 'history', {
      value: { length: 3 },
      writable: true,
    })

    const mockBack = vi.fn()
    const mockPush = vi.fn()
    useRouter.mockReturnValue({ push: mockPush, back: mockBack } as any)
    renderWithSuspense()

    await waitFor(() => {
      expect(screen.getAllByRole('button', { name: /Back to library/i }).length).toBeGreaterThanOrEqual(1)
    })

    const backBtn = screen.getAllByRole('button', { name: /Back to library/i })[0]
    fireEvent.click(backBtn)

    await waitFor(() => {
      expect(mockBack).toHaveBeenCalled()
    })
  })

  it('back button uses push("/biblioteca") if history.length === 1', async () => {
    Object.defineProperty(window, 'history', {
      value: { length: 1 },
      writable: true,
    })

    const mockBack = vi.fn()
    const mockPush = vi.fn()
    useRouter.mockReturnValue({ push: mockPush, back: mockBack } as any)
    renderWithSuspense()

    await waitFor(() => {
      expect(screen.getAllByRole('button', { name: /Back to library/i }).length).toBeGreaterThanOrEqual(1)
    })

    const backBtn = screen.getAllByRole('button', { name: /Back to library/i })[0]
    fireEvent.click(backBtn)

    await waitFor(() => {
      expect(mockPush).toHaveBeenCalledWith('/biblioteca')
    })
  })
})

import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import { Suspense } from 'react'
import NuevoPage from '@/app/(dashboard)/biblioteca/nuevo/page'

const { useSession } = vi.hoisted(() => ({ useSession: vi.fn() }))
const { useRouter, useSearchParams } = vi.hoisted(() => ({
  useRouter: vi.fn(),
  useSearchParams: vi.fn(),
}))

vi.mock('next-auth/react', () => ({ useSession }))
vi.mock('next/navigation', () => ({ useRouter, useSearchParams }))

// Helper to render with Suspense (required for useSearchParams)
function renderWithSuspense(searchParams: URLSearchParams = new URLSearchParams()) {
  useSearchParams.mockReturnValue(searchParams as any)
  return render(
    <Suspense fallback={<div>Cargando…</div>}>
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

  it('renders text type by default', async () => {
    renderWithSuspense()

    await waitFor(() => {
      expect(screen.getByText('Escribir texto')).toBeDefined()
    })
    expect(screen.getByRole('textbox', { name: 'Contenido' })).toBeDefined()
  })

  it('renders pdf type', async () => {
    renderWithSuspense(new URLSearchParams('?tipo=pdf'))

    await waitFor(() => {
      expect(screen.getByText('Subir PDF')).toBeDefined()
    })
    expect(screen.getByLabelText('Archivo PDF')).toBeDefined()
  })

  it('renders youtube type', async () => {
    renderWithSuspense(new URLSearchParams('?tipo=youtube'))

    await waitFor(() => {
      expect(screen.getByText('Enlace de YouTube')).toBeDefined()
    })
    const input = screen.getByLabelText('URL')
    expect(input).toBeDefined()
    expect(input.getAttribute('placeholder')).toBe('https://youtube.com/watch?v=...')
  })

  it('renders interview type', async () => {
    renderWithSuspense(new URLSearchParams('?tipo=interview'))

    await waitFor(() => {
      const status = screen.getByRole('status')
      expect(status).toBeDefined()
      expect(screen.getByText('La entrevista AI es una conversación con tu clon donde él te hará preguntas para extraer tu conocimiento automáticamente.')).toBeDefined()
    })
    const btn = screen.getByRole('button', { name: 'Próximamente' })
    expect(btn).toBeDisabled()
  })

  it('silo radiogroup has 3 buttons with correct labels', async () => {
    renderWithSuspense()

    await waitFor(() => {
      const group = screen.getByRole('radiogroup', { name: 'Silo de contenido' })
      expect(group).toBeDefined()
      const buttons = group.querySelectorAll('button')
      expect(buttons.length).toBe(3)
      expect(screen.getByText('Pedagogía')).toBeDefined()
      expect(screen.getByText('Soporte')).toBeDefined()
      expect(screen.getByText('Ventas')).toBeDefined()
    })
  })

  it('silo default is teach (Pedagogía)', async () => {
    renderWithSuspense()

    await waitFor(() => {
      const btn = screen.getByRole('radio', { name: 'Pedagogía' })
      expect(btn.getAttribute('aria-checked')).toBe('true')
    })
  })

  it('clicking Soporte silo updates aria-checked', async () => {
    renderWithSuspense()

    await waitFor(() => {
      expect(screen.getByRole('radio', { name: 'Pedagogía' })).toBeDefined()
    })

  ***REMOVED***reEvent.click(screen.getByText('Soporte'))

    await waitFor(() => {
      const teachBtn = screen.getByRole('radio', { name: 'Pedagogía' })
      const supportBtn = screen.getByRole('radio', { name: 'Soporte' })
      expect(teachBtn.getAttribute('aria-checked')).toBe('false')
      expect(supportBtn.getAttribute('aria-checked')).toBe('true')
    })
  })

  it('submit text type happy path', async () => {
    ;(global.fetch as any).mockResolvedValueOnce({ ok: true })

    renderWithSuspense()

    await waitFor(() => {
      expect(screen.getByRole('textbox', { name: 'Contenido' })).toBeDefined()
    })

  ***REMOVED***reEvent.change(screen.getByRole('textbox', { name: 'Contenido' }), {
      target: { value: 'Este es mi contenido de prueba' },
    })
  ***REMOVED***reEvent.click(screen.getByRole('button', { name: 'Añadir contenido' }))

    await waitFor(() => {
      expect(screen.getByText('Contenido añadido')).toBeDefined()
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
      expect(screen.getByRole('textbox', { name: 'Contenido' })).toBeDefined()
    })

  ***REMOVED***reEvent.change(screen.getByRole('textbox', { name: 'Contenido' }), {
      target: { value: 'Contenido' },
    })
  ***REMOVED***reEvent.click(screen.getByRole('button', { name: 'Añadir contenido' }))

    // Button should be loading immediately
    await waitFor(() => {
      const btn = screen.getByRole('button', { name: 'Procesando...' })
      expect(btn).toBeDisabled()
    })

    // Resolve the fetch
    resolveFetch!({ ok: true })
  })

  it('back button uses history.back() if history.length > 1', async () => {
    Object.defineProperty(window, 'history', {
      value: { length: 3 },
      writable: true,
    })

    const mockBack = vi.fn()
    const mockPush = vi.fn()
    // Set up router mock BEFORE rendering (renderWithSuspense will re-call mockReturnValue but with same refs)
    useRouter.mockReturnValue({ push: mockPush, back: mockBack } as any)
    renderWithSuspense()

    await waitFor(() => {
      expect(screen.getByRole('button', { name: /Volver a la biblioteca/i })).toBeDefined()
    })

    const backBtn = screen.getByRole('button', { name: 'Volver a la biblioteca' })
  ***REMOVED***reEvent.click(backBtn)

    // The component's router.back() was called on the mock
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
      expect(screen.getByRole('button', { name: /Volver a la biblioteca/i })).toBeDefined()
    })

    const backBtn = screen.getByRole('button', { name: 'Volver a la biblioteca' })
  ***REMOVED***reEvent.click(backBtn)

    await waitFor(() => {
      expect(mockPush).toHaveBeenCalledWith('/biblioteca')
    })
  })
})
import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import { ChatPanel } from '@/components/chat/ChatPanel'

// Mock fetch for SSE streaming tests
const mockFetch = vi.fn()
global.fetch = mockFetch

// Mock crypto.randomUUID
vi.stubGlobal('crypto', {
  randomUUID: () => 'test-uuid-' + Math.random().toString(36).slice(2),
})

// Mock scrollIntoView
Element.prototype.scrollIntoView = vi.fn()

describe('ChatPanel', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('renders empty state with welcome message', () => {
    render(<ChatPanel slug="test-clone" initialSilo="teach" />)
    expect(screen.getByText('¿En qué puedo ayudarte?')).toBeDefined()
    expect(screen.getByText('Pregunta lo que quieras sobre el contenido del creador')).toBeDefined()
  })

  it('renders input textarea', () => {
    render(<ChatPanel slug="test-clone" initialSilo="teach" />)
    expect(screen.getByPlaceholderText('Escribe tu pregunta...')).toBeDefined()
  })

  it('renders send button', () => {
    render(<ChatPanel slug="test-clone" initialSilo="teach" />)
    const buttons = screen.getAllByRole('button')
    expect(buttons.length).toBeGreaterThanOrEqual(1)
  })

  it('renders SiloToggle with initial silo', () => {
    render(<ChatPanel slug="test-clone" initialSilo="sales" />)
    expect(screen.getByText('Ventas')).toBeDefined()
  })

  it('send button is disabled when input is empty', () => {
    render(<ChatPanel slug="test-clone" initialSilo="teach" />)
    const sendButton = screen.getByRole('button', { name: '' }) // SVG only button
    // Find button that contains the SVG send icon
    const buttons = screen.getAllByRole('button')
    const sendBtn = buttons[buttons.length - 1]
    expect(sendBtn).toBeDisabled()
  })

  it('clears input after sending', async () => {
    // Mock successful response with empty stream
    const mockReader = {
      read: vi.fn()
        .mockResolvedValueOnce({ done: false, value: new TextEncoder().encode('data: [DONE]\n\n') })
        .mockResolvedValueOnce({ done: true }),
    }
    mockFetch.mockResolvedValueOnce({
      ok: true,
      body: { getReader: () => mockReader },
    })

    render(<ChatPanel slug="test-clone" initialSilo="teach" />)
    const textarea = screen.getByPlaceholderText('Escribe tu pregunta...')
    fireEvent.change(textarea, { target: { value: 'Hola' } })
    
    const buttons = screen.getAllByRole('button')
    const sendBtn = buttons[buttons.length - 1]
    fireEvent.click(sendBtn)

    await waitFor(() => {
      expect((textarea as HTMLTextAreaElement).value).toBe('')
    })
  })

  it('shows error message on fetch failure', async () => {
    mockFetch.mockRejectedValueOnce(new Error('Network error'))

    render(<ChatPanel slug="test-clone" initialSilo="teach" />)
    const textarea = screen.getByPlaceholderText('Escribe tu pregunta...')
    fireEvent.change(textarea, { target: { value: 'Hola' } })
    
    const buttons = screen.getAllByRole('button')
    const sendBtn = buttons[buttons.length - 1]
    fireEvent.click(sendBtn)

    await waitFor(() => {
      expect(screen.getByText('Network error')).toBeDefined()
    })
  })
})

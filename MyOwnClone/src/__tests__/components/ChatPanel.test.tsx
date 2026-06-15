import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest'
import { render, screen, fireEvent, waitFor, cleanup } from '@testing-library/react'
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
    cleanup()
    vi.clearAllMocks()
  })

  afterEach(() => {
    cleanup()
  })

  it('renders empty state with welcome message', () => {
    render(<ChatPanel slug="test-clone" initialSilo="teach" />)
    expect(screen.getByText('How can I help?')).toBeDefined()
    expect(screen.getByText("Ask anything about the creator's content")).toBeDefined()
  })

  it('renders input textarea', () => {
    render(<ChatPanel slug="test-clone" initialSilo="teach" />)
    expect(screen.getByPlaceholderText('Write your question...')).toBeDefined()
  })

  it('renders send button', () => {
    render(<ChatPanel slug="test-clone" initialSilo="teach" />)
    const buttons = screen.getAllByRole('button')
    expect(buttons.length).toBeGreaterThanOrEqual(1)
  })

  it('renders SiloToggle with initial silo', () => {
    render(<ChatPanel slug="test-clone" initialSilo="sales" />)
    expect(screen.getByText('Sales')).toBeDefined()
  })

  it('send button is disabled when input is empty', () => {
    render(<ChatPanel slug="test-clone" initialSilo="teach" />)
    const sendButton = screen.getByRole('button', { name: 'Send message' })
    expect(sendButton).toBeDisabled()
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
    const textarea = screen.getByPlaceholderText('Write your question...')
    fireEvent.change(textarea, { target: { value: 'Hola' } })

    const sendBtn = screen.getByRole('button', { name: 'Send message' })
    fireEvent.click(sendBtn)

    await waitFor(() => {
      expect((textarea as HTMLTextAreaElement).value).toBe('')
    })
  })

  it('shows error message on fetch failure', async () => {
    mockFetch.mockRejectedValueOnce(new Error('Network error'))

    render(<ChatPanel slug="test-clone" initialSilo="teach" />)
    const textarea = screen.getByPlaceholderText('Write your question...')
    fireEvent.change(textarea, { target: { value: 'Hola' } })

    const sendBtn = screen.getByRole('button', { name: 'Send message' })
    fireEvent.click(sendBtn)

    await waitFor(() => {
      expect(screen.getByText('Network error')).toBeDefined()
    })
  })

  it('surfaces backend stream errors as UI errors', async () => {
    const mockReader = {
      read: vi.fn()
        .mockResolvedValueOnce({ done: false, value: new TextEncoder().encode('data: {"content":"Backend failed","error":true}\n\n') })
        .mockResolvedValueOnce({ done: false, value: new TextEncoder().encode('data: [DONE]\n\n') })
        .mockResolvedValueOnce({ done: true }),
    }
    mockFetch.mockResolvedValueOnce({
      ok: true,
      body: { getReader: () => mockReader },
    })

    render(<ChatPanel slug="test-clone" initialSilo="teach" />)
    const textarea = screen.getByPlaceholderText('Write your question...')
    fireEvent.change(textarea, { target: { value: 'Hola' } })
    fireEvent.click(screen.getByRole('button', { name: 'Send message' }))

    await waitFor(() => {
      expect(screen.getByText('Backend failed')).toBeDefined()
    })
  })

  it('auto-sends the initial query when provided', async () => {
    const mockReader = {
      read: vi.fn()
        .mockResolvedValueOnce({ done: false, value: new TextEncoder().encode('data: {"content":"Hola"}\n\n') })
        .mockResolvedValueOnce({ done: false, value: new TextEncoder().encode('data: {"done":true,"confidence":0.9,"sources":[]}\n\n') })
        .mockResolvedValueOnce({ done: false, value: new TextEncoder().encode('data: [DONE]\n\n') })
        .mockResolvedValueOnce({ done: true }),
    }
    mockFetch.mockResolvedValueOnce({
      ok: true,
      body: { getReader: () => mockReader },
    })

    render(<ChatPanel slug="test-clone" initialSilo="teach" initialQuery="Pregunta inicial" />)

    await waitFor(() => {
      expect(mockFetch).toHaveBeenCalledWith(
        '/api/public/clones/test-clone/chat',
        expect.objectContaining({
          method: 'POST',
        }),
      )
    })
  })

  it('does not render hidden think blocks in assistant replies', async () => {
    const mockReader = {
      read: vi.fn()
        .mockResolvedValueOnce({ done: false, value: new TextEncoder().encode('data: {"content":"<think>Internal reasoning</think>Hola visible"}\n\n') })
        .mockResolvedValueOnce({ done: false, value: new TextEncoder().encode('data: {"done":true,"confidence":0.9,"sources":[]}\n\n') })
        .mockResolvedValueOnce({ done: false, value: new TextEncoder().encode('data: [DONE]\n\n') })
        .mockResolvedValueOnce({ done: true }),
    }
    mockFetch.mockResolvedValueOnce({
      ok: true,
      body: { getReader: () => mockReader },
    })

    render(<ChatPanel slug="test-clone" initialSilo="teach" initialQuery="Pregunta inicial" />)

    await waitFor(() => {
      expect(screen.getByText('Hola visible')).toBeDefined()
    })

    expect(screen.queryByText(/Internal reasoning/i)).toBeNull()
  })
})

import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import { MessageBubble } from '@/components/chat/MessageBubble'

const userMessage = {
  id: '1',
  role: 'user' as const,
  content: 'Hola, ¿cómo estás?',
}

const assistantMessage = {
  id: '2',
  role: 'assistant' as const,
  content: '¡Hola! Estoy bien, gracias.',
  confidence: 0.85,
  sources: [{ content: 'Documento de referencia', score: 0.9 }],
}

describe('MessageBubble', () => {
  it('renders user message with right alignment', () => {
    render(<MessageBubble message={userMessage} />)
    const container = screen.getByText('Hola, ¿cómo estás?').closest('.flex')
    expect(container?.className).toContain('justify-end')
  })

  it('renders assistant message with left alignment', () => {
    render(<MessageBubble message={assistantMessage} />)
    const container = screen.getByText(/Estoy bien/).closest('.flex')
    expect(container?.className).toContain('justify-start')
  })

  it('shows confidence bar when confidence is provided', () => {
    render(<MessageBubble message={assistantMessage} />)
    expect(screen.getByText('85%')).toBeDefined()
  })

  it('shows sources when provided', () => {
    render(<MessageBubble message={assistantMessage} />)
    expect(screen.getByText('1 fuente')).toBeDefined()
  })

  it('does not show confidence bar for user messages', () => {
    const userWithConfidence = { ...userMessage, confidence: 0.5 }
    render(<MessageBubble message={userWithConfidence} />)
    expect(screen.queryByText('50%')).toBeNull()
  })

  it('does not show confidence bar when confidence is undefined', () => {
    const msg = { ...assistantMessage, confidence: undefined }
    render(<MessageBubble message={msg} />)
    expect(screen.queryByText(/85%/)).toBeNull()
  })

  it('does not show sources section when empty array', () => {
    const msg = { ...assistantMessage, sources: [] }
    render(<MessageBubble message={msg} />)
    expect(screen.queryByText('0 fuentes')).toBeNull()
  })

  it('shows streaming pulse animation when isStreaming is true', () => {
    render(<MessageBubble message={assistantMessage} isStreaming />)
    const bubble = screen.getByText(/Estoy bien/).closest('.animate-pulse')
    expect(bubble).toBeDefined()
  })
})

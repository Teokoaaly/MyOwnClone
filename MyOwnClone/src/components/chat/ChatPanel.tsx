'use client'

import { useState, useRef, useEffect, useCallback } from 'react'
import { MessageBubble } from './MessageBubble'
import { SiloToggle } from './SiloToggle'

interface ChatMessage {
  id: string
  role: 'user' | 'assistant'
  content: string
  confidence?: number
  sources?: Array<{ content: string; score: number }>
}

interface ChatPanelProps {
  slug: string
  initialSilo: string
  contextId?: string
}

export function ChatPanel({ slug, initialSilo, contextId }: ChatPanelProps) {
  const [messages, setMessages] = useState<ChatMessage[]>([])
  const [input, setInput] = useState('')
  const [silo, setSilo] = useState(initialSilo)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [streaming, setStreaming] = useState('')
  const bottomRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, streaming])

  const sendMessage = useCallback(async () => {
    const text = input.trim()
    if (!text || loading) return

    setInput('')
    setError(null)
    setLoading(true)

    const userMsg: ChatMessage = {
      id: crypto.randomUUID(),
      role: 'user',
      content: text,
    }
    setMessages((prev) => [...prev, userMsg])

    try {
      const res = await fetch(`/api/clone/${slug}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: text,
          silo,
          context_id: contextId || null,
          conversation_id: null,
        }),
      })

      if (!res.ok) throw new Error(`Error ${res.status}`)

      const reader = res.body?.getReader()
      if (!reader) throw new Error('No response stream')

      const decoder = new TextDecoder()
      let fullResponse = ''
      let finalConfidence: number | undefined
      let finalSources: Array<{ content: string; score: number }> | undefined

      while (true) {
        const { ***REMOVED***, value } = await reader.read()
        if (***REMOVED***) break
        const chunk = decoder.decode(value, { stream: true })
        const lines = chunk.split('\n')
        for (const line of lines) {
          if (line.startsWith('data: ')) {
            const data = line.slice(6)
            if (data === '[DONE]') continue
            try {
              const parsed = JSON.parse(data)
              if (parsed.***REMOVED***) {
              ***REMOVED***nalConfidence = parsed.confidence
              ***REMOVED***nalSources = parsed.sources
              } else {
                fullResponse += parsed.content || ''
                setStreaming(fullResponse)
              }
            } catch {
              fullResponse += data
              setStreaming(fullResponse)
            }
          }
        }
      }

      setMessages((prev) => [
        ...prev,
        {
          id: crypto.randomUUID(),
          role: 'assistant',
          content: fullResponse,
          confidence: finalConfidence,
          sources: finalSources,
        },
      ])
      setStreaming('')
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Error al enviar mensaje')
    } finally {
      setLoading(false)
    }
  }, [input, loading, slug, silo, contextId])

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      sendMessage()
    }
  }

  return (
    <div className="flex flex-1 flex-col overflow-hidden">
      {/* Silo toggle */}
      <div
        className="flex justify-center border-b py-2"
        style={{ borderColor: 'var(--border-soft)' }}
      >
        <SiloToggle active={silo} onChange={setSilo} />
      </div>

      {/* Messages */}
      <div
        role="region"
        aria-label="Mensajes del clon"
        tabIndex={0}
        className="flex-1 space-y-4 overflow-y-auto p-4 outline-none focus-visible:ring-2 focus-visible:ring-[var(--color-accent-violet)]"
      >
        {messages.length === 0 && !loading && (
          <div className="flex h-full items-center justify-center text-center">
            <div>
              <p className="text-2xl font-medium text-[var(--text-primary)]">
                ¿En qué puedo ayudarte?
              </p>
              <p className="mt-2 text-sm text-[var(--text-secondary)]">
                Pregunta lo que quieras sobre el contenido del creador
              </p>
            </div>
          </div>
        )}

        {messages.map((msg) => (
          <MessageBubble key={msg.id} message={msg} cloneId={slug} />
        ))}

        {streaming && (
          <MessageBubble
            message={{ id: 'streaming', role: 'assistant', content: streaming }}
            isStreaming
            cloneId={slug}
          />
        )}

        {loading && !streaming && (
          <div
            className="flex items-center gap-2 px-4 py-2"
            style={{ color: 'var(--text-muted)' }}
            role="status"
            aria-live="polite"
          >
            <span className="flex gap-1" aria-hidden="true">
              <span
                className="h-2 w-2 animate-bounce rounded-full [animation-delay:0ms]"
                style={{ background: 'var(--text-muted)' }}
              />
              <span
                className="h-2 w-2 animate-bounce rounded-full [animation-delay:150ms]"
                style={{ background: 'var(--text-muted)' }}
              />
              <span
                className="h-2 w-2 animate-bounce rounded-full [animation-delay:300ms]"
                style={{ background: 'var(--text-muted)' }}
              />
            </span>
            <span className="text-sm">Pensando...</span>
          </div>
        )}

        {error && (
          <div
            role="alert"
            className="rounded-lg border px-4 py-3 text-sm"
            style={{
              borderColor: 'var(--color-accent-pink)',
              background: 'var(--surface-2)',
              color: 'var(--text-primary)',
            }}
          >
            {error}
            <button
              type="button"
              aria-label="Cerrar mensaje de error"
              onClick={() => setError(null)}
              className="ml-3 hover:opacity-80"
              style={{ color: 'var(--text-muted)' }}
            >
              <span aria-hidden="true">✕</span>
            </button>
          </div>
        )}

        <div ref={bottomRef} />
      </div>

      {/* Input */}
      <div
        className="border-t p-4"
        style={{ borderColor: 'var(--border-soft)' }}
      >
        <div className="flex gap-3">
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Escribe tu pregunta..."
            rows={1}
            disabled={loading}
            aria-label="Escribe tu pregunta"
            className="flex-1 resize-none rounded-xl border px-4 py-3 text-sm outline-none transition placeholder:text-[var(--text-muted)] focus:ring-1 disabled:opacity-50"
            style={{
              borderColor: 'var(--border-medium)',
              background: 'var(--surface-2)',
              color: 'var(--text-primary)',
            }}
          />
          <button
            type="button"
            aria-label="Enviar mensaje"
            onClick={sendMessage}
            disabled={loading || !input.trim()}
            className="rounded-xl px-5 py-3 text-sm font-medium text-white transition disabled:cursor-not-allowed disabled:opacity-50"
            style={{ background: 'var(--color-accent-violet)' }}
            onMouseEnter={(e) => {
              if (!e.currentTarget.disabled) {
                e.currentTarget.style.background = 'var(--color-accent-pink)'
              }
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.background = 'var(--color-accent-violet)'
            }}
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
            ***REMOVED***ll="none"
              viewBox="0 0 24 24"
              strokeWidth={2}
              stroke="currentColor"
              className="h-5 w-5"
              aria-hidden="true"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M6 12 3.269 3.125A59.769 59.769 0 0 1 21.485 12 59.768 59.768 0 0 1 3.27 20.875L5.999 12Zm0 0h7.5"
              />
            </svg>
          </button>
        </div>
      </div>
    </div>
  )
}

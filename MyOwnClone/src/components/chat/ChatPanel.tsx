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
  initialQuery?: string
  mode?: 'default' | 'inline'
  className?: string
  emptyState?: {
    title: string
    description: string
  }
  onReset?: () => void
}

function sanitizeAssistantContent(content: string): string {
  if (!content) return ''

  let sanitized = content
  const openTagIndex = sanitized.indexOf('<think>')
  const closeTagIndex = sanitized.indexOf('</think>')

  if (openTagIndex !== -1) {
    if (closeTagIndex !== -1 && closeTagIndex > openTagIndex) {
      sanitized = `${sanitized.slice(0, openTagIndex)}${sanitized.slice(closeTagIndex + '</think>'.length)}`
    } else {
      sanitized = sanitized.slice(0, openTagIndex)
    }
  }

  return sanitized.replaceAll('</think>', '').trimStart()
}

export function ChatPanel({
  slug,
  initialSilo,
  contextId,
  initialQuery,
  mode = 'default',
  className,
  emptyState,
  onReset,
}: ChatPanelProps) {
  const [messages, setMessages] = useState<ChatMessage[]>([])
  const [input, setInput] = useState('')
  const [silo, setSilo] = useState(initialSilo)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [streaming, setStreaming] = useState('')
  const messagesRef = useRef<HTMLDivElement>(null)
  const bottomRef = useRef<HTMLDivElement>(null)
  const initialQuerySentRef = useRef(false)

  useEffect(() => {
    const container = messagesRef.current
    if (!container) return
    if (typeof container.scrollTo === 'function') {
      container.scrollTo({
        top: container.scrollHeight,
        behavior: 'smooth',
      })
      return
    }
    container.scrollTop = container.scrollHeight
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
      let pending = ''
      let finalConfidence: number | undefined
      let finalSources: Array<{ content: string; score: number }> | undefined

      while (true) {
        const { ***REMOVED***, value } = await reader.read()
        if (***REMOVED***) break
        pending += decoder.decode(value, { stream: true })
        const lines = pending.split('\n')
        pending = lines.pop() ?? ''
        for (const line of lines) {
          if (line.startsWith('data: ')) {
            const data = line.slice(6)
            if (data === '[DONE]') continue
            try {
              const parsed = JSON.parse(data) as {
                content?: string
                ***REMOVED***?: boolean
                error?: boolean
                confidence?: number
                sources?: Array<{ content: string; score: number }>
              }
              if (parsed.error) {
                throw new Error(parsed.content || 'Error sending message')
              }
              if (parsed.***REMOVED***) {
              ***REMOVED***nalConfidence = parsed.confidence
              ***REMOVED***nalSources = parsed.sources
              } else {
                fullResponse += parsed.content || ''
                setStreaming(sanitizeAssistantContent(fullResponse))
              }
            } catch (parseError) {
              if (!(parseError instanceof SyntaxError)) {
                throw parseError
              }
              fullResponse += data
              setStreaming(sanitizeAssistantContent(fullResponse))
            }
          }
        }
      }

      const assistantContent = sanitizeAssistantContent(fullResponse)
      setMessages((prev) => [
        ...prev,
        {
          id: crypto.randomUUID(),
          role: 'assistant',
          content: assistantContent,
          confidence: finalConfidence,
          sources: finalSources,
        },
      ])
      setStreaming('')
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Error sending message')
    } finally {
      setLoading(false)
    }
  }, [input, loading, slug, silo, contextId])

  useEffect(() => {
    const query = initialQuery?.trim()
    if (!query || initialQuerySentRef.current || loading) return

    initialQuerySentRef.current = true
    setInput(query)
  }, [initialQuery, loading])

  useEffect(() => {
    if (!input.trim() || !initialQuerySentRef.current || loading || messages.length > 0) {
      return
    }

    sendMessage()
  }, [input, loading, messages.length, sendMessage])

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      sendMessage()
    }
  }

  const isInline = mode === 'inline'
  const hasMessages = messages.length > 0 || !!streaming
  const showInlineComposer = !hasMessages
  const shellClassName = className ? ` ${className}` : ''

  return (
    <div className={`flex h-full min-h-0 flex-1 flex-col overflow-hidden${shellClassName}`}>
      <div
        className={`shrink-0 border-b ${isInline ? 'px-4 py-3 md:px-5' : 'py-2'}`}
        style={{ borderColor: 'var(--border-soft)' }}
      >
        <div className={`flex ${isInline ? 'items-center justify-between gap-3' : 'justify-center'}`}>
          <SiloToggle active={silo} onChange={setSilo} />
          {isInline && onReset ? (
            <button
              type="button"
              onClick={onReset}
              className="shrink-0 rounded-full border border-[var(--border-medium)] px-3 py-1.5 text-xs text-[var(--text-muted)] transition hover:text-[var(--text-primary)]"
            >
              Nueva consulta
            </button>
          ) : null}
        </div>
      </div>

      <div
        role="region"
        aria-label="Clone messages"
        tabIndex={0}
        ref={messagesRef}
        className={`min-h-0 flex-1 overflow-y-auto outline-none focus-visible:ring-2 focus-visible:ring-[var(--color-accent-violet)] ${isInline ? 'px-4 py-4 md:px-5' : 'p-4'}`}
      >
        {!hasMessages && !loading && (
          <div className={`flex h-full ${isInline ? 'items-start justify-start text-left pt-5' : 'items-center justify-center text-center'}`}>
            <div>
              <p className={`${isInline ? 'text-lg' : 'text-2xl'} font-medium text-[var(--text-primary)]`}>
                {emptyState?.title ?? 'How can I help?'}
              </p>
              <p className="mt-2 text-sm text-[var(--text-secondary)]">
                {emptyState?.description ?? "Ask anything about the creator's content"}
              </p>
            </div>
          </div>
        )}

        <div className="space-y-4">
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
              <span className="text-sm">Thinking...</span>
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
                aria-label="Close error message"
                onClick={() => setError(null)}
                className="ml-3 hover:opacity-80"
                style={{ color: 'var(--text-muted)' }}
              >
                <span aria-hidden="true">✕</span>
              </button>
            </div>
          )}
        </div>

        <div ref={bottomRef} />
      </div>

      <div
        className={`shrink-0 border-t ${isInline ? 'px-4 py-3 md:px-5' : 'p-4'}`}
        style={{ borderColor: 'var(--border-soft)' }}
      >
        <div className={`flex gap-3 ${showInlineComposer ? 'items-end' : 'items-center'}`}>
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder={isInline ? 'Escribe tu pregunta aqui...' : 'Write your question...'}
            rows={showInlineComposer ? 3 : 1}
            disabled={loading}
            aria-label="Write your question"
            className={`flex-1 resize-none rounded-xl border px-4 py-3 text-sm outline-none transition placeholder:text-[var(--text-muted)] focus:ring-1 disabled:opacity-50 ${showInlineComposer ? 'min-h-[88px]' : 'min-h-[48px]'}`}
            style={{
              borderColor: 'var(--border-medium)',
              background: isInline && showInlineComposer ? 'transparent' : 'var(--surface-2)',
              color: 'var(--text-primary)',
            }}
          />
          <button
            type="button"
            aria-label="Send message"
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

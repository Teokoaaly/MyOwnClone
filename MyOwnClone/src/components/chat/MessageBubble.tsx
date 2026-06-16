'use client'

import { useMemo, useState } from 'react'
import DOMPurify from 'dompurify'

interface ChatMessage {
  id: string
  role: 'user' | 'assistant'
  content: string
  confidence?: number
  sources?: Array<{ content: string; score: number }>
}

interface MessageBubbleProps {
  message: ChatMessage
  isStreaming?: boolean
  cloneId?: string
}

export function MessageBubble({ message, isStreaming, cloneId }: MessageBubbleProps) {
  const isUser = message.role === 'user'
  const [feedback, setFeedback] = useState<'up' | 'down' | null>(null)
  const [submitting, setSubmitting] = useState(false)

  const handleFeedback = async (rating: 'up' | 'down') => {
    if (submitting || feedback) return
    setSubmitting(true)
    try {
      const res = await fetch('/api/clone/feedback', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          clone_id: cloneId || '',
          message_id: message.id,
          rating,
        }),
      })
      if (res.ok) {
        setFeedback(rating)
      }
    } catch {
    } finally {
      setSubmitting(false)
    }
  }

  const formattedContent = useMemo(() => {
    if (isUser) return message.content
    const html = message.content
      .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.+?)\*/g, '<em>$1</em>')
      .replace(
        /`(.+?)`/g,
        '<code class="rounded px-1 py-0.5 text-sm" style="background: var(--surface-2); color: var(--text-primary);">$1</code>',
      )
      .replace(/\n/g, '<br />')
    return DOMPurify.sanitize(html, {
      ADD_ATTR: ['onerror', 'onload', 'ontoggle'],
      ADD_TAGS: ['details'],
      FORCE_BODY: false,
    })
  }, [message.content, isUser])

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div
        className={`max-w-[80%] rounded-2xl px-4 py-3 text-sm leading-relaxed ${
          isStreaming ? 'animate-pulse' : ''
        }`}
        style={
          isUser
            ? {
                background: 'var(--color-accent-violet)',
                color: '#FFFFFF',
              }
            : {
                background: 'var(--surface-2)',
                color: 'var(--text-primary)',
                border: '1px solid var(--border-soft)',
              }
        }
      >
        {isUser ? (
          <p>{message.content}</p>
        ) : (
          <div dangerouslySetInnerHTML={{ __html: formattedContent }} />
        )}

        {message.confidence !== undefined && !isUser && (
          <div className="mt-2 flex items-center gap-2">
            <div
              className="h-1 flex-1 rounded-full"
              style={{ background: 'var(--border-medium)' }}
            >
              <div
                className="h-full rounded-full transition-all"
                style={{
                  width: `${Math.round(message.confidence * 100)}%`,
                  background: 'var(--color-accent-green)',
                }}
              />
            </div>
            <span
              className="text-xs"
              style={{ color: 'var(--text-muted)' }}
            >
              {Math.round(message.confidence * 100)}%
            </span>
          </div>
        )}

        {message.sources && message.sources.length > 0 && !isUser && (
          <details className="mt-2">
            <summary
              className="cursor-pointer text-xs hover:opacity-80"
              style={{ color: 'var(--text-muted)' }}
            >
              {message.sources.length} fuente{message.sources.length !== 1 ? 's' : ''}
            </summary>
            <div className="mt-2 space-y-2">
              {message.sources.map((src, idx) => (
                <div
                  key={idx}
                  className="rounded-lg border p-2 text-xs"
                  style={{
                    borderColor: 'var(--border-soft)',
                    background: 'var(--bg-page)',
                    color: 'var(--text-secondary)',
                  }}
                >
                  <span
                    className="font-medium"
                    style={{ color: 'var(--text-primary)' }}
                  >
                    Relevancia: {(src.score * 100).toFixed(0)}%
                  </span>
                  <p className="mt-1">{src.content.slice(0, 200)}...</p>
                </div>
              ))}
            </div>
          </details>
        )}

        {!isUser && !isStreaming && (
          <div className="mt-2 flex items-center gap-2">
            {feedback ? (
              <span
                className="text-xs"
                style={{ color: 'var(--text-muted)' }}
              >
                <span aria-hidden="true">{feedback === 'up' ? '+' : '-'}</span>{' '}
                {feedback === 'up' ? 'Gracias' : 'Recibido'}
              </span>
            ) : (
              <>
                <button
                  type="button"
                  onClick={() => handleFeedback('up')}
                  disabled={submitting}
                  aria-label="Respuesta útil"
                  title="Útil"
                  className="rounded p-1 text-xs transition hover:opacity-80 disabled:opacity-50"
                  style={{ color: 'var(--text-muted)' }}
                  onMouseEnter={(e) => {
                    e.currentTarget.style.color = 'var(--color-accent-green)'
                  }}
                  onMouseLeave={(e) => {
                    e.currentTarget.style.color = 'var(--text-muted)'
                  }}
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                  ***REMOVED***ll="none"
                    viewBox="0 0 24 24"
                    strokeWidth={1.8}
                    stroke="currentColor"
                    className="h-4 w-4"
                    aria-hidden="true"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      d="M6.633 10.5c.806 0 1.533-.446 2.031-1.08a9.041 9.041 0 0 1 2.861-2.4c.723-.384 1.35-.956 1.653-1.715a4.498 4.498 0 0 0 .322-1.672V3.75a.75.75 0 0 1 .75-.75A2.25 2.25 0 0 1 16.5 5.25c0 .372-.048.732-.139 1.078-.092.347-.226.682-.397.973a2.25 2.25 0 0 0 1.94 3.306c.6 0 1.166-.189 1.643-.518a2.25 2.25 0 0 1 2.967 2.082 9.02 9.02 0 0 1-1.054 4.59 9.033 9.033 0 0 1-8.476 4.71H8.25a4.5 4.5 0 0 1-3.118-1.493l-.748-.749a2.25 2.25 0 0 0-1.59-.659H2.25a.75.75 0 0 1-.75-.75v-6.75a.75.75 0 0 1 .75-.75h2.884a2.25 2.25 0 0 1 1.5.586Z"
                    />
                  </svg>
                </button>
                <button
                  type="button"
                  onClick={() => handleFeedback('down')}
                  disabled={submitting}
                  aria-label="Respuesta no útil"
                  title="No útil"
                  className="rounded p-1 text-xs transition hover:opacity-80 disabled:opacity-50"
                  style={{ color: 'var(--text-muted)' }}
                  onMouseEnter={(e) => {
                    e.currentTarget.style.color = 'var(--color-accent-pink)'
                  }}
                  onMouseLeave={(e) => {
                    e.currentTarget.style.color = 'var(--text-muted)'
                  }}
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                  ***REMOVED***ll="none"
                    viewBox="0 0 24 24"
                    strokeWidth={1.8}
                    stroke="currentColor"
                    className="h-4 w-4"
                    aria-hidden="true"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      d="M7.5 15h2.25m8.024-9.75c.011.05.028.1.052.148.591 1.2.924 2.55.924 3.977a8.96 8.96 0 0 1-.999 4.125m.023-8.25c-.076-.365.183-.75.575-.75h.908c.889 0 1.713.518 1.972 1.368.339 1.11.521 2.287.521 3.507 0 1.553-.295 3.036-.831 4.398C20.613 14.547 19.833 15 19 15h-1.053c-.472 0-.745-.556-.5-.96a8.95 8.95 0 0 0 .303-.54m.023-8.25H16.48a4.5 4.5 0 0 1-1.423-.23l-3.114-1.04a4.5 4.5 0 0 0-1.423-.23H6.504c-.694 0-1.372.27-1.907.666L3.75 5.25M3.75 13.5l-1.378-7.643A1.125 1.125 0 0 1 3.49 4.5h1.378c.61 0 1.124.452 1.182 1.058L7.5 13.5"
                    />
                  </svg>
                </button>
              </>
            )}
          </div>
        )}
      </div>
    </div>
  )
}

'use client'

import { useMemo, useState } from 'react'

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
    return message.content
      .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.+?)\*/g, '<em>$1</em>')
      .replace(/`(.+?)`/g, '<code class="rounded bg-zinc-800 px-1 py-0.5 text-sm">$1</code>')
      .replace(/\n/g, '<br />')
  }, [message.content, isUser])

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div
        className={`max-w-[80%] rounded-2xl px-4 py-3 text-sm leading-relaxed ${
          isUser
            ? 'bg-violet-600 text-white'
            : 'border border-zinc-700 bg-zinc-800/50 text-zinc-200'
        } ${isStreaming ? 'animate-pulse' : ''}`}
      >
        {isUser ? (
          <p>{message.content}</p>
        ) : (
          <div dangerouslySetInnerHTML={{ __html: formattedContent }} />
        )}

        {message.confidence !== undefined && !isUser && (
          <div className="mt-2 flex items-center gap-2">
            <div className="h-1 flex-1 rounded-full bg-zinc-700">
              <div
                className="h-full rounded-full bg-green-500 transition-all"
                style={{ width: `${Math.round(message.confidence * 100)}%` }}
              />
            </div>
            <span className="text-xs text-zinc-500">
              {Math.round(message.confidence * 100)}%
            </span>
          </div>
        )}

        {message.sources && message.sources.length > 0 && !isUser && (
          <details className="mt-2">
            <summary className="cursor-pointer text-xs text-zinc-500 hover:text-zinc-400">
              {message.sources.length} fuente{message.sources.length !== 1 ? 's' : ''}
            </summary>
            <div className="mt-2 space-y-2">
              {message.sources.map((src, idx) => (
                <div
                  key={idx}
                  className="rounded-lg border border-zinc-700 bg-zinc-800 p-2 text-xs text-zinc-400"
                >
                  <span className="font-medium text-zinc-300">
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
              <span className="text-xs text-zinc-500">
                {feedback === 'up' ? '✓' : '✗'} {feedback === 'up' ? 'Gracias' : 'Recibido'}
              </span>
            ) : (
              <>
                <button
                  onClick={() => handleFeedback('up')}
                  disabled={submitting}
                  className="rounded p-1 text-xs text-zinc-500 transition hover:bg-zinc-700 hover:text-green-400 disabled:opacity-50"
                  title="Útil"
                >
                  👍
                </button>
                <button
                  onClick={() => handleFeedback('down')}
                  disabled={submitting}
                  className="rounded p-1 text-xs text-zinc-500 transition hover:bg-zinc-700 hover:text-red-400 disabled:opacity-50"
                  title="No útil"
                >
                  👎
                </button>
              </>
            )}
          </div>
        )}
      </div>
    </div>
  )
}

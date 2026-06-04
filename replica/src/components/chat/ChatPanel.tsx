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
        const { done, value } = await reader.read()
        if (done) break
        const chunk = decoder.decode(value, { stream: true })
        const lines = chunk.split('\n')
        for (const line of lines) {
          if (line.startsWith('data: ')) {
            const data = line.slice(6)
            if (data === '[DONE]') continue
            try {
              const parsed = JSON.parse(data)
              if (parsed.done) {
                finalConfidence = parsed.confidence
                finalSources = parsed.sources
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
      <div className="flex justify-center border-b border-zinc-800 py-2">
        <SiloToggle active={silo} onChange={setSilo} />
      </div>

      {/* Messages */}
      <div className="flex-1 space-y-4 overflow-y-auto p-4">
        {messages.length === 0 && !loading && (
          <div className="flex h-full items-center justify-center text-center">
            <div>
              <p className="text-2xl font-medium text-zinc-300">
                ¿En qué puedo ayudarte?
              </p>
              <p className="mt-2 text-sm text-zinc-500">
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
          <div className="flex items-center gap-2 px-4 py-2 text-zinc-500">
            <span className="flex gap-1">
              <span className="h-2 w-2 animate-bounce rounded-full bg-zinc-500 [animation-delay:0ms]" />
              <span className="h-2 w-2 animate-bounce rounded-full bg-zinc-500 [animation-delay:150ms]" />
              <span className="h-2 w-2 animate-bounce rounded-full bg-zinc-500 [animation-delay:300ms]" />
            </span>
            <span className="text-sm">Pensando...</span>
          </div>
        )}

        {error && (
          <div className="rounded-lg border border-red-800 bg-red-950/50 px-4 py-3 text-sm text-red-300">
            {error}
            <button
              onClick={() => setError(null)}
              className="ml-3 text-red-400 hover:text-red-300"
            >
              ✕
            </button>
          </div>
        )}

        <div ref={bottomRef} />
      </div>

      {/* Input */}
      <div className="border-t border-zinc-800 p-4">
        <div className="flex gap-3">
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Escribe tu pregunta..."
            rows={1}
            disabled={loading}
            className="flex-1 resize-none rounded-xl border border-zinc-700 bg-zinc-800/50 px-4 py-3 text-sm text-zinc-100 placeholder-zinc-500 outline-none transition focus:border-violet-600 focus:ring-1 focus:ring-violet-600 disabled:opacity-50"
          />
          <button
            onClick={sendMessage}
            disabled={loading || !input.trim()}
            className="rounded-xl bg-violet-600 px-5 py-3 text-sm font-medium text-white transition hover:bg-violet-500 disabled:cursor-not-allowed disabled:opacity-50"
          >
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="h-5 w-5">
              <path strokeLinecap="round" strokeLinejoin="round" d="M6 12 3.269 3.125A59.769 59.769 0 0 1 21.485 12 59.768 59.768 0 0 1 3.27 20.875L5.999 12Zm0 0h7.5" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  )
}

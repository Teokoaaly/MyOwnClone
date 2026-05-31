"use client";

import { useState, useRef, useEffect } from "react";

interface Message {
  id: string;
  role: "user" | "assistant";
  content: string;
  confidence?: number;
  sources?: Array<{ content: string; score: number }>;
}

interface Props {
  cloneId: string;
  cloneName: string;
  slug: string;
}

export function CloneChat({ cloneId, cloneName, slug }: Props) {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: "welcome",
      role: "assistant",
      content: `¡Hola! Soy ${cloneName}, un clon de IA entrenado para ayudarte. ¿En qué puedo ayudarte hoy?`,
    },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [streaming, setStreaming] = useState("");
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const [conversationId, setConversationId] = useState<string>();
  const [mode, setMode] = useState<string>("pedagogy");

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, streaming]);

  async function handleSend() {
    if (!input.trim() || loading) return;

    const userMessage: Message = {
      id: crypto.randomUUID(),
      role: "user",
      content: input,
    };

    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const res = await fetch(`/api/clone/${slug}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          message: input,
          conversationId,
          mode,
        }),
      });

      if (!res.ok) throw new Error("Chat error");

      const reader = res.body?.getReader();
      if (!reader) throw new Error("No response stream");

      const decoder = new TextDecoder();
      let fullResponse = "";
      let finalConfidence: number | undefined;
      let finalSources: Array<{ content: string; score: number }> | undefined;
      let finalConversationId: string | undefined;

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        const chunk = decoder.decode(value, { stream: true });
        const lines = chunk.split("\n");
        for (const line of lines) {
          if (line.startsWith("data: ")) {
            const data = line.slice(6);
            if (data === "[DONE]") continue;
            try {
              const parsed = JSON.parse(data);
              if (parsed.done) {
                finalConfidence = parsed.confidence;
                finalSources = parsed.sources;
                finalConversationId = parsed.conversationId;
              } else {
                fullResponse += parsed.content || "";
                setStreaming(fullResponse);
              }
            } catch {
              fullResponse += data;
              setStreaming(fullResponse);
            }
          }
        }
      }

      if (finalConversationId) setConversationId(finalConversationId);

      setMessages((prev) => [
        ...prev,
        {
          id: crypto.randomUUID(),
          role: "assistant",
          content: fullResponse,
          confidence: finalConfidence,
          sources: finalSources,
        },
      ]);
      setStreaming("");
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          id: crypto.randomUUID(),
          role: "assistant",
          content:
            "Lo siento, ha ocurrido un error. Por favor, intenta de nuevo.",
        },
      ]);
      setStreaming("");
    } finally {
      setLoading(false);
    }
  }

  function handleNewChat() {
    setMessages([
      {
        id: "welcome",
        role: "assistant",
        content: `¡Hola! Soy ${cloneName}, un clon de IA entrenado para ayudarte. ¿En qué puedo ayudarte hoy?`,
      },
    ]);
    setConversationId(undefined);
  }

  const modes = [
    { value: "pedagogy", label: "Pedagogía" },
    { value: "sales", label: "Ventas" },
    { value: "support", label: "Soporte" },
  ];

  return (
    <div className="flex-1 flex flex-col">
      <div className="flex items-center gap-2 px-6 py-2 bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-800">
        <button
          onClick={handleNewChat}
          className="text-sm text-purple-600 hover:text-purple-700 font-medium"
        >
          + Nueva conversación
        </button>
        <div className="ml-auto flex gap-2">
          {modes.map((m) => (
            <button
              key={m.value}
              onClick={() => setMode(m.value)}
              className={`px-3 py-1 text-xs rounded-full transition-colors ${
                mode === m.value
                  ? "bg-purple-100 dark:bg-purple-900 text-purple-700 dark:text-purple-300"
                  : "bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-400 hover:bg-gray-200"
              }`}
            >
              {m.label}
            </button>
          ))}
        </div>
      </div>

      <div className="flex-1 overflow-y-auto px-6 py-4 space-y-4">
        {messages.map((msg) => (
          <div
            key={msg.id}
            className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}
          >
            <div
              className={`max-w-[80%] rounded-2xl px-4 py-3 ${
                msg.role === "user"
                  ? "bg-purple-600 text-white"
                  : "bg-white dark:bg-gray-800 text-gray-900 dark:text-white border border-gray-200 dark:border-gray-700"
              }`}
            >
              <p className="text-sm whitespace-pre-wrap">{msg.content}</p>
              {msg.confidence !== undefined && msg.role === "assistant" && (
                <div className="mt-2 flex items-center gap-2">
                  <div className="flex-1 h-1 bg-gray-200 dark:bg-gray-700 rounded-full">
                    <div
                      className={`h-1 rounded-full ${
                        msg.confidence >= 0.7
                          ? "bg-green-500"
                          : msg.confidence >= 0.5
                            ? "bg-yellow-500"
                            : "bg-red-500"
                      }`}
                      style={{ width: `${msg.confidence * 100}%` }}
                    />
                  </div>
                  <span className="text-xs text-gray-400">
                    {Math.round(msg.confidence * 100)}%
                  </span>
                </div>
              )}
              {msg.sources && msg.sources.length > 0 && msg.role === "assistant" && (
                <div className="mt-2 pt-2 border-t border-gray-200 dark:border-gray-700">
                  <p className="text-xs font-medium text-gray-500 dark:text-gray-400 mb-1">
                    Fuentes:
                  </p>
                  <div className="space-y-1">
                    {msg.sources.slice(0, 3).map((source, i) => (
                      <div key={i} className="text-xs text-gray-400 dark:text-gray-500 truncate">
                        <span className="text-purple-500 font-medium">
                          {(source.score * 100).toFixed(0)}%
                        </span>{" "}
                        {source.content.slice(0, 100)}...
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </div>
        ))}
        {streaming && (
          <div className="flex justify-start">
            <div className="max-w-[80%] rounded-2xl px-4 py-3 bg-white dark:bg-gray-800 text-gray-900 dark:text-white border border-gray-200 dark:border-gray-700">
              <p className="text-sm whitespace-pre-wrap">{streaming}</p>
            </div>
          </div>
        )}
        {loading && !streaming && (
          <div className="flex justify-start">
            <div className="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-2xl px-4 py-3">
              <div className="typing-dots flex gap-1">
                <span className="w-2 h-2 bg-gray-400 rounded-full" />
                <span className="w-2 h-2 bg-gray-400 rounded-full" />
                <span className="w-2 h-2 bg-gray-400 rounded-full" />
              </div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <div className="px-6 py-4 bg-white dark:bg-gray-900 border-t border-gray-200 dark:border-gray-800">
        <form
          onSubmit={(e) => {
            e.preventDefault();
            handleSend();
          }}
          className="flex gap-3"
        >
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Escribe tu mensaje aquí..."
            disabled={loading}
            className="flex-1 px-4 py-3 border border-gray-300 dark:border-gray-700 rounded-xl bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-purple-500 focus:border-transparent outline-none transition-colors disabled:opacity-50"
          />
          <button
            type="submit"
            disabled={loading || !input.trim()}
            className="px-6 py-3 bg-purple-600 text-white font-semibold rounded-xl hover:bg-purple-700 disabled:opacity-50 transition-colors"
          >
            Enviar
          </button>
        </form>
      </div>
    </div>
  );
}

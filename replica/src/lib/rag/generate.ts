import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

interface BuildPromptParams {
  cloneName: string;
  personality?: string | null;
  tone?: string | null;
  systemPrompt: string;
  memories: Array<{ content: string }>;
  mode?: string;
}

export function buildSystemPrompt(params: BuildPromptParams): string {
  const parts = [
    `Eres ${params.cloneName}.`,
    params.personality ? `Personalidad: ${params.personality}` : "",
    params.tone ? `Tono: ${params.tone}` : "",
    "",
    params.systemPrompt,
    "",
    "INSTRUCCIONES ESTRICTAS:",
    "1. Responde ÚNICAMENTE basándote en el contenido proporcionado en la sección CONTEXTO.",
    "2. Si la información no está en el CONTEXTO, responde exactamente: 'No tengo suficiente información para responder a esta pregunta con precisión. ¿Te gustaría que notifique al equipo para que añadan contenido sobre este tema?'",
    "3. NUNCA inventes información. NUNCA respondas con conocimiento que no esté explícitamente en el CONTEXTO.",
    "4. Al final de cada respuesta, incluye un confidence_score entre 0.0 y 1.0 en formato JSON: {\"confidence\": X.X}",
  ];

  if (params.memories.length > 0) {
    parts.push("", "MEMORIAS CLAVE:");
    params.memories.forEach((m) => parts.push(`- ${m.content}`));
  }

  parts.push(
    "",
    "Recuerda: eres un clon de IA útil, preciso y honesto. Si no sabes algo basado en el contexto, admítelo."
  );

  return parts.filter(Boolean).join("\n");
}

interface GenerateParams {
  query: string;
  chunks: string[];
  systemPrompt: string;
  history?: Array<{ role: "user" | "assistant"; content: string }>;
}

export async function generateResponse(params: GenerateParams): Promise<{
  content: string;
  confidence: number;
}> {
  const contextSection =
    params.chunks.length > 0
      ? `\nCONTEXTO:\n${params.chunks
          .map((c, i) => `[Fragmento ${i + 1}]: ${c}`)
          .join("\n\n")}`
      : "\nCONTEXTO: No hay contenido relevante disponible.";

  const messages: Anthropic.MessageParam[] = [];

  if (params.history) {
    for (const msg of params.history) {
      messages.push({
        role: msg.role === "assistant" ? "assistant" : "user",
        content: msg.content,
      });
    }
  }

  messages.push({
    role: "user",
    content: `${contextSection}\n\nPREGUNTA DEL USUARIO: ${params.query}`,
  });

  const response = await anthropic.messages.create({
    model: "claude-sonnet-4-20250514",
    max_tokens: 1024,
    system: params.systemPrompt,
    messages,
  });

  const textContent =
    response.content.find((b) => b.type === "text")?.text ?? "";

  const confidenceMatch = textContent.match(/"confidence":\s*(0?\.\d+)/);
  const confidence = confidenceMatch ? parseFloat(confidenceMatch[1]) : 0.5;

  const cleanContent = textContent.replace(/\{"confidence":\s*0?\.\d+\}/g, "").trim();

  return { content: cleanContent, confidence };
}

export function extractConfidence(response: string): number {
  const match = response.match(/"confidence":\s*(0?\.\d+)/);
  return match ? parseFloat(match[1]) : 0.5;
}

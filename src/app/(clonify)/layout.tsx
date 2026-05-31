import type { Metadata } from 'next'
import '../globals.css'

export const metadata: Metadata = {
  title: 'Réplica — Tu clon de IA',
  description: 'Chatea con el clon de IA entrenado con el conocimiento del creador',
}

export default function ClonifyLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-gradient-to-b from-zinc-950 to-zinc-900 text-zinc-100">
      {children}
    </div>
  )
}

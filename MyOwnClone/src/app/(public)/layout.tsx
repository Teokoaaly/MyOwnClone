import type { Metadata } from 'next'
import '../globals.css'

export const metadata: Metadata = {
  title: 'YouOwnClone',
  description: 'Your AI clone platform',
}

export default function YouOwnCloneLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-gradient-to-b from-zinc-950 to-zinc-900 text-zinc-100">
      {children}
    </div>
  )
}

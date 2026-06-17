import type { Metadata } from 'next'
import '../globals.css'

export const metadata: Metadata = {
  title: 'MyOwnClone',
  description: 'Your AI clone platform',
  icons: {
    icon: '/favicon.ico',
    shortcut: '/favicon.ico',
    apple: '/favicon.ico',
  },
}

export default function YouOwnCloneLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-gradient-to-b from-zinc-950 to-zinc-900 text-zinc-100">
      {children}
    </div>
  )
}

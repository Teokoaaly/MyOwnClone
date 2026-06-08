'use client'

const SILOS = [
  { id: 'teach', label: 'Aprender', emoji: '📚' },
  { id: 'support', label: 'Soporte', emoji: '💬' },
  { id: 'sales', label: 'Ventas', emoji: '🛒' },
] as const

interface SiloToggleProps {
  active: string
  onChange: (silo: string) => void
}

export function SiloToggle({ active, onChange }: SiloToggleProps) {
  return (
    <div className="inline-flex gap-1 rounded-xl border border-zinc-700 bg-zinc-800/50 p-1">
      {SILOS.map((silo) => {
        const isActive = active === silo.id
        return (
          <button
            key={silo.id}
            onClick={() => onChange(silo.id)}
            className={`flex items-center gap-1.5 rounded-lg px-3 py-1.5 text-sm font-medium transition ${
              isActive
                ? 'bg-violet-600 text-white shadow-lg shadow-violet-600/25'
                : 'text-zinc-400 hover:text-zinc-200'
            }`}
          >
            <span>{silo.emoji}</span>
            <span className="hidden sm:inline">{silo.label}</span>
          </button>
        )
      })}
    </div>
  )
}

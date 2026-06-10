'use client'

const SILOS = [
  { id: 'teach', label: 'Learn', icon: 'book' },
  { id: 'support', label: 'Support', icon: 'chat' },
  { id: 'sales', label: 'Sales', icon: 'cart' },
] as const

interface SiloToggleProps {
  active: string
  onChange: (silo: string) => void
}

function SiloIcon({ icon, className }: { icon: string; className?: string }) {
  if (icon === 'book') {
    return (
      <svg
        xmlns="http://www.w3.org/2000/svg"
      ***REMOVED***ll="none"
        viewBox="0 0 24 24"
        strokeWidth={1.8}
        stroke="currentColor"
        className={className}
        aria-hidden="true"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          d="M12 6.042A8.967 8.967 0 0 0 6 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 0 1 6 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 0 1 6-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0 0 18 18a8.967 8.967 0 0 0-6 2.292m0-14.25v14.25"
        />
      </svg>
    )
  }
  if (icon === 'chat') {
    return (
      <svg
        xmlns="http://www.w3.org/2000/svg"
      ***REMOVED***ll="none"
        viewBox="0 0 24 24"
        strokeWidth={1.8}
        stroke="currentColor"
        className={className}
        aria-hidden="true"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          d="M8.625 12a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H8.25m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H12m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0h-.375M21 12c0 4.556-4.03 8.25-9 8.25a9.764 9.764 0 0 1-2.555-.337A5.972 5.972 0 0 1 5.41 20.97a5.969 5.969 0 0 1-.474-.065 4.48 4.48 0 0 0 .978-2.025c.09-.457-.133-.901-.467-1.226C3.93 16.178 3 14.189 3 12c0-4.556 4.03-8.25 9-8.25s9 3.694 9 8.25Z"
        />
      </svg>
    )
  }
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
    ***REMOVED***ll="none"
      viewBox="0 0 24 24"
      strokeWidth={1.8}
      stroke="currentColor"
      className={className}
      aria-hidden="true"
    >
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        d="M2.25 3h1.386c.51 0 .955.343 1.087.835l.383 1.437M7.5 14.25a3 3 0 0 0-3 3h15.75m-12.75-3h11.218c1.121-2.3 2.1-4.684 2.924-7.138a60.114 60.114 0 0 0-16.536-1.84M7.5 14.25 5.106 5.272M6 20.25a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Zm12.75 0a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Z"
      />
    </svg>
  )
}

export function SiloToggle({ active, onChange }: SiloToggleProps) {
  return (
    <div
      role="group"
      aria-label="Conversation mode"
      className="inline-flex gap-1 rounded-xl border p-1"
      style={{
        borderColor: 'var(--border-medium)',
        background: 'var(--surface-2)',
      }}
    >
      {SILOS.map((silo) => {
        const isActive = active === silo.id
        return (
          <button
            key={silo.id}
            type="button"
            onClick={() => onChange(silo.id)}
            aria-pressed={isActive}
            className="flex items-center gap-1.5 rounded-lg px-3 py-1.5 text-sm font-medium transition focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--color-accent-violet)]"
            style={
              isActive
                ? {
                    background: 'var(--color-accent-violet)',
                    color: 'var(--bg-shell)',
                    boxShadow: '0 8px 24px -8px var(--color-accent-violet)',
                  }
                : {
                    color: 'var(--text-secondary)',
                  }
            }
          >
            <SiloIcon icon={silo.icon} className="h-4 w-4" />
            <span className="hidden sm:inline">{silo.label}</span>
          </button>
        )
      })}
    </div>
  )
}

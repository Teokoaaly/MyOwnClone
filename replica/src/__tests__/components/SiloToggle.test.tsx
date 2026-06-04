import { describe, it, expect, vi } from 'vitest'
import { render, screen, fireEvent } from '@testing-library/react'
import { SiloToggle } from '@/components/chat/SiloToggle'

describe('SiloToggle', () => {
  it('renders all three silo buttons', () => {
    render(<SiloToggle active="teach" onChange={() => {}} />)
    expect(screen.getByText('Aprender')).toBeDefined()
    expect(screen.getByText('Soporte')).toBeDefined()
    expect(screen.getByText('Ventas')).toBeDefined()
  })

  it('highlights the active silo button', () => {
    render(<SiloToggle active="support" onChange={() => {}} />)
    const supportBtn = screen.getByText('Soporte').closest('button')
    expect(supportBtn?.className).toContain('bg-violet-600')
  })

  it('calls onChange with silo id when clicked', () => {
    const onChange = vi.fn()
    render(<SiloToggle active="teach" onChange={onChange} />)
    fireEvent.click(screen.getByText('Ventas'))
    expect(onChange).toHaveBeenCalledWith('sales')
  })

  it('non-active buttons do not have bg-violet-600 class', () => {
    render(<SiloToggle active="teach" onChange={() => {}} />)
    const supportBtn = screen.getByText('Soporte').closest('button')
    expect(supportBtn?.className).toContain('text-zinc-400')
  })
})

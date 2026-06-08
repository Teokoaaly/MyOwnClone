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

  it('highlights the active silo button via inline style', () => {
    render(<SiloToggle active="support" onChange={() => {}} />)
    const supportBtn = screen.getByText('Soporte').closest('button') as HTMLElement
    expect(supportBtn.getAttribute('aria-pressed')).toBe('true')
    const style = (supportBtn as HTMLElement).style
    expect(style.background || style.cssText).toMatch(/color-accent-violet/)
  })

  it('calls onChange with silo id when clicked', () => {
    const onChange = vi.fn()
    render(<SiloToggle active="teach" onChange={onChange} />)
    fireEvent.click(screen.getByText('Ventas'))
    expect(onChange).toHaveBeenCalledWith('sales')
  })

  it('non-active buttons have aria-pressed=false and no violet background', () => {
    render(<SiloToggle active="teach" onChange={() => {}} />)
    const supportBtn = screen.getByText('Soporte').closest('button') as HTMLElement
    expect(supportBtn.getAttribute('aria-pressed')).toBe('false')
    const style = (supportBtn as HTMLElement).style
    // Inactive buttons have secondary text color, not the violet accent
    expect(style.background || '').not.toMatch(/color-accent-violet/)
    expect(style.color || '').toMatch(/text-secondary/)
  })
})

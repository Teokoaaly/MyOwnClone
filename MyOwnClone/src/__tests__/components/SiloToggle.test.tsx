import { describe, it, expect, vi, afterEach } from 'vitest'
import { render, screen, fireEvent, cleanup } from '@testing-library/react'
import { SiloToggle } from '@/components/chat/SiloToggle'

describe('SiloToggle', () => {
  afterEach(() => cleanup())

  it('renders all three silo buttons', () => {
    render(<SiloToggle active="teach" onChange={() => {}} />)
    expect(screen.getAllByText('Learn').length).toBeGreaterThanOrEqual(1)
    expect(screen.getAllByText('Support').length).toBeGreaterThanOrEqual(1)
    expect(screen.getAllByText('Sales').length).toBeGreaterThanOrEqual(1)
  })

  it('highlights the active silo button via inline style', () => {
    render(<SiloToggle active="support" onChange={() => {}} />)
    const supportBtn = screen.getAllByText('Support')[0].closest('button') as HTMLElement
    expect(supportBtn.getAttribute('aria-pressed')).toBe('true')
    const style = supportBtn.style
    expect(style.background || style.cssText).toMatch(/color-accent-violet/)
  })

  it('calls onChange with silo id when clicked', () => {
    const onChange = vi.fn()
    render(<SiloToggle active="teach" onChange={onChange} />)
    fireEvent.click(screen.getAllByText('Sales')[0])
    expect(onChange).toHaveBeenCalledWith('sales')
  })

  it('non-active buttons have aria-pressed=false and no violet background', () => {
    render(<SiloToggle active="teach" onChange={() => {}} />)
    const supportBtn = screen.getAllByText('Support')[0].closest('button') as HTMLElement
    expect(supportBtn.getAttribute('aria-pressed')).toBe('false')
    const style = supportBtn.style
    expect(style.background || '').not.toMatch(/color-accent-violet/)
    expect(style.color || '').toMatch(/text-secondary/)
  })
})

import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest'
import { render, screen, fireEvent, cleanup, within } from '@testing-library/react'
import { SearchCommandBar } from '@/components/ui/SearchCommandBar'

// Mock i18n navigation.
const pushMock = vi.fn()
vi.mock('@/i18n/navigation', () => ({
  Link: ({ children, href, onClick, ...props }: any) => <a href={href} onClick={onClick} {...props}>{children}</a>,
  useRouter: () => ({ push: pushMock }),
  usePathname: () => '/resumen',
}))

// Mock fetch globally for the dynamic data fetch.
const fetchMock = vi.fn()
global.fetch = fetchMock

// jsdom does not implement scrollIntoView.
Element.prototype.scrollIntoView = vi.fn()

// Helper: render with a known list of pages.
function renderOpen() {
  // Open the trigger first.
  render(
    <SearchCommandBar
      pages={[
        { href: '/resumen', label: 'Resumen', icon: '📊' },
        { href: '/cerebro', label: 'Cerebro', icon: '🧠' },
        { href: '/productos', label: 'Productos', icon: '📦' },
      ]}
    />,
  )
***REMOVED***reEvent.click(screen.getByRole('button', { name: /open search/i }))
}

describe('SearchCommandBar', () => {
  beforeEach(() => {
    fetchMock.mockReset()
    pushMock.mockReset()
    fetchMock.mockResolvedValue({ ok: true, json: () => Promise.resolve([]) })
  })
  afterEach(() => {
    cleanup()
  })

  it('renders only a trigger button when closed', () => {
    render(
      <SearchCommandBar
        pages={[{ href: '/resumen', label: 'Resumen', icon: '📊' }]}
      />,
    )
    expect(screen.queryByRole('dialog')).toBeNull()
    expect(
      screen.getByRole('button', { name: /open search/i }),
    ).toBeDefined()
  })

  it('opens a dialog when the trigger is clicked', () => {
    renderOpen()
    const dialog = screen.getByRole('dialog')
    expect(dialog).toBeDefined()
    expect(dialog.getAttribute('aria-modal')).toBe('true')
  })

  it('lists the static pages when the query is empty', () => {
    renderOpen()
    // Each page becomes an <li role="option">. Three pages, three options.
    const options = screen.getAllByRole('option')
    expect(options).toHaveLength(3)
  })

  it('filters results by query', () => {
    renderOpen()
    const input = screen.getByPlaceholderText(/search pages/i)
  ***REMOVED***reEvent.change(input, { target: { value: 'cere' } })
    // "Cerebro" still matches. "Resumen" and "Productos" do not.
    const options = screen.getAllByRole('option')
    expect(options).toHaveLength(1)
    expect(within(options[0]).getByText('Cerebro')).toBeDefined()
  })

  it('navigates with ArrowDown / ArrowUp', () => {
    renderOpen()
    const input = screen.getByPlaceholderText(/search pages/i)
    // aria-activedescendant lives on the input (the combobox), not
    // on the listbox.
    // initial active idx = 0
    expect(input.getAttribute('aria-activedescendant')).toBe('cmdk-result-0')
  ***REMOVED***reEvent.keyDown(window, { key: 'ArrowDown' })
    expect(input.getAttribute('aria-activedescendant')).toBe('cmdk-result-1')
  ***REMOVED***reEvent.keyDown(window, { key: 'ArrowUp' })
    expect(input.getAttribute('aria-activedescendant')).toBe('cmdk-result-0')
  })

  it('Enter on a result calls router.push and closes the dialog', () => {
    renderOpen()
  ***REMOVED***reEvent.keyDown(window, { key: 'ArrowDown' }) // idx = 1 -> /cerebro
  ***REMOVED***reEvent.keyDown(window, { key: 'Enter' })
    expect(pushMock).toHaveBeenCalledWith('/cerebro')
    // Dialog should now be unmounted.
    expect(screen.queryByRole('dialog')).toBeNull()
  })

  it('Escape closes the dialog', () => {
    renderOpen()
    expect(screen.queryByRole('dialog')).not.toBeNull()
  ***REMOVED***reEvent.keyDown(window, { key: 'Escape' })
    expect(screen.queryByRole('dialog')).toBeNull()
  })

  it('Cmd+K toggles the dialog from anywhere', () => {
    render(
      <SearchCommandBar
        pages={[{ href: '/resumen', label: 'Resumen', icon: '📊' }]}
      />,
    )
    expect(screen.queryByRole('dialog')).toBeNull()
  ***REMOVED***reEvent.keyDown(window, { key: 'k', metaKey: true })
    expect(screen.queryByRole('dialog')).not.toBeNull()
  ***REMOVED***reEvent.keyDown(window, { key: 'k', metaKey: true })
    expect(screen.queryByRole('dialog')).toBeNull()
  })

  it('Ctrl+K also opens the dialog', () => {
    render(
      <SearchCommandBar
        pages={[{ href: '/resumen', label: 'Resumen', icon: '📊' }]}
      />,
    )
  ***REMOVED***reEvent.keyDown(window, { key: 'k', ctrlKey: true })
    expect(screen.queryByRole('dialog')).not.toBeNull()
  })
})

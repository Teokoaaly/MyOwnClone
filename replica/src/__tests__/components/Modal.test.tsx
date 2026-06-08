import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest'
import { render, screen, fireEvent, cleanup } from '@testing-library/react'
import { useState } from 'react'
import { Modal } from '@/components/ui/Modal'

// Modal mounts a <div role="dialog"> only when `open` is true. The
// container must therefore be toggleable. We wrap Modal in a tiny
// host component to control it from tests.
function Host({
  initiallyOpen = true,
  onClose,
  children = <button>Inside</button>,
}: {
  initiallyOpen?: boolean
  onClose?: () => void
  children?: React.ReactNode
}) {
  const [open, setOpen] = useState(initiallyOpen)
  return (
    <>
      <button data-testid="trigger" onClick={() => setOpen(true)}>Open</button>
      <button data-testid="external">External</button>
      <Modal
        open={open}
        onClose={() => {
          onClose?.()
          setOpen(false)
        }}
        title="Title here"
      >
        {children}
      </Modal>
    </>
  )
}

describe('Modal', () => {
  beforeEach(() => {
    // jsdom defaults body.activeElement to null; give it a real node.
    document.body.innerHTML = ''
  })
  afterEach(() => {
    cleanup()
  })

  it('renders nothing when closed', () => {
    render(<Host initiallyOpen={false} />)
    expect(screen.queryByRole('dialog')).toBeNull()
  })

  it('renders title and an accessible labelled dialog when open', () => {
    render(<Host />)
    const dialog = screen.getByRole('dialog')
    expect(dialog).toBeDefined()
    expect(dialog.getAttribute('aria-modal')).toBe('true')
    // The dialog is labelled by the title <h2>.
    const title = screen.getByText('Title here')
    expect(title.tagName).toBe('H2')
    expect(dialog.getAttribute('aria-labelledby')).toBe(title.id)
  })

  it('closes when Escape is pressed', () => {
    const onClose = vi.fn()
    render(<Host onClose={onClose} />)
    fireEvent.keyDown(window, { key: 'Escape' })
    expect(onClose).toHaveBeenCalled()
  })

  it('closes when the backdrop is clicked', () => {
    const onClose = vi.fn()
    render(<Host onClose={onClose} />)
    // The first absolute sibling is the backdrop. Find it via the
    // aria-hidden marker — backdrops are decorative.
    const backdrop = document.querySelector('[aria-hidden="true"]') as HTMLElement
    expect(backdrop).toBeTruthy()
    fireEvent.click(backdrop)
    expect(onClose).toHaveBeenCalled()
  })

  it('traps focus at the end of the focusable list with Tab', async () => {
    function Multi() {
      const [open, setOpen] = useState(true)
      return (
        <Modal
          open={open}
          onClose={() => setOpen(false)}
          title="t"
        >
          <button>A</button>
          <button>B</button>
          <button>C</button>
        </Modal>
      )
    }
    render(<Multi />)
    // Initial focus should be on the first focusable inside the dialog
    // (the close button, because the tabbable children are rendered
    // after it in the DOM). Use the keyboard handler to verify the
    // wrap behaviour: focus the last button, then press Tab and
    // expect focus to land on the first.
    const buttons = screen.getAllByRole('button')
    const last = buttons[buttons.length - 1]
    last.focus()
    fireEvent.keyDown(window, { key: 'Tab' })
    // We cannot directly assert document.activeElement after the
    // synthetic handler (the handler only calls e.preventDefault and
    // moves focus, which jsdom reflects on activeElement).
    expect(document.activeElement).toBe(buttons[0])
  })

  it('traps focus at the start of the focusable list with Shift+Tab', () => {
    function Multi() {
      const [open, setOpen] = useState(true)
      return (
        <Modal
          open={open}
          onClose={() => setOpen(false)}
          title="t"
        >
          <button>A</button>
          <button>B</button>
        </Modal>
      )
    }
    render(<Multi />)
    const buttons = screen.getAllByRole('button')
    // Focus the first focusable inside the dialog (the close button)
    // and Shift+Tab — the trap should cycle to the last.
    buttons[0].focus()
    fireEvent.keyDown(window, { key: 'Tab', shiftKey: true })
    expect(document.activeElement).toBe(buttons[buttons.length - 1])
  })
})

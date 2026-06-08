"use client";

import { type FC, type ReactNode, useCallback } from "react";
import * as Dialog from "@radix-ui/react-dialog";

export interface SheetProps {
  open: boolean;
  onClose: () => void;
  children: ReactNode;
  /** Accessibility label for the dialog. Required for screen readers. */
  title: string;
  /** Optional description for the dialog. */
  description?: string;
  /** Side from which the sheet slides in. Default: "left". */
  side?: "left" | "right";
  /** Width of the sheet. Default: "280px". */
  width?: string;
}

const sideClasses: Record<NonNullable<SheetProps["side"]>, string> = {
  left: "inset-y-0 left-0 data-[state=open]:animate-slideInLeft data-[state=closed]:animate-slideOutLeft",
  right: "inset-y-0 right-0 data-[state=open]:animate-slideInRight data-[state=closed]:animate-slideOutRight",
};

export const Sheet: FC<SheetProps> = ({
  open,
  onClose,
  children,
  title,
  description,
  side = "left",
  width = "280px",
}) => {
  const handleOpenChange = useCallback(
    (isOpen: boolean) => {
      if (!isOpen) onClose();
    },
    [onClose],
  );

  return (
    <Dialog.Root open={open} onOpenChange={handleOpenChange}>
      <Dialog.Portal>
        {/* Overlay */}
        <Dialog.Overlay className="fixed inset-0 z-40 bg-black/40 backdrop-blur-sm data-[state=open]:animate-fadeIn data-[state=closed]:animate-fadeOut" />

        {/* Sheet content */}
        <Dialog.Content
          aria-describedby={description ? undefined : undefined}
          className={`fixed z-50 flex flex-col outline-none ${sideClasses[side]}`}
          style={{
            width,
            background: "var(--bg-sidebar)",
            borderColor: "var(--border-soft)",
            boxShadow:
              side === "left"
                ? "4px 0 64px rgba(15,23,42,0.18)"
                : "-4px 0 64px rgba(15,23,42,0.18)",
          }}
        >
          {/* Hidden title for screen readers */}
          <Dialog.Title className="sr-only">{title}</Dialog.Title>
          {description && (
            <Dialog.Description className="sr-only">
              {description}
            </Dialog.Description>
          )}

          {children}
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
};

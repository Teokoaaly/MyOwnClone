import { type FC } from "react";

interface HeaderBreadcrumbProps {
  title?: string;
  breadcrumbs?: string[];
  user?: {
    name?: string | null;
    email?: string | null;
    image?: string | null;
  };
  /** Action button rendered on the right side (e.g. "Create Clone") */
  action?: React.ReactNode;
}

export const HeaderBreadcrumb: FC<HeaderBreadcrumbProps> = ({
  title = "Workspace Overview",
  breadcrumbs = ["MyOwnClone", "Admin", "Dashboard"],
  user,
  action,
}) => {
  const initials = user?.name
    ? user.name.charAt(0).toUpperCase()
    : user?.email?.charAt(0).toUpperCase() ?? "U";

  return (
    <div className="flex items-center justify-between mb-5">
      {/* Left: breadcrumb + title */}
      <div>
        {/* Breadcrumb */}
        <nav
          aria-label="Ruta"
          className="flex items-center gap-1 text-xs text-[var(--text-muted)] mb-1.5"
        >
          <ol className="flex items-center gap-1">
            {breadcrumbs.map((segment, i) => {
              const isLast = i === breadcrumbs.length - 1;
              return (
                <li
                  key={`${segment}-${i}`}
                  className="flex items-center gap-1"
                >
                  {i > 0 && (
                    <svg
                      aria-hidden="true"
                      className="h-3 w-3 text-[var(--text-faint)]"
                    ***REMOVED***ll="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth={2}
                        d="M9 5l7 7-7 7"
                      />
                    </svg>
                  )}
                  <span
                    aria-current={isLast ? "page" : undefined}
                    className={
                      isLast
                        ? "text-[var(--text-primary)] font-medium"
                        : ""
                    }
                  >
                    {segment}
                  </span>
                </li>
              );
            })}
          </ol>
        </nav>

        {/* Title */}
        <h1 className="text-xl font-semibold text-[var(--text-primary)] tracking-tight">
          {title}
        </h1>
      </div>

      {/* Right: action + avatar */}
      <div className="flex items-center gap-3">
        {action}
        {user && (
          <div
            className="h-8 w-8 rounded-full bg-gradient-to-br from-[#F97316] to-[#FB923C] flex items-center justify-center text-white text-xs font-semibold font-sans shadow-sm"
            role="img"
            aria-label={user.name ?? user.email ?? "Usuario"}
          >
            {user.image ? (
              <img
                src={user.image}
                alt=""
                className="h-full w-full rounded-full object-cover"
              />
            ) : (
              <span aria-hidden="true">{initials}</span>
            )}
          </div>
        )}
      </div>
    </div>
  );
};
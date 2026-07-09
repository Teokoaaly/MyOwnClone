"""Tour definitions — registry of all tours and their steps.

Each tour has a unique ID, display name, and ordered list of steps.
Steps have a key, title, optional description, and position for the UI.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TourStep:
    key: str
    title: str
    description: str = ""
    position: str = "bottom_center"
    icon: str | None = None


@dataclass
class TourDefinition:
    id: str
    name: str
    steps: list[TourStep] = field(default_factory=list)

    @property
    def step_keys(self) -> list[str]:
        return [s.key for s in self.steps]

    def get_step(self, key: str) -> TourStep | None:
        for s in self.steps:
            if s.key == key:
                return s
        return None


# ─── Tour Registry ───────────────────────────────────────────────────────

ONBOARDING_TOUR = TourDefinition(
    id="onboarding",
    name="Onboarding",
    steps=[
        TourStep("knowledge", "Conecta tus fuentes", "Import content from LinkedIn, Twitter, website, PDFs, audio, video.", icon="book-open"),
        TourStep("voice-clone", "Crea tu clon de voz", "Record or upload 5-10 minutes of audio to clone your voice.", icon="mic"),
        TourStep("persona", "Personaliza tu agente", "Configure how your AI agent looks and behaves.", icon="users"),
    ],
)

DASHBOARD_TOUR = TourDefinition(
    id="dashboard",
    name="Dashboard Tour",
    steps=[
        TourStep("quick-actions", "Quick Actions", "Access common tasks from here.", position="bottom_center"),
        TourStep("personas-overview", "Your Personas", "View and manage all your AI personas.", position="bottom_center"),
        TourStep("knowledge-library", "Knowledge Library", "Upload and organize your knowledge sources.", position="bottom_center"),
        TourStep("conversations", "Your Conversations", "Review past conversations with your clones.", position="bottom_center"),
        TourStep("sidebar", "Sidebar", "Navigate between sections using the sidebar.", position="bottom_left"),
        TourStep("widget-setup", "Widget Setup", "Embed your clone on any website.", position="bottom_center"),
        TourStep("dashboard-complete", "You're All Set!", "You're ready to start using MyOwnClone.", position="bottom_center"),
    ],
)

PERSONA_TOUR = TourDefinition(
    id="persona",
    name="Persona Creation Tour",
    steps=[
        TourStep("persona-welcome", "Create Your First Persona", "Let's set up your AI persona.", position="bottom_center"),
        TourStep("persona-add-sources", "Add Knowledge Sources", "Upload documents to train your persona.", position="bottom_center"),
        TourStep("persona-auto-capture", "Auto-Capture Visitors", "Enable automatic visitor capture.", position="bottom_center"),
        TourStep("persona-customize-look", "Customize the Look", "Set avatar, colors, and theme.", position="bottom_center"),
        TourStep("persona-widget", "Add to Your Website", "Get the embed code for your site.", position="bottom_center"),
        TourStep("persona-complete", "Your Persona is Ready!", "Your persona is live and ready to help.", position="bottom_center"),
    ],
)

# Registry
TOURS: dict[str, TourDefinition] = {
    t.id: t for t in [ONBOARDING_TOUR, DASHBOARD_TOUR, PERSONA_TOUR]
}


def get_tour(tour_id: str) -> TourDefinition | None:
    return TOURS.get(tour_id)


def list_tours() -> list[TourDefinition]:
    return list(TOURS.values())

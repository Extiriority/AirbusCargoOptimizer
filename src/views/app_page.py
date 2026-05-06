from nicegui import ui

from .header_view import header_view
from .theme import apply_app_theme

APP_NAME = "Airbus Auto Cargo Organizer"

def create_app() -> None:
    apply_app_theme()

    with ui.column().classes("page gap-4"):
        header_view(APP_NAME)

    with ui.footer().classes("bg-transparent shadow-none"):
        with ui.element("div").classes("w-full max-w-[1500px] mx-auto px-3 pb-2"):
            with ui.row().classes(
                    "w-full items-center justify-between px-4 py-1.5 text-sm text-grey-8 bg-grey-1 rounded-t-xl shadow-2"):
                ui.label("ACO, Airbus Cargo Optimizer")
                ui.label("Built by Giang, Applied Quantum Technology MSc")
                ui.label("HvA - Hogeschool van Amsterdam")
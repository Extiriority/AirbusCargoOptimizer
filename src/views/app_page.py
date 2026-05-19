from nicegui import ui

from src.data.aircraft_data import test_aircraft_data
from src.data.container_data import test_container_list

from .cargo_capacity_view import cargo_capacity_length_view
from .header_view import header_view
from .theme import apply_app_theme

APP_NAME = "Airbus Auto Cargo Organizer"


def create_app() -> None:
    apply_app_theme()
    aircraft = test_aircraft_data()
    containers = test_container_list()

    with ui.column().classes("page gap-4"):
        header_view(APP_NAME)
        cargo_capacity_length_view(aircraft, containers)

    with ui.footer().classes("bg-transparent shadow-none"):
        with ui.element("div").classes("w-full max-w-[1500px] mx-auto px-3 pb-2"):
            with ui.row().classes(
                "w-full items-center justify-between px-4 py-1.5 text-sm text-grey-8 bg-grey-1 rounded-t-xl shadow-2"
            ):
                ui.label("ACO, Airbus Cargo Optimizer")
                ui.label("Built by Giang, Applied Quantum Technology MSc")
                ui.label("HvA - Hogeschool van Amsterdam")

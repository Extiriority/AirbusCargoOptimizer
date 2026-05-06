from datetime import datetime

from nicegui import ui

def header_view(app_name: str) -> None:
    with ui.row().classes("w-full items-center justify-between"):
        ui.label(app_name).classes("text-2xl font-bold")
        clock = ui.label().classes("text-sm text-grey-7")
        ui.timer(1.0, lambda: clock.set_text(f"{datetime.now():%X}"))

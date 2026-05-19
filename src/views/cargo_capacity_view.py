from typing import Sequence

from nicegui import ui

from src.controller.run_controller import optimize_cargo_loading
from src.models.aircraft_model import Aircraft
from src.models.container_model import Container

from .cargo_data_view import cargo_data_table, loaded_positions
from .cargo_loading_view import (
    available_cargo_options,
    can_fit_container,
    cargo_load_controls,
    cargo_loading_visual,
    find_container,
    loaded_container_ids,
)
from .cg_shear_view import cg_and_shear_view


def cargo_capacity_length_view(
    aircraft: type[Aircraft], containers: Sequence[Container]
) -> None:
    cargo_position_count = aircraft.cargo_capacity_length
    cargo_sample_count = aircraft.allocated_cargo_amount
    assignments: list[list[Container]] = [[] for _ in range(cargo_position_count)]

    with ui.card().classes("cargo-capacity-card w-full p-0 overflow-hidden"):
        _cargo_capacity_header(cargo_position_count, cargo_sample_count)

        @ui.refreshable
        def loading_visual() -> None:
            cargo_loading_visual(containers, assignments, cargo_sample_count)

        @ui.refreshable
        def cg_shear_visual() -> None:
            cg_and_shear_view(aircraft, assignments)

        @ui.refreshable
        def cargo_table() -> None:
            cargo_data_table(containers, loaded_positions(assignments))

        def refresh_loading_state() -> None:
            loaded_ids = loaded_container_ids(assignments)
            cargo_options = available_cargo_options(containers, loaded_ids)
            cargo_select.set_options(cargo_options)
            if cargo_select.value in loaded_ids or cargo_select.value not in cargo_options:
                cargo_select.set_value(next(iter(cargo_options), None))
            loading_visual.refresh()
            cg_shear_visual.refresh()
            cargo_table.refresh()

        def add_selected_cargo() -> None:
            container = find_container(containers, cargo_select.value)
            if container is None:
                ui.notify("Choose a cargo item first.", color="warning")
                return

            position_index = int(position_select.value) - 1
            if not can_fit_container(assignments[position_index], container):
                ui.notify(
                    f"Position {position_index + 1} is full for {container.container_type.name.title()} cargo.",
                    color="negative",
                )
                return

            assignments[position_index].append(container)
            ui.notify(
                f"Loaded cargo {container.container_id} into position {position_index + 1}.",
                color="positive",
            )
            refresh_loading_state()

        def reset_loading() -> None:
            for position in assignments:
                position.clear()
            ui.notify("Cargo loading cleared.", color="primary")
            refresh_loading_state()

        def optimize_loading() -> None:
            optimized_assignments = optimize_cargo_loading(aircraft, list(containers))
            for position, optimized_position in zip(assignments, optimized_assignments):
                position.clear()
                position.extend(optimized_position)
            payload_mass = sum(
                container.container_mass
                for position in assignments
                for container in position
            )
            ui.notify(f"Optimized loading: {payload_mass:,} kg payload.", color="positive")
            refresh_loading_state()

        with ui.element("div").classes("cargo-workspace-grid"):
            with ui.element("div").classes("cargo-plane-column"):
                loading_visual()
                cargo_select, position_select = cargo_load_controls(
                    containers,
                    cargo_position_count,
                    add_selected_cargo,
                    optimize_loading,
                    reset_loading,
                )
            with ui.element("div").classes("cargo-cg-column"):
                cg_shear_visual()
        cargo_table()


def _cargo_capacity_header(cargo_position_count: int, cargo_sample_count: int) -> None:
    with ui.element("div").classes("cargo-capacity-header"):
        with ui.column().classes("gap-1"):
            ui.label("Cargo Capacity Length").classes("card_title")
            ui.label("Visualized as the aircraft cargo capacity positions N.").classes(
                "text-sm text-grey-7"
            )
        with ui.row().classes("cargo-capacity-metrics"):
            _metric("N", f"{cargo_position_count}", "positions")
            _metric("n", f"{cargo_sample_count}", "cargo samples")


def _metric(label: str, value: str, caption: str) -> None:
    with ui.element("div").classes("cargo-metric"):
        ui.label(label).classes("cargo-metric-label")
        ui.label(value).classes("cargo-metric-value")
        ui.label(caption).classes("cargo-metric-caption")

from typing import Sequence

from nicegui import ui

from src.models.container_model import Container


def cargo_data_table(
    containers: Sequence[Container], loaded_positions: dict[int, int]
) -> None:
    columns = [
        {
            "name": "container_id",
            "label": "Cargo ID",
            "field": "container_id",
            "align": "left",
            "sortable": True,
        },
        {
            "name": "container_type",
            "label": "Type",
            "field": "container_type",
            "align": "left",
            "sortable": True,
        },
        {
            "name": "container_mass",
            "label": "Mass (kg)",
            "field": "container_mass",
            "align": "right",
            "sortable": True,
        },
        {
            "name": "status",
            "label": "Status",
            "field": "status",
            "align": "left",
            "sortable": True,
        },
    ]
    rows = [
        {
            "container_id": container.container_id,
            "container_type": container.container_type.name.title(),
            "container_mass": container.container_mass,
            "status": (
                f"Loaded in N{loaded_positions[container.container_id]}"
                if container.container_id in loaded_positions
                else "Waiting"
            ),
        }
        for container in containers
    ]

    with ui.element("section").classes("cargo-table-section w-full"):
        with ui.row().classes("cargo-table-header"):
            ui.label("Cargo Data").classes("card_title")
            ui.badge(f"{len(rows)} items", color="primary").classes("cargo-table-badge")

        ui.table(
            columns=columns,
            rows=rows,
            row_key="container_id",
            pagination={"rowsPerPage": 10},
        ).classes("cargo-data-table w-full").props("flat bordered dense").style(
            "width: 100%;"
        )


def loaded_positions(assignments: Sequence[Sequence[Container]]) -> dict[int, int]:
    return {
        container.container_id: index + 1
        for index, position in enumerate(assignments)
        for container in position
    }

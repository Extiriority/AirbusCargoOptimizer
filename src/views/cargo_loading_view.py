from typing import Callable, Sequence

from nicegui import ui

from src.models.container_model import Container
from src.models.enums import ContainerType


def cargo_loading_visual(
    containers: Sequence[Container],
    assignments: Sequence[Sequence[Container]],
    cargo_sample_count: int,
) -> None:
    loaded_ids = loaded_container_ids(assignments)
    cargo_position_count = len(assignments)
    ui.html(
        f"""
        <section class="cargo-loading-visual" aria-label="Loaded cargo layout">
            <div class="aircraft-shell">
                <div class="aircraft-nose"></div>
                <div class="cargo-deck" style="--cargo-slots: {cargo_position_count};">
                    <div class="cargo-slot-strip">{_build_loaded_slot_markup(assignments)}</div>
                    <div class="selected-cargo-length">
                        <span></span>
                    </div>
                </div>
                <div class="aircraft-tail"></div>
            </div>

            <div class="cargo-samples" aria-label="Cargo sample containers">
                <div class="cargo-samples-label">{cargo_sample_count} cargo sample items</div>
                <div class="cargo-samples-strip">{_build_cargo_sample_markup(containers, loaded_ids)}</div>
            </div>
        </section>
        """
    )


def cargo_load_controls(
    containers: Sequence[Container],
    cargo_position_count: int,
    on_add: Callable[[], None],
    on_optimize: Callable[[], None],
    on_reset: Callable[[], None],
) -> tuple[ui.select, ui.select]:
    with ui.element("section").classes("cargo-load-controls"):
        with ui.row().classes("cargo-load-header"):
            ui.label("Load Cargo Into Plane").classes("card_title")
            ui.label("Select a cargo item and the aircraft position to place it in.").classes(
                "text-sm text-grey-7"
            )
        with ui.row().classes("cargo-load-actions"):
            cargo_select = ui.select(
                available_cargo_options(containers, set()),
                label="Cargo item",
                value=containers[0].container_id if containers else None,
            ).classes("cargo-load-select")
            position_select = ui.select(
                list(range(1, cargo_position_count + 1)),
                label="Position N",
                value=1,
            ).classes("cargo-position-select")
            ui.button("Add", icon="add", on_click=on_add).props("unelevated")
            ui.button("Optimize", icon="auto_fix_high", on_click=on_optimize).props(
                "unelevated color=secondary"
            )
            ui.button("Reset", icon="restart_alt", on_click=on_reset).props(
                "flat color=dark"
            )

    return cargo_select, position_select


def available_cargo_options(
    containers: Sequence[Container], loaded_ids: set[int]
) -> dict[int, str]:
    return {
        container.container_id: (
            f"#{container.container_id} "
            f"{container.container_type.name.title()} "
            f"({container.container_mass} kg)"
        )
        for container in containers
        if container.container_id not in loaded_ids
    }


def find_container(
    containers: Sequence[Container], container_id: int | None
) -> Container | None:
    return next(
        (
            container
            for container in containers
            if container.container_id == container_id
        ),
        None,
    )


def can_fit_container(position: Sequence[Container], container: Container) -> bool:
    used_capacity = sum(_container_capacity(container_item) for container_item in position)
    return used_capacity + _container_capacity(container) <= 2


def loaded_container_ids(assignments: Sequence[Sequence[Container]]) -> set[int]:
    return {
        container.container_id
        for position in assignments
        for container in position
    }


def _container_capacity(container: Container) -> int:
    if container.container_type == ContainerType.HALF:
        return 1
    return 2


def _build_loaded_slot_markup(assignments: Sequence[Sequence[Container]]) -> str:
    if not assignments:
        return ""

    slot_width = 100 / len(assignments)
    markup = []
    for index, containers in enumerate(assignments):
        cargo_blocks = "".join(_build_loaded_cargo_markup(container) for container in containers)
        if not cargo_blocks:
            cargo_blocks = '<span class="cargo-empty-slot">Empty</span>'
        markup.append(
            f"""
            <span class="cargo-slot cargo-load-slot" style="width: {slot_width:.4f}%">
                <span class="cargo-slot-number">{index + 1}</span>
                <span class="cargo-slot-load">{cargo_blocks}</span>
            </span>
            """
        )
    return "".join(markup)


def _build_loaded_cargo_markup(container: Container) -> str:
    cargo_class = (
        "loaded-cargo loaded-cargo-half"
        if container.container_type == ContainerType.HALF
        else "loaded-cargo loaded-cargo-standard"
    )
    return f'<span class="{cargo_class}">#{container.container_id}</span>'


def _build_cargo_sample_markup(
    containers: Sequence[Container], loaded_ids: set[int]
) -> str:
    if not containers:
        return ""

    markup = []
    for container in containers:
        classes = "cargo-sample"
        if container.container_type == ContainerType.HALF:
            classes += " cargo-sample-half"
        if container.container_id in loaded_ids:
            classes += " cargo-sample-loaded"
        markup.append(f'<span class="{classes}">{container.container_id}</span>')
    return "".join(markup)

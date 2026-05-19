from typing import Sequence

from nicegui import ui

from src.models.aircraft_model import Aircraft
from src.models.container_model import Container


def cg_and_shear_view(
    aircraft: type[Aircraft], assignments: Sequence[Sequence[Container]]
) -> None:
    ui.html(_build_cg_and_shear_markup(aircraft, assignments))


def _build_cg_and_shear_markup(
    aircraft: type[Aircraft], assignments: Sequence[Sequence[Container]]
) -> str:
    positioned_containers = _positioned_containers(assignments)
    payload_mass = sum(container.container_mass for _, container in positioned_containers)
    left_payload_mass, right_payload_mass = _side_payload_masses(assignments)
    total_mass = aircraft.body_mass + payload_mass
    loaded_cg = (
        (
            aircraft.body_mass * aircraft.body_center_of_gravity
            + sum(container.container_mass * x for x, container in positioned_containers)
        )
        / total_mass
        if total_mass
        else aircraft.body_center_of_gravity
    )
    empty_cg_percent = _x_to_percent(aircraft.body_center_of_gravity)
    loaded_cg_percent = _x_to_percent(loaded_cg)
    min_cg_percent = _x_to_percent(aircraft.minimum_allowed_center_of_gravity)
    max_cg_percent = _x_to_percent(aircraft.maximum_allowed_center_of_gravity)
    target_cg_percent = _x_to_percent(aircraft.target_center_of_gravity)
    in_limits = (
        aircraft.minimum_allowed_center_of_gravity
        <= loaded_cg
        <= aircraft.maximum_allowed_center_of_gravity
    )
    payload_metric_class = (
        "cg-metric-over-limit"
        if payload_mass > aircraft.maximum_payload_mass
        else ""
    )
    maximum_shear_mass = getattr(aircraft, "maximum_shear_mass", 22000)
    left_metric_class = (
        "cg-side-over-limit" if left_payload_mass > maximum_shear_mass else ""
    )
    right_metric_class = (
        "cg-side-over-limit" if right_payload_mass > maximum_shear_mass else ""
    )
    limit_label = "Inside CG limits" if in_limits else "Outside CG limits"
    limit_class = "cg-status-ok" if in_limits else "cg-status-bad"
    shear_points = _build_shear_polyline(assignments)

    return f"""
    <section class="cg-shear-section" aria-label="Centre of gravity and shear visualization">
        <div class="cg-shear-header">
            <div>
                <div class="card_title">Centre of Gravity and Shear</div>
                <div class="cg-shear-subtitle">Only the x-coordinate is visualized; cargo masses are placed at their slot centres.</div>
            </div>
            <div class="cg-status {limit_class}">{limit_label}</div>
        </div>

        <div class="cg-axis-panel">
            <div class="cg-axis-label cg-axis-forward">forward x &lt; 0</div>
            <div class="cg-axis-label cg-axis-aft">aft x &gt; 0</div>
            <div class="cg-limit-zone" style="left: {min_cg_percent:.2f}%; width: {max_cg_percent - min_cg_percent:.2f}%;"></div>
            <div class="cg-axis-line"></div>
            <div class="cg-marker cg-min" style="left: {min_cg_percent:.2f}%;">x min</div>
            <div class="cg-marker cg-max" style="left: {max_cg_percent:.2f}%;">x max</div>
            <div class="cg-marker cg-target" style="left: {target_cg_percent:.2f}%;">target</div>
            <div class="cg-marker cg-empty" style="left: {empty_cg_percent:.2f}%;">empty</div>
            <div class="cg-marker cg-loaded" style="left: {loaded_cg_percent:.2f}%;">loaded</div>
        </div>

        <div class="cg-metrics">
            <div><span>x empty</span><strong>{aircraft.body_center_of_gravity:.3f}</strong></div>
            <div><span>x loaded</span><strong>{loaded_cg:.3f}</strong></div>
            <div class="{payload_metric_class}"><span>payload</span><strong>{payload_mass:,} kg</strong></div>
            <div><span>total mass</span><strong>{total_mass:,} kg</strong></div>
            <div class="cg-left-mass {left_metric_class}"><span>left / forward cargo</span><strong>{left_payload_mass:,} kg</strong></div>
            <div class="cg-right-mass {right_metric_class}"><span>right / aft cargo</span><strong>{right_payload_mass:,} kg</strong></div>
            <div><span>S0 max</span><strong>{maximum_shear_mass:,} kg</strong></div>
        </div>

        <div class="shear-panel">
            <div class="shear-title">Shear curve S(x)</div>
            <svg class="shear-svg" viewBox="0 0 100 44" preserveAspectRatio="none" role="img" aria-label="Shear curve">
                <line x1="0" y1="38" x2="100" y2="38" class="shear-axis"></line>
                <line x1="50" y1="4" x2="50" y2="40" class="shear-midline"></line>
                <polyline points="{shear_points}" class="shear-line"></polyline>
            </svg>
            <div class="shear-caption">Forward of x = 0 the curve accumulates loaded mass from the nose; aft of x = 0 it accumulates from the tail.</div>
        </div>
    </section>
    """


def _positioned_containers(
    assignments: Sequence[Sequence[Container]],
) -> list[tuple[float, Container]]:
    if not assignments:
        return []

    capacity_count = len(assignments)
    positioned = []
    for index, position in enumerate(assignments):
        x_position = -0.5 + ((index + 0.5) / capacity_count)
        for container in position:
            positioned.append((x_position, container))
    return positioned


def _side_payload_masses(assignments: Sequence[Sequence[Container]]) -> tuple[int, int]:
    if not assignments:
        return 0, 0

    middle = len(assignments) / 2
    left_mass = 0
    right_mass = 0
    for index, position in enumerate(assignments):
        position_mass = sum(container.container_mass for container in position)
        if index < middle:
            left_mass += position_mass
        else:
            right_mass += position_mass
    return left_mass, right_mass


def _x_to_percent(value: float) -> float:
    return min(max((value + 0.5) * 100, 0), 100)


def _build_shear_polyline(assignments: Sequence[Sequence[Container]]) -> str:
    if not assignments:
        return "0,38 100,38"

    slot_masses = [
        sum(container.container_mass for container in position)
        for position in assignments
    ]
    maximum = max(sum(slot_masses), 1)
    center_index = len(slot_masses) // 2
    points: list[tuple[float, float]] = []

    forward_running = 0
    for index in range(center_index):
        forward_running += slot_masses[index]
        x = ((index + 1) / len(slot_masses)) * 100
        y = 38 - (forward_running / maximum) * 30
        points.append((x, y))

    aft_running = 0
    aft_points: list[tuple[float, float]] = []
    for index in range(len(slot_masses) - 1, center_index - 1, -1):
        aft_running += slot_masses[index]
        x = (index / len(slot_masses)) * 100
        y = 38 - (aft_running / maximum) * 30
        aft_points.append((x, y))

    all_points = [(0, 38), *points, (50, 38), *reversed(aft_points), (100, 38)]
    return " ".join(f"{x:.2f},{y:.2f}" for x, y in all_points)

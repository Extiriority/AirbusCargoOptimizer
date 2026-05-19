from src.models.aircraft_model import Aircraft
from src.models.container_model import Container
from src.models.enums import ContainerType


def optimize_cargo_loading(
    aircraft: type[Aircraft], containers: list[Container]
) -> list[list[Container]]:
    """
    Run the full classical loading pipeline.

    This is the method the UI calls when the Optimise button is clicked. I implemented it
    as a classical baseline, so the app can produce a valid loading plan before adding any
    quantum or hybrid optimiser later.
    """
    selected_containers = _select_payload(aircraft, containers)
    return _arrange_for_center_of_gravity(aircraft, selected_containers)


def _select_payload(
    aircraft: type[Aircraft], containers: list[Container]
) -> list[Container]:
    """
    Select the heaviest useful subset of cargo under aircraft payload and slot capacity.

    This uses dynamic programming because the cargo weights are integer kg values and the
    aircraft has hard limits. I implemented it to avoid a greedy choice accidentally
    missing a better mass combination.
    """
    max_capacity_units = aircraft.cargo_capacity_length * 2
    max_payload_mass = aircraft.maximum_payload_mass
    states: dict[tuple[int, int], list[Container]] = {(0, 0): []}

    for container in containers:
        container_units = _container_capacity_units(container)
        next_states = dict(states)

        for (used_units, used_mass), selected in states.items():
            new_units = used_units + container_units
            new_mass = used_mass + container.container_mass
            if new_units > max_capacity_units or new_mass > max_payload_mass:
                continue

            key = (new_units, new_mass)
            if key not in next_states:
                next_states[key] = [*selected, container]

        states = next_states

    best_units, best_mass = max(
        states,
        key=lambda state: (
            state[1],
            -abs((state[0] / 2) - aircraft.cargo_capacity_length),
            -state[0],
        ),
    )
    return states[(best_units, best_mass)]


def _arrange_for_center_of_gravity(
    aircraft: type[Aircraft], containers: list[Container]
) -> list[list[Container]]:
    """
    Place the selected cargo into aircraft positions while respecting CG and shear goals.

    This is separate from payload selection because choosing which cargo to carry and
    deciding where to place it are different problems. I implemented this stage to make
    the visualisation produce a physically meaningful loading layout.
    """
    position_count = aircraft.cargo_capacity_length
    groups = _build_slot_groups(containers)
    assignments: list[list[Container]] = [[] for _ in range(position_count)]
    if not groups:
        return assignments

    target_cargo_moment = _target_cargo_moment(aircraft, containers)
    slot_centers = _slot_centers(position_count)
    right_side_groups = _choose_right_side_groups(
        aircraft, groups, target_cargo_moment, slot_centers
    )
    right_group_ids = {id(group) for group in right_side_groups}
    left_side_groups = [group for group in groups if id(group) not in right_group_ids]
    left_positions = list(range(position_count // 2))
    right_positions = list(range(position_count // 2, position_count))

    for group, position_index in _place_groups_on_side(
        left_side_groups, left_positions, slot_centers, target_cargo_moment
    ):
        assignments[position_index].extend(group)
    for group, position_index in _place_groups_on_side(
        right_side_groups, right_positions, slot_centers, target_cargo_moment
    ):
        assignments[position_index].extend(group)

    _improve_assignment_by_swapping(
        assignments, target_cargo_moment, slot_centers, _maximum_shear_mass(aircraft)
    )
    return assignments


def _choose_right_side_groups(
    aircraft: type[Aircraft],
    groups: list[list[Container]],
    target_cargo_moment: float,
    slot_centers: list[float],
) -> list[list[Container]]:
    """
    Decide which cargo groups should go on the aft/right side of the aircraft.

    The shear curve has its maximum at x = 0, so each side must stay below the shear
    limit. I implemented this dynamic-programming split to keep right/aft mass close to
    the CG target without exceeding S0 max.
    """
    shear_limit = _maximum_shear_mass(aircraft)
    half_position_count = len(slot_centers) // 2
    max_right_groups = len(slot_centers) - half_position_count
    total_payload_mass = sum(_group_mass(group) for group in groups)
    right_target_mass = min(
        shear_limit,
        max(0, total_payload_mass / 2 + target_cargo_moment),
    )
    states: dict[tuple[int, int], list[list[Container]]] = {(0, 0): []}

    for group in groups:
        group_mass = _group_mass(group)
        next_states = dict(states)
        for (group_count, mass), selected_groups in states.items():
            new_group_count = group_count + 1
            new_mass = mass + group_mass
            if new_group_count > max_right_groups or new_mass > shear_limit:
                continue
            next_states[(new_group_count, new_mass)] = [*selected_groups, group]
        states = next_states

    _, best_mass = min(
        states,
        key=lambda state: (
            abs(state[1] - right_target_mass),
            abs((total_payload_mass - state[1]) - state[1]),
        ),
    )
    best_key = min(
        [key for key in states if key[1] == best_mass],
        key=lambda key: abs(key[0] - max_right_groups),
    )
    return states[best_key]


def _place_groups_on_side(
    groups: list[list[Container]],
    positions: list[int],
    slot_centers: list[float],
    target_cargo_moment: float,
) -> list[tuple[list[Container], int]]:
    """
    Assign cargo groups to concrete positions on one side of the aircraft.

    Heavier groups are placed according to the desired moment direction. I implemented
    this to make the arrangement help the loaded centre of gravity instead of simply
    filling positions from left to right.
    """
    sorted_groups = sorted(groups, key=_group_mass, reverse=True)
    sorted_positions = sorted(
        positions,
        key=lambda index: slot_centers[index],
        reverse=target_cargo_moment >= 0,
    )
    return list(zip(sorted_groups, sorted_positions))


def _build_slot_groups(containers: list[Container]) -> list[list[Container]]:
    """
    Convert cargo items into position-sized groups.

    Standard cargo uses one full N position, while two half cargo items can share one N.
    I implemented this grouping so the rest of the optimiser can reason in aircraft
    positions instead of individual half-slot fragments.
    """
    standard_groups = [
        [container]
        for container in containers
        if container.container_type == ContainerType.STANDARD
    ]
    half_containers = [
        container for container in containers if container.container_type == ContainerType.HALF
    ]
    half_containers.sort(key=lambda container: container.container_mass, reverse=True)
    half_groups = [
        half_containers[index : index + 2]
        for index in range(0, len(half_containers), 2)
    ]
    return [*standard_groups, *half_groups]


def _improve_assignment_by_swapping(
    assignments: list[list[Container]],
    target_cargo_moment: float,
    slot_centers: list[float],
    shear_limit: int,
) -> None:
    """
    Locally improve the arrangement by swapping occupied positions.

    The first placement is a good deterministic starting point, but swaps can reduce the
    distance from the target cargo moment. I implemented this as a simple local search
    while rejecting swaps that break the shear constraint.
    """
    improved = True
    while improved:
        improved = False
        current_error = _cargo_moment_error(assignments, target_cargo_moment, slot_centers)

        for left in range(len(assignments)):
            for right in range(left + 1, len(assignments)):
                assignments[left], assignments[right] = assignments[right], assignments[left]
                if _side_shear_violation(assignments, shear_limit) > 0:
                    assignments[left], assignments[right] = assignments[right], assignments[left]
                    continue
                swap_error = _cargo_moment_error(
                    assignments, target_cargo_moment, slot_centers
                )
                if swap_error < current_error:
                    current_error = swap_error
                    improved = True
                    continue
                assignments[left], assignments[right] = assignments[right], assignments[left]


def _cargo_moment_error(
    assignments: list[list[Container]],
    target_cargo_moment: float,
    slot_centers: list[float],
) -> float:
    """
    Measure how far the current cargo layout is from the target cargo moment.

    This is the score used by the swap improver. I implemented it to give the layout
    step a clear objective: move the loaded aircraft CG closer to the target.
    """
    moment = sum(
        _group_mass(position) * slot_centers[index]
        for index, position in enumerate(assignments)
    )
    return abs(moment - target_cargo_moment)


def _target_cargo_moment(
    aircraft: type[Aircraft], containers: list[Container]
) -> float:
    """
    Compute the cargo moment needed to reach the aircraft target centre of gravity.

    The empty aircraft already has its own mass and CG, so the cargo must compensate for
    that existing moment. I implemented this helper to translate the CG target into the
    moment value used by the placement algorithm.
    """
    payload_mass = sum(container.container_mass for container in containers)
    return (
        aircraft.target_center_of_gravity * (aircraft.body_mass + payload_mass)
        - aircraft.body_mass * aircraft.body_center_of_gravity
    )


def _slot_centers(position_count: int) -> list[float]:
    """
    Return the x-coordinate of each cargo position centre.

    Containers are modelled as point masses at their geometrical centre, matching the
    problem statement. I implemented this helper so all moment and shear calculations use
    one consistent coordinate system from -L/2 to L/2.
    """
    return [
        -0.5 + ((index + 0.5) / position_count)
        for index in range(position_count)
    ]


def _group_mass(containers: list[Container]) -> int:
    """
    Sum the mass of a cargo group or loaded position.

    I implemented this tiny helper because the optimiser repeatedly compares grouped
    cargo masses during splitting, placing, swapping, and shear checks.
    """
    return sum(container.container_mass for container in containers)


def _container_capacity_units(container: Container) -> int:
    """
    Convert cargo type into half-position capacity units.

    A standard container takes two half-units, while a half-container takes one. I
    implemented this to express both cargo types with integer capacity values for dynamic
    programming.
    """
    if container.container_type == ContainerType.HALF:
        return 1
    return 2


def _maximum_shear_mass(aircraft: type[Aircraft]) -> int:
    """
    Read the maximum centre shear mass for one side of the aircraft.

    The problem data uses S0 max = 22.000 kg. I implemented this helper to allow different aircraft to specify their own shear limits.
    """
    return getattr(aircraft, "maximum_shear_mass", 22000)


def _side_shear_violation(assignments: list[list[Container]], shear_limit: int) -> int:
    """
    Calculate how much the layout exceeds the left/right shear limit.

    This protects the triangular shear constraint shown in the assignment. I implemented
    it so manual checks and optimizer swaps can reject layouts where one side carries too
    much cargo mass.
    """
    middle = len(assignments) // 2
    left_mass = sum(_group_mass(position) for position in assignments[:middle])
    right_mass = sum(_group_mass(position) for position in assignments[middle:])
    return max(left_mass - shear_limit, right_mass - shear_limit, 0)

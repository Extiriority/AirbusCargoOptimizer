from src.models.aircraft_model import Aircraft

def test_aircraft_data() -> type[Aircraft]:
    aircraft = Aircraft
    aircraft.maximum_payload_mass = 40000
    aircraft.body_mass = 120000
    aircraft.cargo_capacity_length = 20
    aircraft.allocated_cargo_amount = 30
    aircraft.body_center_of_gravity = -0.05
    aircraft.minimum_allowed_center_of_gravity = -0.1
    aircraft.maximum_allowed_center_of_gravity = 0.2
    aircraft.target_center_of_gravity = 0.1
    aircraft.maximum_shear_mass = 22000

    return aircraft

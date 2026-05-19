from dataclasses import dataclass

@dataclass
class Aircraft:
    body_mass: int # We
    maximum_payload_mass: int # Wp
    total_mass: int # W
    cargo_capacity_length: int # N
    allocated_cargo_amount: int # n
    body_center_of_gravity: float # X ecg
    loaded_center_of_gravity: float # X cg
    minimum_allowed_center_of_gravity: float # X min cg
    maximum_allowed_center_of_gravity: float # X max cg
    target_center_of_gravity: float # X tcg
    maximum_shear_mass: int # S0 max

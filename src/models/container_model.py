from dataclasses import dataclass

from .enums import ContainerType


@dataclass
class Container:
    """
    Container model representing a cargo container with its unique ID, type, and mass.
    """
    container_id: int
    container_type: ContainerType
    container_mass: int

    @property
    def container_mass(self) -> int:
        """Mass of the container in kg. Always non-negative."""
        return getattr(self, "_container_mass")

    @container_mass.setter
    def container_mass(self, value: int) -> None:
        # Reject booleans which are a subclass of int
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("container_mass must be an int (not bool)")
        if value < 0:
            raise ValueError("container_mass must be non-negative")
        self._container_mass = value


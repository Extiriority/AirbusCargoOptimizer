from typing import List

from src.models.container_model import Container
from src.models.enums import ContainerType

def test_container_list() -> List[Container]:
    return [
        Container(1, ContainerType.STANDARD, 2134),
        Container(2, ContainerType.STANDARD, 3455),
        Container(3, ContainerType.STANDARD, 1866),
        Container(4, ContainerType.STANDARD, 1699),
        Container(5, ContainerType.STANDARD, 3500),
        Container(6, ContainerType.STANDARD, 3332),
        Container(7, ContainerType.STANDARD, 2578),
        Container(8, ContainerType.STANDARD, 2315),
        Container(9, ContainerType.STANDARD, 1888),
        Container(10, ContainerType.STANDARD, 1786),
        Container(11, ContainerType.STANDARD, 3277),
        Container(12, ContainerType.STANDARD, 2987),
        Container(13, ContainerType.STANDARD, 2534),
        Container(14, ContainerType.STANDARD, 2111),
        Container(15, ContainerType.STANDARD, 2607),
        Container(16, ContainerType.STANDARD, 1566),
        Container(17, ContainerType.STANDARD, 1765),
        Container(18, ContainerType.STANDARD, 1946),
        Container(19, ContainerType.STANDARD, 1732),
        Container(20, ContainerType.STANDARD, 1641),
        Container(21, ContainerType.HALF, 1800),
        Container(22, ContainerType.HALF, 986),
        Container(23, ContainerType.HALF, 873),
        Container(24, ContainerType.HALF, 1764),
        Container(25, ContainerType.HALF, 1239),
        Container(26, ContainerType.HALF, 1487),
        Container(27, ContainerType.HALF, 769),
        Container(28, ContainerType.HALF, 836),
        Container(29, ContainerType.HALF, 659),
        Container(30, ContainerType.HALF, 765),
    ]
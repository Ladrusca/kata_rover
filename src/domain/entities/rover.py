from dataclasses import dataclass
from src.domain.value_objects.direction import Direction


@dataclass
class Rover:

    coord_x: float
    coord_y: float
    direction: str

    def __init__(self, coord_x: float, coord_y: float, direction: Direction) -> None:
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.direction = direction

    def move(self, coord_x: float, coord_y: float) -> None:
        self.coord_x += coord_x
        self.coord_y += coord_y

    def turn(self, direction: str) -> None:
        self.direction = direction

    def set_origin_point(
        self, coord_x: float, coord_y: float, direction: Direction
    ) -> None:
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.direction = direction

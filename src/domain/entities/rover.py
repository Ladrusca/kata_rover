from dataclasses import dataclass


@dataclass
class Rover:

    def __init__(self, coord_x: float, coord_y: float, direction: str) -> None:
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.direction = direction

    coord_x: float
    coord_y: float
    direction: str

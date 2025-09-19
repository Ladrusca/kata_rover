from src.domain.value_objects.direction import Direction
from src.ports.primary.irover_manager import IRoverManager
from src.domain.entities.rover import Rover
from src.domain.services.movement_rules_service import MovementRulesService


class RoverManager(IRoverManager):

    def __init__(self, rover: Rover):
        self.rover = rover

    def set_origin_point(
        self, coord_x: float, coord_y: float, direction: Direction
    ) -> None:
        self.rover.set_origin_point(coord_x, coord_y, direction)

    def move_rover(self, command_list: list) -> None:
        for movement in command_list:
            MovementRulesService.apply_rule(self.rover, movement)

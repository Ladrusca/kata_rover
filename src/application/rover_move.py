from src.ports.primary.irover_move import IRoverMove
from src.domain.entities.rover import Rover
from src.domain.services.movement_rules_service import MovementRulesService


class RoverMove(IRoverMove):

    def set_origin_point(self, coord_x: float, coord_y: float, direction: str) -> None:

        rover = Rover(coord_x=coord_x, coord_y=coord_y, direction=direction)

    def move_rover(self, rover: Rover, command_list: list) -> None:

        for movement in command_list:
            direction_x, directiony, new_direction = MovementRulesService.get_rule(rover.direction, movement)

            rover.coord_x += direction_x
            rover.coord_y += directiony

            if new_direction:
                rover.direction = new_direction

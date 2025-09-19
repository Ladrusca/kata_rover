from src.ports.primary.irover_move import IRoverMove
from src.domain.entities.rover import Rover
from src.domain.value_objects.position import Position
from src.domain.value_objects.movement import Movement


class RoverMove(IRoverMove):

    def set_origin_point(self, coord_x: float, coord_y: float, direction: str) -> None:

        rover = Rover(coord_x=coord_x, coord_y=coord_y, direction=direction)

    def move_rover(self, rover: Rover, command_list: list) -> None:

        for movement in command_list:

            if rover.direction == Position.N:
                if movement == Movement.F:
                    rover.coord_y += 1

                elif movement == Movement.B:
                    rover.coord_y -= 1
                elif movement == Movement.L:
                    rover.direction = Position.W

                elif movement == Movement.R:
                    rover.direction = Position.E

            elif rover.direction == Position.S:
                if movement == Movement.F:
                    rover.coord_y -= 1

                elif movement == Movement.B:
                    rover.coord_y += 1
                elif movement == Movement.L:
                    rover.direction = Position.E

                elif movement == Movement.R:
                    rover.direction = Position.W

            elif rover.direction == Position.W:
                if movement == Movement.F:
                    rover.coord_x -= 1

                elif movement == Movement.B:
                    rover.coord_x += 1

                elif movement == Movement.L:
                    rover.direction = Position.S

                elif movement == Movement.R:
                    rover.direction = Position.N

            elif rover.direction == Position.E:
                if movement == Movement.F:
                    rover.coord_x += 1

                elif movement == Movement.B:
                    rover.coord_x -= 1
                elif movement == Movement.L:
                    rover.direction = Position.N

                elif movement == Movement.R:
                    rover.direction = Position.S

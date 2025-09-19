from src.domain.value_objects.movement import Movement
from src.domain.value_objects.direction import Direction
from src.domain.entities.rover import Rover


class MovementRulesService:
    RULES = {
        Direction.N: {
            Movement.F: lambda r: r.move(0, 1),
            Movement.B: lambda r: r.move(0, -1),
            Movement.L: lambda r: r.turn(Direction.W),
            Movement.R: lambda r: r.turn(Direction.E),
        },
        Direction.S: {
            Movement.F: lambda r: r.move(0, -1),
            Movement.B: lambda r: r.move(0, 1),
            Movement.L: lambda r: r.turn(Direction.E),
            Movement.R: lambda r: r.turn(Direction.W),
        },
        Direction.W: {
            Movement.F: lambda r: r.move(-1, 0),
            Movement.B: lambda r: r.move(1, 0),
            Movement.L: lambda r: r.turn(Direction.S),
            Movement.R: lambda r: r.turn(Direction.N),
        },
        Direction.E: {
            Movement.F: lambda r: r.move(1, 0),
            Movement.B: lambda r: r.move(-1, 0),
            Movement.L: lambda r: r.turn(Direction.N),
            Movement.R: lambda r: r.turn(Direction.S),
        },
    }

    @classmethod
    def apply_rule(cls, rover: Rover, movement: Movement):
        action = cls.RULES.get(rover.direction, {}).get(movement)

        if not action:
            raise NotImplementedError

        action(rover)

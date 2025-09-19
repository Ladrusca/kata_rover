from src.domain.value_objects.movement import Movement
from src.domain.value_objects.position import Position

class MovementRulesService:
    RULES = {
        (Position.N, Movement.F): (0, 1, None),
        (Position.S, Movement.F): (0, -1, None),
        (Position.E, Movement.F): (1, 0, None),
        (Position.W, Movement.F): (-1, 0, None),

        (Position.N, Movement.B): (0, -1, None),
        (Position.S, Movement.B): (0, 1, None),
        (Position.E, Movement.B): (-1, 0, None),
        (Position.W, Movement.B): (1, 0, None),

        (Position.N, Movement.L): (0, 0, Position.W),
        (Position.S, Movement.L): (0, 0, Position.E),
        (Position.E, Movement.L): (0, 0, Position.N),
        (Position.W, Movement.L): (0, 0, Position.S),

        (Position.N, Movement.R): (0, 0, Position.E),
        (Position.S, Movement.R): (0, 0, Position.W),
        (Position.E, Movement.R): (0, 0, Position.S),
        (Position.W, Movement.R): (0, 0, Position.N),
    }

    @classmethod
    def get_rule(cls, direction: Position, movement: Movement):
        return cls.RULES[(direction, movement)]

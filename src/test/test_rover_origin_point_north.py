from src.application.rover_move import RoverMove
from src.domain.entities.rover import Rover
from src.domain.value_objects.position import Position
from src.domain.value_objects.movement import Movement
import pytest


@pytest.fixture
def rover():
    rover = RoverMove()

    rover.set_origin_point(25, 30, Position.N)

    return rover


@pytest.fixture
def rover_entity():
    return Rover(25, 30, Position.N)


def test_get_starting_points(rover):

    assert rover


def test_move_rover_forward(rover, rover_entity):

    command_list = [Movement.F]

    rover.move_rover(rover_entity, command_list)

    assert rover_entity.coord_y == 31


def test_move_rover_backward(rover, rover_entity):

    command_list = [Movement.B]

    rover.move_rover(rover_entity, command_list)

    assert rover_entity.coord_y == 29


def test_move_rover_turn_left(rover, rover_entity):

    command_list = [Movement.L]

    rover.move_rover(rover_entity, command_list)

    assert rover_entity.direction == Position.W


def test_move_rover_turn_right(rover, rover_entity):

    command_list = [Movement.R]

    rover.move_rover(rover_entity, command_list)

    assert rover_entity.direction == Position.E


def test_move_random(rover, rover_entity):

    command_list = [
        Movement.F,
        Movement.F,
        Movement.R,
        Movement.B,
        Movement.L,
        Movement.F,
        Movement.F,
        Movement.F,
        Movement.L,
        Movement.B,
    ]

    rover.move_rover(rover_entity, command_list)

    assert rover_entity.coord_x == 25
    assert rover_entity.coord_y == 35
    assert rover_entity.direction == Position.W

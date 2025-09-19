from src.domain.value_objects.direction import Direction
from src.domain.value_objects.movement import Movement
import pytest


@pytest.fixture
def rover_service(clean_rover_service):
    clean_rover_service.rover.coord_x = 25
    clean_rover_service.rover.coord_y = 30
    clean_rover_service.rover.direction = Direction.N

    return clean_rover_service


def test_move_rover_forward(rover_service):

    command_list = [Movement.F]

    rover_service.move_rover(command_list)

    assert rover_service.rover.coord_y == 31


def test_move_rover_backward(rover_service):

    command_list = [Movement.B]

    rover_service.move_rover(command_list)

    assert rover_service.rover.coord_y == 29


def test_move_rover_turn_left(rover_service):

    command_list = [Movement.L]

    rover_service.move_rover(command_list)

    assert rover_service.rover.direction == Direction.W


def test_move_rover_turn_right(rover_service):

    command_list = [Movement.R]

    rover_service.move_rover(command_list)

    assert rover_service.rover.direction == Direction.E


def test_move_random(rover_service):

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

    rover_service.move_rover(command_list)

    assert rover_service.rover.coord_x == 25
    assert rover_service.rover.coord_y == 35
    assert rover_service.rover.direction == Direction.W

from src.domain.value_objects.direction import Direction
import pytest


@pytest.fixture
def rover_service(clean_rover_service):
    return clean_rover_service


def test_get_starting_points(rover_service):

    new_coord_x = 50
    new_coord_y = 10
    new_direction = Direction.N

    rover_service.set_origin_point(new_coord_x, new_coord_y, new_direction)

    assert rover_service.rover.coord_x == new_coord_x
    assert rover_service.rover.coord_y == new_coord_y
    assert rover_service.rover.direction == new_direction

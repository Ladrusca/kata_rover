from src.application.rover_manager import RoverManager
from src.domain.value_objects.direction import Direction
from src.domain.entities.rover import Rover
import pytest


@pytest.fixture
def clean_rover_service():
    rover = Rover(0, 0, Direction.N)
    return RoverManager(rover)

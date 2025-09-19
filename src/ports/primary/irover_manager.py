from abc import ABC, abstractmethod
from src.domain.value_objects.direction import Direction


class IRoverManager(ABC):

    @abstractmethod
    def set_origin_point(
        self, coord_x: float, coord_y: float, direction: Direction
    ) -> None:
        """Set origin point"""

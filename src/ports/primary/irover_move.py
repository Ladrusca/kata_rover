from abc import ABC, abstractmethod


class IRoverMove(ABC):

    @abstractmethod
    def set_origin_point(self, coord_x: float, coord_y: float, direction: str) -> None:
        """Set origin point"""

"""This module contains the inteface for the Graph"""

from abc import ABC, abstractmethod

class GraphInterface(ABC):
    """Defines the blueprint for the Graphs classes"""
    @abstractmethod
    def __init__(self, num_vertices: int) -> None:
        super().__init__()

    @abstractmethod
    def add_edge(v1: int, v2: int) -> None:
        pass

    @abstractmethod
    def is_adjacent(v1: int, v2: int) -> bool:
        pass

    @abstractmethod
    def return_adjacent(v: int) -> list[int]:
        pass

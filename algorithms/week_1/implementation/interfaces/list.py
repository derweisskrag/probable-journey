"""This module provides blueprint for LinkedLists"""

from abc import ABC, abstractmethod
from enum import Enum

class Position(Enum):
    """Provides navigation accross the Linked List."""
    START="START"
    MIDDLE="MIDDLE"
    END="END"


class AbstractedNode:
    """Represents the node of the list"""
    def __init__(self, data: int) -> None:
        """Initializes the node of the list.
        
        Args:
            data (int): the value in the node
        """


    @property
    def data(self) -> int:
        """Returns the value of the node."""


    @data.setter
    def data(self, value: int) -> None:
        """Sets a value to the node."""


class AbstractedLinkedList(ABC):
    """Blueprint for Linked lists"""
    def __init__(self, head: AbstractedNode = None) -> None:
        """Initializes the list.

        Args:
            head (Node): the first node of the list, located at the start.
                By default, it is of None type.
        """


    @abstractmethod
    def append_to_front(self, data: int) -> None:
        """Adds node to the front of the list. 

        Args:
            data (int): data in the node.
        """

    @abstractmethod
    def append_to_middle(self, data: int) -> None:
        """Adds node to the middle of the list.
        
        Args:
            data (int): data in the node.
        """


    @abstractmethod
    def append_to_end(self, data: int) -> None:
        """Adds node to the end of the list. 

        Args:
            data (int): data in the node.
        """


    @abstractmethod
    def insert_node(self, data: int, position: Position | int) -> None:
        """Adds node to a specific position of the list.

        Args:
            data (int): data in the node,
            position (Positio | int): a position of the node in the list.
        """


    @abstractmethod
    def delete_head(self) -> AbstractedNode:
        """Deletes the first node of the list (head) and returns it.

        Returns:
            head (Node): the head of the list.
        """


    @abstractmethod
    def delete_tail(self) -> AbstractedNode:
        """Deletes the last node of the list (tail) and returns it.

        Returns:
            tail (Node): the tail of the list.
        """


    @abstractmethod
    def delete_node(self, position: Position | int) -> AbstractedNode:
        """Deletes a node at the specified position.

        Args:
            position (Position | int): a position of the node in the list.
        """


    @abstractmethod
    def update_list(self) -> None:
        """Updates the list: keeps track of the tail, head nodes.
        """


    @abstractmethod
    def compute_length(self) -> int:
        """Computes the length of the list.
        """


    @property
    def head(self) -> AbstractedNode:
        """Returns the head."""


    @head.setter
    def head(self, node: AbstractedNode) -> None:
        """Sets a value to the head."""


    @property
    def tail(self) -> AbstractedNode:
        """Returns the tail."""


    @tail.setter
    def tail(self, node: AbstractedNode) -> None:
        """Sets a value to the tail."""

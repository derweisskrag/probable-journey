"""This module contains utility class"""

from implementation.linked_list import LinkedList
from implementation.circular_linked_list import CircularLinkedList
from implementation.doubly_linked_list import DoublyLinkedList

class Utils:
    """Utility class"""
    def __init__(self, linked_list: LinkedList | CircularLinkedList | DoublyLinkedList) -> None:
        """Initialization of the class"""
        self._linked_list = linked_list


    def remove_duplicates(self) -> None:
        """Removes duplicates from the list."""

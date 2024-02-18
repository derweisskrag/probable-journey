"""This module contains the doubly-linked list."""

class Node:
    """Reprenests the node of the doubly-linked list."""
    def __init__(self, data: int) -> None:
        """Initialization of the node of doubly-linked list."""
        self._data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """Represents the DoublyLinkedList"""
    def __init__(self, head: Node) -> None:
        """Initialization of the doubly-linked list."""

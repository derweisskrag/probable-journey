"""This module contains the doubly-linked list."""

from functools import lru_cache
from enum import Enum

class Direction(Enum):
    """Defines the direction where to traverse the list."""
    FORWARDS=1
    BACKWARDS=-1


class Node:
    """Reprenests the node of the doubly-linked list."""
    def __init__(self, data: int) -> None:
        """Initialization of the node of doubly-linked list."""
        self._data = data
        self.next = None
        self.prev = None


    @property
    def data(self) -> int:
        """Retrieves the value of the node"""
        return self._data  


    @data.setter
    def data(self, value: int) -> None:
        """Sets a new value to the node."""
        self._data = value


    def __repr__(self) -> str:
        return f"Node(data={self.data})"


class DoublyLinkedList:
    """Represents the DoublyLinkedList."""
    def __init__(self, head: Node) -> None:
        """Initialization of the doubly-linked list."""
        self._head = head if head else None
        self._tail = head


    @property
    def head(self) -> Node:
        """Retrieves the head."""
        return self._head


    @head.setter
    def head(self, node: Node) -> None:
        """Sets the node to the head."""
        self._head = node


    @property
    def tail(self) -> Node:
        """Retrieves the head."""
        return self._tail


    @tail.setter
    def tail(self, node: Node) -> None:
        """Sets the node to the head."""
        self._tail = node


    def traverse(self) -> Node:
        """Generator function.
        
        Returns:
            node (Node): the node of the list.
        """
        current = self.head

        while current:
            yield current
            current = current.next


    def display(self) -> None:
        """Displays the doubly-linked list."""
        for node in self.traverse():
            print(node, end="<-->" if node.next else "")


    def has_head(self) -> bool:
        """Checks if the head exists"""
        return self.head is not None


    def append_front(self, data: int) -> None:
        """Adds the node to the front.

        Args:
            data (int): the data in the node.
        """
        # position == 0 is the beginning
        self.insert_node(data, 0)


    def append_end(self, data: int) -> None:
        """Adds the node to the end of the list.
        
        Args:
            data (int): data in the node.
        """
        self.insert_node(data, self.compute_length())

    
    def insert_node(self, data: int, position: int) -> None:
        """Adds the node at the specified position.
        
        Args:
            data (int): the data in the node.

        """

        if not self.has_head():
            self.head = Node(data)
        
        # create new_node
        new_node = Node(data)

        # process edge cases, right?
        if position == 0:
            # append to front
            new_node.next = self.head
            self.head = new_node

            # balance
            self.update_list()

        elif position == self.compute_length():
            # append to end
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            # append the node at the index
            for index, current in enumerate(self.traverse()):
                if index == position - 1:
                    # add the node
                    new_node.next = current.next
                    new_node.prev = current

                    if current.next is not None:
                        current.next.prev = new_node

                    current.next = new_node


    def add(self, data: int, direction: Direction) -> None:
        """Adds the node to the linked list from
        
        Args:
            data (int): the data in the node.
            direction (Direction): defines the traversal direction.
        """

        if direction.value == 1:
            # forward
            self.insert_node(data, 2) # 1, 2, ... , len(DoublyLinkedList)
        elif direction.value == -1:
            # backwards
            self.insert_node(data, self.compute_length() - 1)
        else:
            raise TypeError(f"Invalid type: '{direction}'! Should be an int of either '1' or '-1'.")


    def delete_head(self) -> Node:
        """Deletes the head.
        
        Returns:
            head (Node): the head of the linked list.
        """
        self.delete_node(1)

    
    def delete_tail(self) -> Node:
        """Deletes the tail.
        
        Returns:
            tail (Node): the tail of the linked list.
        """
        self.delete_node(self.compute_length())


    def delete_node(self, position: int) -> Node:
        """Deletes the node at the specified index.
        
        Args:
            position (int): the index at which the node is located in the linked list.

        Returns:
            node_to_delete (Node): node to be deleted from the linked list.
        """
        # edge cases
        if position == 1:
            # delete the head
            node_to_delete = self.head
            self.head = self.head.next
            return node_to_delete
        elif position == self.compute_length():
            # delete the tail
            node_to_delete = self.tail
            self.tail = self.tail.prev
            return node_to_delete
        else:
            # delete the node at the position
            # start from 1
            for index, current in enumerate(self.traverse(), start = 1):
                if index == position - 1:
                    # current is the node before to delete
                    node_to_delete = current.next
                    current.next = node_to_delete.next
                    
                    if node_to_delete.next is not None: # is not tail
                        node_to_delete.next.prev = current

                    return node_to_delete


    @lru_cache(maxsize=100)
    def compute_length(self) -> int:
        """Computes the length of the list.
        
        Returns:
            length (int): the length of the doubly-linked list.
        """
        return len([node for node in self.traverse()])
    

    def update_list(self) -> None:
        """Checks if tail is valid"""
        for index, node in enumerate(self.traverse()):
            if index == self.compute_length(): # last element
                self.tail = node


def create_mock_linked_list(data: list[int]):
    """Creates the mock linked list.
        
    Args:
        data (list[int]): the list of integers, representing
            node's data to be added to the linked list.
    """

    doubly_linked_list = DoublyLinkedList(Node(data[0]))

    for index, value in enumerate(data):
        if index == 0:
            continue
        doubly_linked_list.add(Node(value), 1)

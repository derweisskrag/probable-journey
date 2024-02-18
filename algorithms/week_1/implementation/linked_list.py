"""This modules contains the linked list"""

from typing import override

from abstracted_list import AbstractedLinkedList, AbstractedNode, Position

class Node(AbstractedNode):
    """Represents the node of the linked list."""
    def __init__(self, data: int) -> None:
        """This class represents the node used in
        LinkedList data structure.

        Args:
            data (int): an integer.
        """

        # must be an integer
        assert isinstance(data, int), f"The data {data} must be an integer"

        # call super
        super().__init__(data)

        # instantiate
        self._data = data
        self.next = None # link to the next node


    @property
    def data(self):
        """Retrieves the data of the node."""
        return self._data


    def __repr__(self) -> str:
        return f"Node(data={self._data})"


    def __str__(self) -> str:
        return f"Node(data={self._data})"


    def __eq__(self, other) -> bool:
        return self.data == other.data


class LinkedList(AbstractedLinkedList):
    """Represents linked-list."""
    def __init__(self, head: Node = None) -> None:
        """Initializes the linked list.

        Args:
            head (Node): a starting node to create
                a linked list.
        """

        # call the super
        super().__init__(head)

        self._head = None if not head else head
        self._tail = None
        self._test_values: list[int] = [90, 80, 60, 50]


    @property
    def get_test_values(self) -> list[int]:
        """Get the test values to create a mock linked list.
        """
        return self._test_values


    @property
    def head(self) -> Node:
        """Retrieve the head of the linked list.
        """
        return self._head


    @head.setter
    def head(self, node: Node) -> None:
        """Sets the head value to the head.

        Args:
            node (Node): a node to insert.
        """

        # set the head to a node
        self._head = node


    @property
    def tail(self) -> Node:
        """Retrieve the last node of the list."""
        return self._tail


    @tail.setter
    def tail(self, node: Node) -> None:
        """Sets a node to the tail."""
        if not isinstance(node, Node):
            raise TypeError(f"Cannot assign {node} to the tail")
        self._tail = node


    def traverse(self):
        """This methods traverses the linked list.
        """

        # current node: starting from head
        current = self.head

        # traverse
        while current:
            yield current
            current = current.next


    def get_last_node(self) -> Node:
        """Retrieves the last node of the linked list.

        Returns:
            last_node (Node): the last node (tail).
        """

        if not self.has_head():
            return None

        head = self.head
        current = head

        while current.next:
            current = current.next

        # return the last node
        return current


    def create_mock_linked_list(self) -> None:
        """This method creates a mock linked list of the form
           
            90->80->60->50.

        The purpose of this method is to create a basic linked
        list to test the functionality of the class.
        """

        # get the test values
        values = self.get_test_values
        index: int = 0 # to process the list

        # head must be None
        # create the head node with the value '90'
        self.head = Node(values[index])

        # to create a list dynamically, declare 'current_node'
        current = self.head

        while index < 3:
            # increase the index
            index += 1

            # create new_node
            new_node = Node(values[index])

            # form the list
            current.next = new_node
            current = new_node


    # display linked list in format: A->B->C
    def display(self) -> None:
        """This method displays the current linked list.
        It uses the utility function of `traverse` to 
        efficiently traverse the list.
        """

        # traverse the list and print nodes
        for node in self.traverse():
            print(node, end="->" if node.next else "")


    def has_head(self) -> bool:
        """Checks if the head exists
        """
        return self.head is not None


    @override
    def append_to_end(self, data: int) -> None:
        """This method is used to insert 
        a new node to the linked list to the end.
        """
        self.insert_node(data, Position.END)


    @override
    def append_to_middle(self, data: int) -> None:
        """Adds the node to the middle of the linked list."""
        self.insert_node(data, Position.MIDDLE)


    @override
    def append_to_front(self, data: int) -> None:
        """This methods adds the node to the front
        """
        self.insert_node(data, Position.START)


    @override
    def insert_node(self,
        data: int,
        position: Position | int) -> None:
        """The methods adds the node to the speficied position.

        Args:
            data (int): an integer - valued hold by the node.
            position (int): an index.
        """
        return 0


    @override
    def delete_head(self) -> Node:
        """Deletes the head (the first node in the list) of the linked list.
        
        Returns:
            head (Node): the head of the linked list.
        """
        self.delete_node(Position.START)


    @override
    def delete_middle_node(self) -> Node:
        """Deletes the middle node of the linked list.
        
        Returns:
            middle (Node): the middle node of the linked list.
        """
        self.delete_node(Position.MIDDLE)


    @override
    def delete_tail(self) -> Node:
        """Deletes the tail (the last node in the list) of the linked list.

        Returns:
            tail (Node): the tail of the linked list.
        """
        self.delete_node(Position.END)


    @override
    def delete_node(self, position: int) -> Node:
        """The method deletes the node at the specified position.

        Args:
            position (int): an integer to represent the position of 
                a node to be deleted.

        Returns:
            node_to_delete (Node): a deleted node.
        """

        if position == 0:
            node_to_delete = self.head
            self.head = self.head.next
            return node_to_delete

        # traverse the list starting from head
        current = self.head

        for _ in range(position - 1):
            if current is None:
                return
            current = current.next

        if current.next is None:
            return None

        node_to_delete = current.next
        current.next = node_to_delete.next

        # return the deleted node
        return node_to_delete


    def compute_length(self) -> None:
        """This method computes the length of the linked list.
        """

        start = self.head
        end = self.get_last_node()
        count = 1
        current = start

        while current:
            # increase the count
            count += 1
            # traverse the list
            current = current.next

            if current == end:
                return count


    def __repr__(self) -> str:
        return f"LinkedList(head={self.head}, length={self.compute_length()})"


    def __len__(self) -> int:
        return self.compute_length()

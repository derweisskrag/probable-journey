"""This modules contains the linked list"""

from typing import override
from ..interfaces.abstracted_list import AbstractedLinkedList, AbstractedNode, Position, Action

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

        self._head = head
        self._tail = head
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

        self.tail = current


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


    def has_tail(self) -> bool:
        """Checks if the tail exits"""
        return self.tail is not None


    def determine_middle(self, length: int) -> int:
        """Determines the middle node of the linked list.

        Args:
            length (int): the length of the linked list.

        Returns:
            middle_index (int): the position of the middle node.
        """

        return length // 2 if length % 2 == 0 else length // 2 + 1


    def match_position(self,
                       new_node: Node = None,
                       position: Position = None,
                       action: Action = None) -> None:
        """Matches the position to perfrom the correct algorithm.
        
        Args:
            new_node (Node): the node of the linked list.
            position (Position): the position of the node in the list.
        """

        if not position or not new_node:
            return


        match position.value, action.value:
            case "START", "INSERT":
                new_node.next = self.head
                self.head = new_node
            case "END", "INSERT":
                self.tail.next = new_node
                self.tail = new_node
            case "MIDDLE", "INSERT":
                index = 0
                middle = self.determine_middle(self.compute_length())
                current = self.head

                while index != middle - 1:
                    index += 1
                    current = current.next

                new_node.next = current.next
                current.next = new_node
            case _:
                raise TypeError(f"Invalid action: '{position:!r}' !")
            


    def dispatch(self,
                 data: int = None,
                 action: Action = None,
                 position: Position = None) -> None:
        """Dispatches the event to perform an action.

        Args:
            action (Action): delete or insert node,
            position (Position): the position of the node.
        """

        if not action and not position:
            return

        match action.value:
            case "INSERT":
                self.insert_node(data, position, action)
            case "DELETE":
                return self.delete_node(position, action)
            case _:
                raise TypeError(f"Invalid action: '{action}' !")


    @override
    def append_to_end(self, data: int) -> None:
        """This method is used to insert 
        a new node to the linked list to the end.
        """
        self.dispatch(data, Action.INSERT, Position.END)


    @override
    def append_to_middle(self, data: int) -> None:
        """Adds the node to the middle of the linked list."""
        self.dispatch(data, Action.INSERT, Position.MIDDLE)


    @override
    def append_to_front(self, data: int) -> None:
        """This methods adds the node to the front
        """
        self.dispatch(data, Action.INSERT, Position.START)


    def append_at_index(self, data: int, position: int) -> None:
        """Appends the node at the specified position"""
        if position == 0:
            self.append_to_front(data)
        elif position == self.compute_length():
            self.append_to_end(data)
        else:
            self.dispatch(data, Action.INSERT, position)


    @override
    def insert_node(self,
        data: int,
        position: Position | int = 0,
        action: Action = None) -> None:
        """The methods adds the node to the speficied position.

        Args:
            data (int): an integer - valued hold by the node.
            position (int): an index.
        """

        if not self.has_head():
            # list empty, no starting point at this moment
            # create it
            self.head = Node(data)
            self.tail = self.head

        
        # create new node
        new_node = Node(data)

        # check the type of position
        if isinstance(position, Position):
            self.match_position(new_node, position, action)
        elif isinstance(position, int):
            # arbitrary index
            for index, current in enumerate(self.traverse()):
                if index == position - 1:
                    new_node.next = current.next
                    current.next = new_node
        else:
            raise TypeError(f"Invalid type: '{position:}'. Should be Position or Int!")


    @override
    def delete_head(self) -> Node:
        """Deletes the head (the first node in the list) of the linked list.
        
        Returns:
            head (Node): the head of the linked list.
        """
        return self.dispatch(None, Action.DELETE, Position.START)


    @override
    def delete_middle_node(self) -> Node:
        """Deletes the middle node of the linked list.
        
        Returns:
            middle (Node): the middle node of the linked list.
        """
        return self.dispatch(None, Action.DELETE, Position.MIDDLE)


    @override
    def delete_tail(self) -> Node:
        """Deletes the tail (the last node in the list) of the linked list.

        Returns:
            tail (Node): the tail of the linked list.
        """
        return self.dispatch(None, Action.DELETE, Position.END)


    @override
    def delete_node(self, 
                    position: Position | int,
                    action: Action) -> Node:
        """The method deletes the node at the specified position.

        Args:
            position (int): an integer to represent the position of 
                a node to be deleted.

        Returns:
            node_to_delete (Node): a deleted node.
        """


        if not isinstance(position, Position):
            # when not specified explicilty by Enum: "START", "END", "MIDDLE"
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
        else:
            # instance of Position
            # match types
            match position.value:
                case "MIDDLE":
                    for index, current in enumerate(self.traverse()):
                        if self.determine_middle(self.compute_length()) - 1 == index + 1:
                            node_to_delete = current.next
                            current.next = node_to_delete.next
                            return node_to_delete
                case "END":
                    for node in self.traverse():
                        if node.next == self.tail:
                            node_to_delete = self.tail
                            node.next = None # delete the node
                            self.tail = node
                            return node_to_delete
                case "START":
                    node_to_delete = self.head
                    self.head = self.head.next
                    return node_to_delete


    def delete_node_at_index(self, position) -> Node:
        """Deletes the node from position"""
        if position == 0:
            return self.dispatch(None, Action.DELETE, Position.START)
        else:
            return self.dispatch(None, Action.DELETE, position)


    @override
    def update_list(self) -> None:
        """Updates the list: keeps track of the tail, and size."""
        return 0


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

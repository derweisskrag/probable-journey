# Replace # TODO: with your code

class Node:
    def __init__(self, data: int) -> None:
        """A node object used by the linked list.

        Args:
            data (int): an integer to represent the value hold by the node.
        """
        self._data = data
        self.next = None


    @property
    def data(self) -> int:
        return self._data


    def __str__(self) -> str:
        return f"Node(data={self.data})"


    def __repr__(self) -> str:
        return f"Node(data={self.data})"


    def __eq__(self, other) -> bool:
        return self.data == other.data


    def __le__(self, other) -> bool:
        return self.data <= other.data


    def __ge__(self, other) -> bool:
        return self.data >= other.data


class CircularLinkedList:
    def __init__(self):
        """Circular linked list
        """
        self._head = None
        self._mock_values = [90, 80, 60, 50]


    @property
    def head(self) -> Node:
        return self._head


    @head.setter
    def head(self, node: Node) -> None:
        if node is None:
            return

        if isinstance(node, Node):
            self._head = node
        else:
            raise TypeError(f"Cannot assign {node} to the head!")


    @property
    def mock_values(self):
        return self._mock_values
    


    def traverse(self) -> Node:
        """This method uses generator to traverse the linked list.

        Returns:
            node (Node): a node of a linked list.
        """

        if not self.head:
            return

        current = self.head
        yield current

        while current.next != self.head:
            current = current.next
            yield current


    def has_head(self) -> bool:
        return self.head is not None


    def get_last_node(self) -> Node:
        """Retrieves the last node of the circular linked list.
        The last node is the tail whose next is the head.

        Returns:
            tail (Node): a node positioned at the end of the
                circular linked list.
        """

        current = self.head
        while current.next != self.head:
            current = current.next

        return current


    # create the linked list: 90->80->60->50
    def create_mock_linked_list(self) -> None:
        """This method creates a circular mock linked list.
        """
        
        # get the mock values
        values = self.mock_values
        
        # set the index
        index = 0

        # create the head
        self.head = Node(values[index])

        # keep track of nodes using `current`
        current = self.head

        while index < 3:
            # increase the index
            index += 1

            # create a new node
            new_node = Node(values[index])

            # form the list
            current.next = new_node
            current = new_node

        current.next = self.head


    def compute_length(self) -> int:
        """The method computes the length of the 
        circular linked list.

        Returns:
            length (int): the length of the circular
                linked list.
        """

        start = self.head
        end = self.get_last_node()
        count = 1
        current = start

        while current.next != start:
            # increase the count 
            count += 1

            # traverse the list
            current = current.next

            if current == end:
                return count


    # display circular linked list A->B->C in format: A->B->C->A
    def display(self) -> None:
        """This method displays the circular linked list.
        """

        # traverse the list using generator
        for node in self.traverse():
            print(node, end="->")

        # indicate the circular linked list
        print(self.head)


    def append_to_front(self, data: int) -> None:
        """This methods adds new node to the front of 
        the circular linked list.

        Args:
            data (int): an integer hold by the node
        """

        if not self.has_head():
            self.head = Node(data)
        else:
            # create new node
            new_node = Node(data)

            new_node.next = self.head
            self.head = new_node


    def append_to_end(self, data: int) -> None:
        """This methods adds the node to the end of the 
        circular linked list.

        Args:
            data (int): an integer hold by the node.
        """

        if not self.has_head():
            self.head = Node(data)
        else:
            last_node = self.get_last_node
            new_node = Node(data)

            last_node.next = new_node
            new_node.next = self.head


    def insert_node(self, 
        data: int, 
        position: int) -> None:
        """This methods inserts the node inserts the node
        at the specified position.

        Args:
            data (int): value of the node.
            position (int): indicates the index of the node at
                the circular linked list.

        """

        # create new node
        new_node = Node(data)

        if not self.has_head() \
            or postion == 0:
            # append the node to the front
            self.append_to_front(data)
        elif position == self.compute_length() - 1:
            # append the node to the end
            self.append_to_end(data)
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    return
                current = current.next

            new_node.next = current.next
            current.next = new_node


    def delete_node(self, position: int) -> Node:
        """This method deletes the node at the specified position.

        Args:
            position (int): indicates the index of the node at
                the circular linked list.

        Returns:
            node_to_delete (Node): a node to be deleted.
        """

        if position == 0: # delete the head
            node_to_delete = self.head
            self.head = self.head.next
            return node_to_delete
        elif position == self.compute_length() - 1:
            last_node = self.get_last_node()
            node_to_delete = last_node
            last_node.next = self.head
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    return
                current = current.next

            node_to_delete = current.next
            current.next = node_to_delete.next

            return node_to_delete



# Start of the script
linked_list = CircularLinkedList()

# create the initial linked list
linked_list.create_mock_linked_list()

# print the updated linked list
linked_list.display()



class Node:
    def __init__(self, data: int) -> None:
        """This class represents the node used in
        LinkedList data structure.

        Args:
            data (int): an integer.
        """
        
        # must be an integer
        assert isinstance(data, int), f"The data must be an integer"

        # instantiate
        self._data = data
        self.next = None # link to the next node


    @property
    def data(self):
        return self._data


    def __repr__(self) -> str:
        return f"Node(data={self._data})"


    def __str__(self) -> str:
        return f"Node(data={self._data})"


    def __eq__(self, other) -> bool:
        return self.data == other.data


class LinkedList:
    def __init__(self, head: Node = None) -> None:
        """This class represents the LinkedList.

        Args:
            head (Node): a starting node to create
                a linked list.
        """
        self._head = None if not head else head
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


    # method to append a node
    def append_to_end(self, data: int) -> None:
        """This method is used to insert 
        a new node to the linked list to the end.
        """

        if not self.has_head():
            self.head = Node(data)
        else:
            # get the head
            head = self.head

            # new node to add
            new_node = Node(data)

            # get the last node
            last_node = self.get_last_node()

            # insert the new node
            last_node.next = new_node


    def append_to_front(self, data: int) -> None:
        """This methods adds the node to the front
        """

        if not self.has_head():
            self.head = Node(data)
        else:
            # new_node to insert
            new_node = Node(data)

            # arrange the node to the front
            new_node.next = self.head
            self.head = new_node


    # insert node to linked list
    def insert_node(self, 
        data: int, 
        position: int) -> None:
        """The methods adds the node to the speficied position.

        Args:
            data (int): an integer - valued hold by the node.
            position (int): an index.
        """

        # create new_node 
        new_node = Node(data)

        if not self.has_head():
            new_node.next = self.head
            self.head = new_node 
        else:
            # traverse the list starting from head
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    return # exit the loop when current is None
                current = current.next

            new_node.next = current.next
            current.next = new_node


    # method to delete node at the given position
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
        return f"LinkedList(head={self.head}, length={self.length})"


    def __len__(self) -> int:
        return self.compute_length()


# Start of the script
linked_list = LinkedList() 

# create the initial linked list
linked_list.create_mock_linked_list()

# print the updated linked list
linked_list.display()
print() # empty string
print(len(linked_list), end="\n")

# try to insert
linked_list.append_to_front(30)
linked_list.display()

print()
print(len(linked_list), end="\n")

# to the end
linked_list.append_to_end(100)
linked_list.display()

print()
print(len(linked_list), end="\n")

# add to the position
linked_list.insert_node(110, 3)
linked_list.display()

print()
print(len(linked_list), end="\n")
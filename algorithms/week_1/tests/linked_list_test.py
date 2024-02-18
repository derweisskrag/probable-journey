import unittest

from ..implementation.linked_list import LinkedList, Node

class LinkedListTest(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList(Node(10))


    def tearDown(self):
        # release resources
        pass


    def test_append_front(self):
        # Test 1
        self.linked_list.append_to_front(20)
        self.linked_list.append_to_front(30)
        self.assertEqual(self.linked_list.head.data, 30)
        self.assertEqual(self.linked_list.tail.data, 10)

    
    def test_append_end(self):
        # Test 2
        self.linked_list.append_to_end(20)
        self.linked_list.append_to_end(30)
        self.assertEqual(self.linked_list.head.data, 10)
        self.assertEqual(self.linked_list.tail.data, 30)


    def test_append(self):
        # Test 3
        expected_data: list[int] = [10, 20, 30, 40]
        for data in expected_data[1:]:
            self.linked_list.append_to_end(data)

        # actual data
        actual_data = [node.data for node in self.linked_list.traverse()]

        # verify
        self.assertEqual(actual_data, expected_data)

    
    def test_delete_head(self):
        self.linked_list.append_to_end(20) # add Node(20) to the end
        # remove head
        head = self.linked_list.delete_head()
        # verify results
        self.assertEqual(head.data, 10)
        self.assertEqual([node.data for node in self.linked_list.traverse()], [20])


    def test_delete_tail(self):
        # populate the list
        for data in [20, 50, 100, 75]:
            self.linked_list.append_to_end(data)
        
        # delete tail
        tail = self.linked_list.delete_tail()

        # verify results
        self.assertEqual(tail.data, 75)
        self.assertEqual(self.linked_list.compute_length(), 4)
        self.assertEqual([node.data for node in self.linked_list.traverse()], [10, 20, 50, 100])


    def test_delete_middle(self):
        # populate the list
        self.linked_list.append_to_end(50)
        self.linked_list.append_to_middle(25)

        # delete the middle
        middle = self.linked_list.delete_middle_node()

        # verify results
        self.assertEqual(middle.data, 25)
        self.assertEqual([node.data for node in self.linked_list.traverse()], [10, 50])

    
    def test_delete_node_at_index(self):
        # populate the list
        for data in [25, 50, 75, 100, 125, 150]:
            self.linked_list.append_to_front(data)

        # delete the node
        # REMIND: 0 1 2 ... - For linked list, I used 0, ..., 1
        # For doublylinked list I used 1, ... 
        node_at_position_of_3 = self.linked_list.delete_node_at_index(3)

        # verify results
        self.assertEqual(node_at_position_of_3.data, 75)
        self.assertEqual([node.data for node in self.linked_list.traverse()], [150, 125, 100, 50, 25, 10])


    def test_mock_list(self):
        # create mock list
        self.linked_list.create_mock_linked_list()

        # verify
        self.assertEqual([node.data for node in self.linked_list.traverse()], [90, 80, 60, 50])
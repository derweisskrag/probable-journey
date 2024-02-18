"Testing DoublyLinkedList data structure"

import unittest

from ..implementation.doubly_linked_list import DoublyLinkedList, Direction, Node

class DoublyLinkedListTest(unittest.TestCase):
    def setUp(self):
        # initialize stuff
        self.doubly_linked_list = DoublyLinkedList(Node(10))



    def tearDown(self):
        # release resources
        pass


    def test_append_front(self):
        # Test 1:
        # Testing `append_front`
        self.doubly_linked_list.append_front(5)
        self.assertEqual(self.doubly_linked_list.head.data, 5)
        self.assertEqual(self.doubly_linked_list.tail.data, 10)


    def test_append_end(self):
        # Test 2:
        # Testing `append_end`
        self.doubly_linked_list.append_end(15)
        self.assertEqual(self.doubly_linked_list.head.data, 10)
        self.assertEqual(self.doubly_linked_list.tail.data, 15)

    
    def test_traverse_forward(self):
        # Test 3:
        expected_data: list[int] = [10, 20, 30, 40]

        for data in expected_data[1:]:
            self.doubly_linked_list.append_end(data)

        # actual data
        actual_data = [node.data for node in self.doubly_linked_list.traverse()]

        # verify equality
        self.assertEqual(actual_data, expected_data)

    
    def test_traverse_backward(self):
        # Test 4:
        expected_data: list[int] = [10, 20, 30, 40]
        for data in expected_data[1:]:
            self.doubly_linked_list.append_end(data)

        # actual data 
        actual_data = [node.data for node in self.doubly_linked_list.traverse()][::-1]

        # verify
        self.assertEqual(actual_data, list(reversed(expected_data)))


    def test_delete_node(self):
        expected_data: list[int] = [10, 20, 30, 40]
        for data in expected_data[1:]:
            self.doubly_linked_list.append_end(data)

        # delete the node at the position 1
        self.doubly_linked_list.delete_node(2)

        # actual data
        actual_data = [node.data for node in self.doubly_linked_list.traverse()]
        self.assertEqual(actual_data, [10, 30, 40])
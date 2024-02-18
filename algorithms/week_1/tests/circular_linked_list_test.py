import unittest

from ..implementation.circular_linked_list import CircularLinkedList, Node

class CircularLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.circular_linked_list = CircularLinkedList(Node(10))


    def tearDown(self):
        pass


    def test_append_front(self):
        # append to front
        self.circular_linked_list.append_to_front(20)
        
        # verify results
        self.assertEqual(self.circular_linked_list.head.data, 20)

    
    def test_append_end(self):
        # append to end
        self.circular_linked_list.append_to_end(20)

        # verify results
        self.assertEqual(self.circular_linked_list.head.data, 10)
        

    def test_insert_node(self):
        for data in [20, 30, 40]:
            self.circular_linked_list.append_to_front(data)

        # actual data
        actual_data = [node.data for node in self.circular_linked_list.traverse()]

        # verify
        self.assertEqual(actual_data, [40, 30, 20, 10])
        

    def test_delete_head(self):
        # insert new node
        self.circular_linked_list.append_to_front(20)

        # delete head
        head = self.circular_linked_list.delete_node(0)

        # verify results
        self.assertEqual(head.data, 20)


    def test_delete_tail(self):
        # insert new node
        self.circular_linked_list.append_to_front(20)

        # delete tail
        tail = self.circular_linked_list.delete_node(self.circular_linked_list.compute_length() - 1)

        # verify results
        self.assertEqual(tail.data, 10)


    def test_mock_list(self):
        # create mock list
        self.circular_linked_list.create_mock_linked_list()

        # verify
        self.assertEqual([node.data for node in self.circular_linked_list.traverse()], [90, 80, 60, 50])
import unittest

# import data structures 
from ..implementation.linked_list import LinkedList, Node as LinkedListNode
from ..implementation.circular_linked_list import CircularLinkedList, Node as CircularLinkedListNode
from ..implementation.doubly_linked_list import DoublyLinkedList, Node as DoublyLinkedListNode


# import scripts
from ..homework.remove_duplicates import remove_duplicates
from ..homework.concatenate import concatenate
from ..homework.palindrome_doubly_linked_list import is_palindrome
from ..homework.reverse_circular_list import reverse_circular_linked_list

class HomeWork(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList(LinkedListNode(10))
        self.doubly_linked_list = DoublyLinkedList(DoublyLinkedListNode(10))
        self.circular_linked_list = CircularLinkedList(CircularLinkedListNode(10))


    def tearDown(self):
        pass


    def test_remove_duplicates(self):
        # populate the list with the data
        for data in [20, 30, 40, 20, 10, 20, 30]:
            self.linked_list.append_to_end(data)

        # use the function to remove duplicates
        actual_list = remove_duplicates(self.linked_list)

        # verify results
        self.assertEqual([node.data for node in actual_list.traverse()], [10, 20, 30, 40])


    def test_concatenate(self):
        # declare two test lists
        l1 = LinkedList(LinkedListNode(10))
        l2 = LinkedList(LinkedListNode(90))

        # populate them with data
        for data in [20, 30, 25, 15, 5]:
            l1.append_to_end(data)

        for data in [5, 9, 13, 31, 26]:
            l2.append_to_end(data)

        # perform concatenation
        result = concatenate(l1, l2)

        # verify result
        self.assertEqual([node.data for node in result.traverse()], [10, 20, 30, 25, 15, 5, 90, 5, 9, 13, 31, 26])


    def test_reverse_circular_linked_list(self):
        # create circular-linked list
        circular_linked_list = CircularLinkedList(CircularLinkedListNode(1))
        
        # populate it with more data
        for data in [2, 3, 4, 5, 6, 7, 8, 9]:
            circular_linked_list.append_to_front(data)


        # reverse the list
        reversed_list = reverse_circular_linked_list(circular_linked_list)

        # verify the result 
        self.assertEqual([node.data for node in reversed_list.traverse()], [1, 2, 3, 4, 5, 6, 7, 8, 9])
        


    def test_palindrome_doubly_linked_list(self):
        # create list 
        doubly_linked_list = DoublyLinkedList(DoublyLinkedListNode(1))

        # populate it with data
        for data in [2, 3, 2, 1]:
            doubly_linked_list.append_end(data)

        # check for palindrome
        result = is_palindrome(doubly_linked_list)

        # verify result
        self.assertEqual(result, True)
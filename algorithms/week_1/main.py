"""Entry point"""

# import unittests
import unittest

from .implementation.circular_linked_list import CircularLinkedList, Node

# import tests
from .tests.linked_list_test import LinkedListTest
from .tests.circular_linked_list_test import CircularLinkedListTest
from .tests.doubly_linked_list_test import DoublyLinkedListTest
from .tests.homework import HomeWork

def main():
    """Main function"""
    test_suite = unittest.TestLoader().loadTestsFromTestCase(HomeWork)

    test_runner = unittest.TextTestRunner()

    test_runner.run(test_suite)
    

if __name__ == "__main__":
    main()

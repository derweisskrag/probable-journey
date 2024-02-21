"""This module provides the Test cases for the circular queue"""

# import unittest
import unittest

# import the circular queue
from ..implementation.circular_queue import CircularQueue


class CircularQueueTest(unittest.TestCase):
    def setUp(self):
        self.queue = CircularQueue(maxsize=5)


    def tearDown(self):
        # clean up
        pass

    
    def test_enqueue(self):
        """Test the function of the enqueue for the circular queue."""

        # define the element to be enqueued
        element_to_enqueue: int = 1

        # call the method
        self.queue.enqueue(element_to_enqueue)

        # test it
        self.assertEqual(self.queue.queue[0], element_to_enqueue)


"""The entry method of the week_2 module"""

# import the test
from .tests.circular_queue_test import CircularQueueTest

# import unittest
import unittest

def main():
    """Main function"""

    test_suite = unittest.TestLoader().loadTestsFromTestCase(CircularQueueTest)

    test_runner = unittest.TextTestRunner()

    test_runner.run(test_suite)


if __name__ == "__main__":
    main()

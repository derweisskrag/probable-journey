"""Module containing the function"""

from ..implementation.doubly_linked_list import DoublyLinkedList

def is_palindrome(lst: DoublyLinkedList) -> bool:
    """Checks if the doubly-linked list is a palindrome.
    
    Args:
        lst (DoublyLinkedList): the doubly-linked list.

    Returns:
        result (bool): True or False.
    """

    # edge case
    if not lst.head:
        return True

    head = lst.head
    tail = lst.tail

    def _is_palindrome_recursive(front, rear):
        if front == rear or front.prev == rear:
            return True
        if front.data != rear.data:
            return False
        return _is_palindrome_recursive(front.next, rear.prev)

    return _is_palindrome_recursive(head, tail)

"""Module provides the function for reversing the circular linked list."""

from ..implementation.circular_linked_list import CircularLinkedList

def reverse_circular_linked_list(lst: CircularLinkedList) -> CircularLinkedList:
    """Reverses the circular linked list.

    Args:
        lst (CircularLinkedList): the circular-linked list.

    Returns:
        result (CircularLinkedList): the reversed circular-linked list.
    """

    if not lst.head:
        return lst

    
    current = lst.head
    previous = None

    while current.next:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    # Handle the last node separately
    current.next = previous
    lst.head = current  # Update the head of the list

    return lst
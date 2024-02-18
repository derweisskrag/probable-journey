"""Module containing the implementation of `remove_duplicates` from linked list"""

from ..implementation.linked_list import LinkedList, Node

def remove_duplicates(lst: LinkedList) -> LinkedList:
    """Removes duplicates from the sorted linked list.
    
    Args:
        lst (LinkedList): the linked list to process.

    Returns:
        result (LinkedList): the linked list without duplicates.
    """

    if not lst.head:
        return lst

    # declare set
    seen = set([lst.head.data])
    current = lst.head


    while current.next:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next


    return lst
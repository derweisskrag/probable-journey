from ..implementation.linked_list import LinkedList

def concatenate(l1: LinkedList, l2: LinkedList) -> LinkedList: 
    """Concatenates two linked lists.

    Args:
        l1 (LinkedList): the first linked list.
        l2 (LinkedList): the second linked list.

    Returns:
        result (LinkedList)
    """

    # edge cases

    if not l2:
        return l1
    
    if not l1:
        return l2
    
    if not l1 and not l2:
        return

    for node in l2.traverse():
        # add nodes of l2 to l1
        l1.append_to_end(node.data)

    return l1
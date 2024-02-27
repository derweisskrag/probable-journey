class Node:
    """Reprenests the node of the doubly-linked list."""
    def __init__(self, data: int) -> None:
        """Initialization of the node of doubly-linked list."""
        self._data = data
        self.next = None
        self.prev = None


    @property
    def data(self) -> int:
        """Retrieves the value of the node"""
        return self._data  


    @data.setter
    def data(self, value: int) -> None:
        """Sets a new value to the node."""
        self._data = value


    def __repr__(self) -> str:
        return f"Node(data={self.data})"



class DoublyLinkedList:
    """Represents the DoublyLinkedList."""
    def __init__(self) -> None:
        """Initialization of the doubly-linked list."""
        self._head = self._tail = None


    @property
    def get_head(self) -> Node:
    	"""Retrieves the head"""
    	return self._head


    @property
    def get_tail(self) -> Node:
    	"""Retrieves the tail"""
    	return self._tail


    def traverse(self) -> Node:
    	"""Traverses the doubly-linked lists and yields a node.

		Yields:
			current (Node): the node to yield.
    	"""

    	if not self.has_head():
    		return

    	current = self._head

    	while current:
    		yield current
    		current = current.next


    def insert_node(self, position: int, value: int) -> None:
    	"""Insersts the node at the specified position of
    	the doubly-linked list.


		Args:
			position (int): the index of the node (0, 1, ...).
			value (int): the value of the node to be added.
    	"""
    	
    	if not self.has_head():
    		# linked list is empty
    		# set the head:
    		self._head = Node(value)

    		# set the tail:
    		self._tail = self._head
    	else:
	    	# create new_node
	    	new_node = Node(value)

	    	# process edge cases
	    	if position == 0:
	    		# append to the front
	    		# arrange the new node in list:
	    		new_node.next = self._head
	    		self._head.prev = new_node

	    		# update the head
	    		self._head = new_node
	    	elif position == -1:
	    		# append to the end
	    		# arrange the new node in list:
	    		self._tail.next = new_node
	    		new_node.prev = self._tail

	    		# update the tail
	    		self._tail = new_node
	    	else:
	    		# insert at the specified position
	    		# position = 0, 1, ... - index
	    		for index, node in enumerate(self.traverse()):
	    			if index == position - 1: # stop before the target position node
	    				# arrange the node
	    				new_node.next = node.next
	    				new_node.prev = node

	    				if node.next is not None:
	    					node.next.prev = new_node

	    				# update the current node's next
	    				node.next = new_node



    def append_to_front(self, value: int) -> None:
    	"""Appends a node to the front."""
    	self.insert_node(0, value)


    def append_to_end(self, value: int) -> None:
    	"""Appends a node to the end."""
    	self.insert_node(-1, value)


    def remove_rear(self) -> Node:
    	"""Removes the element from the end of the Doubly-linked list.

		Returns:
			node_to_delete (Node): tail of the doubly-linked list.
    	"""
    	return self.remove_node(-1) # remove the at index `-1`


    def remove_front(self) -> Node:
    	"""Removes the element from the front of the Doubly-linked list.

    	Returns:
    		node_to_delete (Node): the head of the doubly-linked list.
    	"""
    	return self.remove_node(0)


    def remove_node(self, position: int) -> Node:
    	"""Removes the node from the list at the specified position.
		
		Args:
			position (int): the position of node to be deleted.

		Returns:
			node_to_delete (Node): node to delete.
    	"""
    	if not self.has_head() or not self.has_tail():
    		return

		# handle edge cases
    	if position == 0:
    		# delete head
    		node_to_delete = self._head

    		# re-arrange the list
    		self._head = self._head.next

    		# delete the node
    		if not self._head:
    			# if the head was the only node
    			self._tail = None

    		# return the deleted node
    		return node_to_delete
    	elif position == -1:
    		# delete the tail
    		node_to_delete = self._tail

    		# re-arrange the list
    		self._tail = self._tail.prev

    		# delete
    		if self._tail:
    			self._tail.next = None
    		else:
    			self._head = None

    		return node_to_delete
    	else:
    		# traverse the list
    		for index, node in enumerate(self.traverse()):
    			if index == position - 1: # stop before target node
    				# define the node to delete
    				node_to_delete = node.next

    				# re-arrange the list
    				node.next = node_to_delete.next
    				
    				if node.next:
    					node.next.prev = node

    				# return the node
    				return node_to_delete


    def has_head(self) -> bool:
    	"""Checks if the head is set"""
    	return self._head is not None


    def has_tail(self) -> bool:
    	"""Checks if the tail is set"""
    	return self._tail is not None


    def display(self) -> None:
    	"""Displays the doubly-linked list."""
    	for node in self.traverse():
    		print(node, end="<-->" if node.next else "")


class Deque:
	"""Represents the deque class"""
	def __init__(self) -> None:
		self._deque = DoublyLinkedList()
		self._size = 0



	def enqueue_front(self, value: int) -> None:
		"""Enqueues an element to the left of the dequeue.

		Args:
			value (int): an element to be added to the dequeue.
		"""

		# add an element to the front
		self._deque.append_to_front(value)
		
		# update the size
		self._size += 1


	def enqueue_rear(self, value: int) -> None:
		"""Enqueues an element to the right of the dequeue (rear).

		Args:
			value (int): an element to be added to the dequeue.
		"""
		# add an element to the rear
		self._deque.append_to_end(value)

		# update the size
		self._size += 1


	def peek_front(self) -> None:
		"""Displays the front peak of the dequeue."""
		if self.is_empty():
			raise IndexError("Deque is empty")
		
		# print the top element on the left
		print(self._deque.get_head)


	def peek_rear(self) -> None:
		"""Displays the rear peak of the dequeue."""
		if self.is_empty():
			raise IndexError("Deque is empty")

		# print the top element on the right
		print(self._deque.get_tail)


	def dequeue_front(self) -> Node:
		"""Removes the element from the front of the dequeue.

		Returns:
			element_to_deque (Node): the left peek of the dequeue.
		"""

		if self.is_empty():
			raise IndexError("Deque is empty")

		# remove the element
		element_to_deque = self._deque.remove_front()

		# update the size
		self._size -= 1

		# return the dequeued value
		return element_to_deque


	def dequeue_rear(self) -> Node:
		"""Removes the element from the end of the dequeue.

		Returns:
			element_to_deque (Node): the right peek of the dequeue (peek_rear).
		"""

		if self.is_empty():
			raise IndexError("Deque is empty")

		# remove the element
		element_to_deque = self._deque.remove_rear()

		# update the size
		self._size -= 1

		# return the dequeued element
		return element_to_deque


	def is_empty(self) -> bool:
		"""Checks if the deque is empty"""
		return self._size == 0


	def display(self) -> None:
		"""Displays the deque elements to the console"""
		self._deque.display()


	def __len__(self) -> int:
		return self._size


class DequeList:
	"""Represents the deque implemented by an array"""
	def __init__(self) -> None:
		self._deque = []


	def is_empty(self) -> bool:
		"""Checks if the deque is empty"""
		return len(self._deque) == 0


	def enqueue_front(self, value: int) -> None:
		"""Enqueues a value to the front of the deque 
		implemented by a list.

		Args:
			value (int): a value to be enqueued to the front.
		"""
		self._deque.insert(0, value)


	def enqueue_rear(self, value: int) -> None:
		"""Enqueues a value to the rear of the dequeue.

		Args:
			value (int): a value to be enqueued.
		"""
		self._deque.append(value)


	def dequeue_front(self) -> int:
		"""Dequeues the element from the front of the dequeue.

		Returns:
			element_to_deque (int): the peek_front element.
		"""

		return self._deque.pop(0)


	def dequeue_rear(self) -> int:
		"""Dequeues the peek_rear element from the deque.

		Returns:
			element_to_deque (int): the peek_rear.
		"""
		return self._deque.pop()


	def peek_rear(self) -> int:
		"""Displays the top element from rear"""
		print(self._deque[-1])


	def peek_front(self) -> int:
		"""Displays the top element from front"""
		print(self._deque[0])


	def traverse(self) -> int:
		for value in self._deque:
			yield value


	def display(self) -> None:
		for index, element in enumerate(self.traverse()):
			print(element, end="->" if index != len(self._deque) - 1 else "")

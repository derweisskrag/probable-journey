"""This module implements the queue using Array"""

class Queue[T]:
    """Represents the queue."""
    def __init__(self) -> None:
        self._queue = []
        self._size = 0


    @property
    def queue(self) -> list[T]:
        """Retrieves the queue."""
        return self._queue


    @property
    def size(self) -> int:
        """Retrieves the size of the queue."""
        return self._size
    

    @size.setter
    def size(self, value: T) -> None:
        """Sets a value to the size."""
        self._size = value


    def enqueue(self, element: T) -> None:
        """This methods enqueues (appends) the element to the queue.
        
        Args:
            element (T): element to be enqueued.
        """
        self.queue.append(element)


    def dequeue(self) -> T:
        """Dequeues (removes) the element from the queue.
        
        Returns:
            result (T): removes the element from the queue.
        """
        if self.is_empty():
            return
        
        return self.queue.pop(0)
    

    def peek(self) -> None:
        """Displays the top element of the queue."""
        print(f"{self.queue[0]}")


    def is_empty(self) -> bool:
        """Checks if the queue is empty.
        
        Returns:
            result (bool): if empty, returns True, otherwise False.
        """
        return self.size == 0


    def display(self) -> None:
        """Displays the queue elements (prints to the console)."""
        for elem in self.queue:
            print(f"{elem}")


    def __len__(self) -> int:
        """Overloads the `len` function to return the length of the queue."""
        return self.size
    

    def __repr__(self) -> str:
        return f"Queue(peek={self.peek()}, length={self.size})"
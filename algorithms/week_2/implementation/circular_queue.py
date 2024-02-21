"""Circular queue module implemented by array"""

class CircularQueue:
    """Represents Circular Queue implemented by the list (Array)."""
    def __init__(self, maxsize: int) -> None:
        self._queue = [0] * maxsize
        self._size = maxsize
        self._front = 0
        self._count = 0


    @property
    def queue(self) -> list:
        """Retrieves the queue."""
        return self._queue
 

    @property
    def size(self) -> int:
        """Retrieves the size of the queue."""
        return self._size
    

    @property
    def front(self) -> int:
        """Retrieves the front index of the circular queue."""
        return self._front
    

    @front.setter
    def front(self, value: int) -> None:
        """Sets a value to the front index of the circular queue."""
        self._front = value


    @property
    def count(self) -> int:
        """Retrieves the current total number of element present in 
        the circular queue.
        """
        return self._count
    

    @count.setter
    def count(self, value: int) -> None:
        """Sets a value to the current total number of elements present in
        the circular queue."""
        self._count = value
    

    def enqueue(self, element: int) -> None:
        """Adds an element to the circular queue.
        
        Args:
            element (int): element to be enqueued.
        """
        if self.is_full():
            # if the circular queue full
            # dequeue the top element
            self.dequeue()


        # insert the element to the queue
        # to the front of the circular queue.
        self.queue[(self.front + self.count) % self.size] = element
        
        # update the total number of elements in the queue
        self.count += 1


    def dequeue(self) -> int:
        """Removes an element from the circular queue.
        
        Returns:
            element (int): element of the circular queue
                to be removed.
        """
        # take the top element of the queue
        result = self.queue[self.front]

        # remove the element from the queue
        self.queue[self.front] = None

        # update the front index
        self.front = (self.front + 1) % self.size

        # update the total number elements of the queue
        self.count -= 1

        # return the dequeued element
        return result
    

    def peek(self) -> None:
        """Displays the top element of the circular queue."""
        print(f"The peek element = {self.queue[self.front]}")


    def display(self) -> None:
        """Displays the circular queue, and prints elements to the console."""
        print(str(self.queue))


    def is_empty(self) -> bool:
        """Checks if the circular queue is empty.
        
        Returns:
            result (bool): if empty, returns True, otherwise False.
        """
        return self.size == 0

    
    def is_full(self) -> bool:
        """Checks if the circular queue is full.
        
        Returns:
            reulst (bool): if full, returns True, otherwise False.
        """
        return self.size == self.count


    def __len__(self):
        """Overloads the `len` function to return the size of the circular queue."""
        return self.size
    

    def __str__(self) -> str:
        return "->".join(map(str, self.queue))

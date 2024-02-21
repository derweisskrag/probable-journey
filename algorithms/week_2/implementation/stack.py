"""This module implements the stack"""

class Stack[T]:
    """Represents the stack"""
    def __init__(self) -> None:
        self._stack = []
        self._size = 0
    

    @property
    def size(self) -> int:
        """Retrieves the stack."""
        return self._size
    

    @size.setter
    def size(self, value: int) -> None:
        """Sets the value to the size."""
        self._size = value


    @property
    def stack(self) -> list[T]:
        """Retrieves the stack."""
        return self._stack


    def pop(self):
        """Pops the element from the top of the Stack.
        
        Returns:
            element (T): element from the stack.
        """

        if self.is_empty():
            return
        
        # decrease the size
        self.size -= 1

        return self.stack.pop()

    def append(self, element):
        """Appends the element to the stack
        
        Args:
            element (T): the element add to the stack.
        """

        self.size += 1
        self._stack.append(element)


    def peek(self) -> None:
        """Shows the top element of the stack."""
        
        if self.is_empty():
            return
        
        print(f"{self.stack[-1]}")


    def display(self) -> None:
        """Displays the stack elements"""
        for elem in reversed(self.stack):
            print(f"{elem}")


    def is_empty(self) -> bool:
        """Cheks if the stack is empty.
        
        Returns:
            result (bool): if empty -> True, otherwise False.
        """
        return self.size == 0


    def __len__(self):
        """Returns the size by overloading `len`."""
        return self.size

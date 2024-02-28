from abc import ABC, abstractmethod
from typing import override # as of Python 12

class GraphInterface(ABC):
    """Defines the blueprint for the Graphs classes"""
    @abstractmethod
    def __init__(self, num_vertices: int) -> None:
        super().__init__()

    @abstractmethod
    def add_edge(self, v1: int, v2: int) -> None:
        pass

    @abstractmethod
    def is_adjacent(self, v1: int, v2: int) -> bool:
        pass

    @abstractmethod
    def return_adjacent(self, v: int) -> list[int]:
        pass


class WeightedGraphInterface(GraphInterface):
    def __init__(self, num_vertices: int) -> None:
        super().__init__(num_vertices)


    @abstractmethod
    def add_edge(v1: int, v2: int, w: int) -> None:
        pass


class Graph(GraphInterface):
    """Represents the undirected Graph implemented by the adjacent matrix."""
    def __init__(self, num_vertices: int) -> None:
        super().__init__(num_vertices)
        self._data = [
            [0] * num_vertices for _ in range(num_vertices)
        ]
        
    
    @override
    def add_edge(self, v1: int, v2: int) -> None:
        """Adds an edge between two vertices.
        
        Args:
            v1 (int): the v1 vertex in Graph.
            v2 (int): the v2 vertex in Graph.
        """
        # our graph is not symmetric
        try:
            self._data[v1][v2], self._data[v2][v1] = 1, 1
        except IndexError as e:
            raise Exception(f"Must be a valid index for the 2D-list (matrix): {e!r}")
        
        
        
    @override
    def is_adjacent(self, v1: int, v2: int) -> bool:
        """Checks if two vertices are adjacent."""
        
        # Must check if there is an edge between them
        return self._data[v1][v2] > 0
        
       
    @override
    def return_adjacent(self, v: int) -> tuple[int]:
        """Returns the adjacent list that implements the Graph.
        
        Args:
            v (int): the row index.
            
        Returns:
            adjacent_list (tuple[int]): a list of pointers.
        """
        # return the adjacent list
        return tuple(((row, index) for index, row in enumerate(self._data[v]) if row > 0))


class DirectedGraph(Graph):
    """Represents the undirected Graph implemented by the adjacent matrix."""
    def __init__(self, num_vertices: int) -> None:
        super().__init__(num_vertices)
        
    @override
    def add_edge(self, v1: int, v2: int) -> None:
        """Adds an edge between two vertices.
        
        Args:
            v1 (int): the v1 vertex in Graph.
            v2 (int): the v2 vertex in Graph.
        """
        # our graph is not symmetric
        try:
            self._data[v1][v2] = 1
        except IndexError as e:
            raise Exception(f"Must be a valid index for the 2D-list (matrix): {e!r}")
        
        
      


class WeightedGraph(WeightedGraphInterface, Graph):
    def __init__(self, num_vertices: int) -> None:
        super().__init__(num_vertices)
        self._data = [
            [0] * num_vertices for _ in range(num_vertices)
        ]


    @override
    def add_edge(self, v1: int, v2: int, weight: int) -> None:
        """Adds an edge between vertices"""
        
        # undirected weighted graph
        self._data[v1][v2] = weight
        self._data[v2][v1] = weight



def main():
    num_vertices = 6
    graph = Graph(num_vertices)
    graph.add_edge(1, 2)
    print(graph.return_adjacent(1))
    
    directed_graph = DirectedGraph(num_vertices)
    directed_graph.add_edge(1, 2)
    print(directed_graph._data)
    
    w=WeightedGraph(num_vertices)
    w.add_edge(1,2, 20)
    print(w._data)
    print(w.is_adjacent(1,2))
    print(w.return_adjacent(1))
    

if __name__ == "__main__":
    main()

"""This module implements graph using adjacency matrix"""
class Graph(GraphInterface):
    """Represents the Graph implemented by the adjacent matrix."""
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
        
        
        
    @override
    def is_adjacent(self, v: int) -> bool:
        """Checks if two vertices are adjacent"""
        pass
        
       
    @override
    def return_adjacent(self, v: int) -> list[int]:
        """Returns the adjacent list that implements the Graph.
        
        Args:
            v (int): the row index.
            
        Returns:
            adjacent_list (list[int]): a list of pointers.
        """
        pass

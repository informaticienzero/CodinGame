import sys
import math

class Graph:

    def __init__(self, **kwargs):
        """Creates a Graph.

        Kwargs:
            graph (dictionary) : an already existing dictionary of vertex and edges.
            is_directed (bool) : is the graph directed (true) or not (false).

        Returns:
            An undirected empty Graph by default.

        """
        self.__data = kwargs.get('graph', {})
        self.__is_directed = kwargs.get('is_directed', False)


    def add_vertex(self, vertex):
        """Adds a vertex to the graph. If vertex already exists, does nothing.

        Args:
            vertex : a vertex to add.
        """
        if not self.contains_vertex(vertex):
            self.__data[vertex] = []


    def remove_vertex(self, vertex):
        """Removes a vertex to the graph. If the vertex is not in graph, does nothing.

        Args:
            vertex : a vertex to remove.
        """
        connections = self.connected_vertex(vertex)
        if len(connections) == 0:
            self.__data.pop(vertex, None)
        else:
            # First erasing all occurences in connected vertex.
            for connected in connections:
                if len(self.connected_vertex(connected)) != 0:
                    self.connected_vertex(connected).remove(vertex)
            self.__data.pop(vertex, None)

    
    def connected_vertex(self, vertex):
        """Gets all the connected vertex of a given vertex.

        Returns:
            A list of vertex if the vertex exists.
            An empty list if the vertex doesn't exist.
        """
        return self.__data.get(vertex, [])


    def contains_vertex(self, vertex):
        """Checks if the graph has the specified vertex.

        Args:
            vertex : a vertex.

        Returns:
            True if the vertex is in the graph.
            False if the vertex is not in the graph.
        """
        return vertex in self.__data.keys()


    def add_edge(self, first, second):
        """Add an edge between two vertex. If a vertex is not valid or doesn't exist, does nothing.

        Args:
            first : a vertex.
            second : a vertex.
        """
        if self.contains_vertex(first) and self.contains_vertex(second):
            self.__data[first].append(second)

            # If undirected graph, don't forget to add edge in the other side too.
            if not self.__is_directed:
                self.__data[second].append(first)


    def remove_edge(self, first, second):
        """Removes an edge between two vertex. If a vertex is not valid or doesn't exist, does nothing.

        Args:
            first : a vertex.
            second : a vertex.
        """
        if second in self.connected_vertex(first):
             self.__data[first].remove(second)

        # If undirected graph, don't forget to delete in the other side too.
        if not self.__is_directed:
            if first in self.connected_vertex(second):
                self.__data[second].remove(first)


    def has_edge(self, first, second):
        """Checks if there is an edge between two vertex.
        If one of the vertex in not in the graph or doesn't exist, return False.

        Args:
            first : a vertex.
            second : a vertex.

        Returns:
            False if one or both of the vertex are not set or not in graph or not connected.
            True:
                if is_directed : there is a connexion from first to second.
                else : there is a connexion from first to second and from second to first.
        """
        has_connexion = False

        if self.contains_vertex(first) and self.contains_vertex(second):
            if self.__is_directed:
                has_connexion = second in self.__data[first]
            else:
                has_connexion = first in self.__data[second] and second in self.__data[first]

        return has_connexion


    def interior_degree(self, vertex):
        """Returns the interior degree of a vertex, a.k.a the number of edges coming to the vertex.

        Args:
            vertex : An existing vertex

        Returns:
            An integer giving the interior degree of the vertex.
        """
        total = 0
        for key in self.__data:
            total += self.__data[key].count(vertex)
        return total


    def exterior_degree(self, vertex):
        """Returns the exterior degree of a vertex, a.k.a the number of edges extending from the vertex.

        Args:
            vertex : An existing vertex

        Returns:
            An integer giving the exterior degree of the vertex.
        """
        return len(self.connected_vertex(vertex))


    def degree(self, vertex):
        """Returns the degree of a vertex, a.k.a the number of edges coming to and extending from the vertex.

        Args:
            vertex : An existing vertex

        Returns:
            An integer giving the (interior + exterior) degree of the vertex.
        """
        return self.interior_degree(vertex) + self.exterior_degree(vertex)


    def to_list(self):
        """Returns the graph in the form of an adjacent list using a dictionary.

        Returns:
            A dictionary representing the graph.
        """
        return self.__data


    def to_matrix(self):
        pass


    @staticmethod
    def bfs_paths(graph, start, goal):
        """Uses the Breadth First Search algorithms to find all paths from a vertex to another.

        Arguments:
            graph (Graph) : a non empty graph.
            start (vertex) : the vertex from where we start.
            goal (vertex) : the vertex to reach.

        Returns:
            A generator.
        """
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next in set(graph.to_list()[vertex]) - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))
    

    @staticmethod
    def bfs_shortest_path(graph, start, goal):
        """Gets the sortest path between two vertexes using the BFS algorithm.

        Arguments:
                graph (Graph) : a non empty graph.
                start (vertex) : the vertex from where we start.
                goal (vertex) : the vertex to reach.
        
        Returns:
            A list which is the shortest path.
        """
        try:
            return next(Graph.bfs_paths(graph, start, goal))
        except StopIteration:
            return None


graph = Graph()
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    
    graph.add_vertex(n1)
    graph.add_vertex(n2)
    graph.add_edge(n1, n2)

gateways = []    
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gateways.append(ei)

# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    
    # The main loop is inspired by DeVoTeD, thanks to him !
    path = range(1000)
    for gate in gateways:
        current = Graph.bfs_shortest_path(graph, si, gate)
        if current != None and len(current) < len(path):
            path = current

    print(str(path[0]) + " " + str(path[1]))

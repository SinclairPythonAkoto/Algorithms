"""Graph

A graph is a collection of nodes (verticies), and edges connecting
them, with no hierarchical structure.

One common use of a graph is to represent a social network, where people are nodes 
in the graph and relationships between them are edges. Each edge can have a weight 
representing the strength of the relationship between the two people.

This implementation below could be used in a real-world scenario to represent a 
social network. Each person is represented by a node in the graph, and each relationship 
between two people is represented by an edge. The graph structure allows for efficient 
searching and traversal of the social network. For example, you could use graph algorithms 
to find the shortest path between two people, or to identify clusters of people with strong 
relationships.
"""
class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.adjacent_nodes = {}
    
    def add_edge(self, node, weight=0):
        self.adjacent_nodes[node] = weight
    
    def __lt__(self, other):
        return self.name < other.name
    

class Graph:
    def __init__(self) -> None:
        self.nodes = {}

    def add_node(self, name):
        node = Node(name)
        self.nodes[name] = node
        return node
    
    def add_edge(self, node1, node2, weight=0):
        if node1 not in self.nodes:
            self.add_node(node1)
        if node2 not in self.nodes:
            self.add_node(node2)
        self.nodes[node1].add_edge(self.nodes[node2], weight)
        self.nodes[node2].add_edge(self.nodes[node1], weight)


# create a new empty graph
social_network: Graph = Graph()

# add some people to the graph
alice = social_network.add_node('Alice')
bob = social_network.add_node('Node')
john = social_network.add_node('John')
david = social_network.add_node('David')

# add some people to the graph
alice = social_network.add_node('Alice')
bob = social_network.add_node('Bob')
charlie = social_network.add_node('Charlie')
david = social_network.add_node('David')

# add some relationships to the graph
social_network.add_edge('Alice', 'Bob', 3)
social_network.add_edge('Alice', 'Charlie', 2)
social_network.add_edge('Bob', 'Charlie', 1)
social_network.add_edge('Charlie', 'David', 4)

# find the shortest path between Alice and David
# using Dijkstra's algorithm
from heapq import heappop, heappush
def dijkstra(start_node, end_node):
    heap = [(0, start_node, [])]
    visited = set()
    while heap:
        (cost, current_node, path) = heappop(heap)
        if current_node in visited:
            continue
        visited.add(current_node)
        path = path + [current_node]
        if current_node == end_node:
            return path
        for neighbor, weight in current_node.adjacent_nodes.items():
            heappush(heap, (cost + weight, neighbor, path))
    return None

path = dijkstra(alice, david)
print('Shortest path from Alice to David:', ' -> '.join([node.name for node in path]))


# Output
# Shortest path from Alice to David: Alice -> Charlie -> David
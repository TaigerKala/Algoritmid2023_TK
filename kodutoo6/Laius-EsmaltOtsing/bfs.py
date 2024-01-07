
from collections import defaultdict

class Graph:

    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.visited = []

    def BFS(self, s):
        
        jarjekord = []
        jarjekord.append(s)
        self.visited.append(s)

        while jarjekord:
            s = jarjekord.pop(0)
            print(s, end = " ")

            for i in self.graph[s]:
                if i not in self.visited:
                    jarjekord.append(i)
                    self.visited.append(s)

g = Graph()

g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)

g.BFS(2)
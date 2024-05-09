class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start, queue=None, visited=None):
        if queue is None:
            queue = [start]
        if visited is None:
            visited = set()
        if not queue:
            return

        v = queue.pop(0)
        print(v, end=' ')
        visited.add(v)

        for neighbor in self.graph[v]:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)

        self.bfs(None, queue, visited)

# Test the BFS algorithm
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)
print("\nBreadth First Traversal (BFS):")
g.bfs(3)

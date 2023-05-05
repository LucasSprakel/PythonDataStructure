from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def add_edge(self, u, v):
        self.grafo[u-1][v-1] = 1  

    def show_matrix(self):
        for i in range(self.vertices):
            print(self.grafo[i])
    
    def bfs(self, s, t):
        visited = [False] * self.vertices
        queue = deque([[s]])
        visited[s] = True

        while queue:
            path = queue.popleft()
            node = path[-1]
            if node == t:
                return path
            for neighbor in range(self.vertices):
                if self.grafo[node][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

        print("Não há caminho entre os vértices")
        return None

    def dfs(self, s):
        visited = [False] * self.vertices
        stack = deque([s])
        path = []
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                path.append(node)
                for neighbor in reversed(self.grafo[node]):
                    stack.append(neighbor)

        return path

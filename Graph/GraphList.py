from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def add_edge(self, u, v):
        self.grafo[u-1].append(v)


    def show_list(self):
        for i in range(self.vertices):
            print(f'{i+1}:', end='  ')
            for j in self.grafo[i]:
                print(f'{j}  ->', end='  ')
            print('')

    def bfs(self, s, t=None):
        visited = [False] * self.vertices
        queue = []
        path = {}
        queue.append(s)
        visited[s-1] = True
        while queue:
            u = queue.pop(0)
            for v in self.grafo[u-1]:
                if not visited[v-1]:
                    visited[v-1] = True
                    queue.append(v)
                    path[v] = u
                    if t is not None and v == t:
                        return path
        if t is not None:
            return "Não há caminho entre os vértices"
        else:
            return path
      
    
    def dfs(self, source):
        visited = [False] * self.vertices
        stack = []
        path = {}
        stack.append(source)
        while stack:
            u = stack.pop()
            if not visited[u-1]:
                visited[u-1] = True
                for v in self.grafo[u-1]:
                    if not visited[v-1]:
                        stack.append(v)
                        path[v] = u
        return path


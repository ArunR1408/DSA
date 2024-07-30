class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [[] for i in range(v)]
        self.visited = [False] * v
    
    def addEdge(self, src, dest):
        self.adj[src].append(dest)
        self.adj[dest].append(src)
    
    def printArr(self):
        print("Adjacency List Representation of the Graph:")
        for i in range(self.v):
            print(f"{i} -> {' '.join(map(str, self.adj[i]))}")
                
    def dfs(self, k):
        self.visited[k] = True
        print(k, end=' ')
        
        for neighbor in self.adj[k]:
            if not self.visited[neighbor]:
                self.dfs(neighbor)

n = int(input())
print(round(n*(n-1)/2))
obj = Graph(n)

class graph:
    def __init__(self,v):
        self.v=v
        self.adj=[[] for i in range(v)]
        self.visited = [False]*v
       
    def addEdge(self,src,dest):
        self.adj[src].append(dest)
        self.adj[dest].append(src)
       
    def printgraph(self):
        for i in range(v):
            print(i,end="-> ")
            for j in range(len(obj.adj[i])):
                if j==len(obj.adj[i])-1:
                   
                    print(obj.adj[i][j])
                else:
                    print(obj.adj[i][j],end="-> ")
               
           
t=int(input())
for i in range(t) :
    v,e=map(int,input().split())
    obj=graph(v)
    for i in range(e):
        src,dest=map(int,input().split())
        obj.addEdge(src,dest)
    obj.printgraph()  
print('Please enter the number of nodes in the graph')
print('Please enter the number of edges in the graph')
print('Is the graph directed')
print('Adjacency Matrix Representation:')
n=int(input())
m=int(input())
d=input()=='yes'
g=[[0]*n for _ in range(n)]
for row in g:
  print(*row)
for i in range(m):
  print(f'Enter the start node, end node and weight of edge no {i+1}')
  u,v,w=map(int,input().split())
  g[u-1][v-1]=w
  if not d:g[v-1][u-1]=w
print('Adjacency Matrix Representation:')
for row in g:
  print(*row)

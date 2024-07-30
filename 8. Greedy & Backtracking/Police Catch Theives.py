n = int(input())
p = []
t = []

for i in range(n):
  s = input()
  if s == "P":
    p.append(s)
  else:
    t.append(s)
    
if len(p)< len(t):
  print("Maximum thieves caught:",len(p))
else:
  print("Maximum thieves caught:",len(t))
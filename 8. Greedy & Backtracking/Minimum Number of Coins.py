demo = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
demo = demo [::-1]
n = int(input())
res = []
i = 0
while (i< len(demo)):
  while (n >= demo[i]):
    n -= demo[i]
    res.append(demo[i])
  i+=1
for k in range(len(res)):
  print(res[k], end = '  ')
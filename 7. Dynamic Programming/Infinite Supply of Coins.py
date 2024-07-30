def count_ways(coins, n):
  dp = [0] * (n + 1)
  dp[0] = 1
  for coin in coins:
    for i in range(coin, n + 1):
      dp[i] += dp[i - coin]
  return dp[n]

n = int(input())
coins = list(map(int, input().split()))
amount = int(input())
print(count_ways(coins, amount))

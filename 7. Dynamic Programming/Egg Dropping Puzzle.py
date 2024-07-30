def egg_drop(n, k):
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dp[i][1] = 1
        dp[i][0] = 0
    
    for j in range(1, k + 1):
        dp[1][j] = j
    
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            dp[i][j] = float('inf')
            for x in range(1, j + 1):
                res = 1 + max(dp[i - 1][x - 1], dp[i][j - x])
                if res < dp[i][j]:
                    dp[i][j] = res

    return dp[n][k]

T = int(input().strip())
results = []

for _ in range(T):
    N, K = map(int, input().strip().split())
    results.append(egg_drop(N, K))

for result in results:
    print(result)

def max_money(coins):
    n = len(coins)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    for length in range(1, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            a = dp[i+2][j] if (i + 2) <= j else 0
            b = dp[i+1][j-1] if (i + 1) <= (j - 1) else 0
            c = dp[i][j-2] if i <= (j - 2) else 0
            
            dp[i][j] = max(coins[i] + min(a, b), coins[j] + min(b, c))
    
    return dp[0][n-1]

n = int(input().strip())
coins = list(map(int, input().strip().split()))
print(max_money(coins))
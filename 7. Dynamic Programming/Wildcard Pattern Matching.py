'''
a = input()
b = input()
bl = list(b)
if bl[0] in a and bl[-1] in a:
  print('true')
else: 
  print('false')
  '''

def isMatch(s, p):
    m, n = len(s), len(p)

    # Create a 2D DP table to store matching information
    dp = [[False] * (n + 1) for _ in range(m + 1)]

   
    dp[0][0] = True

  
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]

    return dp[m][n]

str = input()
pattern = input()

if isMatch(str, pattern):
    print("true")
else:
    print("false")

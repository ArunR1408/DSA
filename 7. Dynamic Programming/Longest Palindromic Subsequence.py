def longest_palindromic_subsequence(s):
    n = len(s)
    # Initialize the dp table
    dp = [[0] * n for _ in range(n)]
    
    # All subsequences of length 1 are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Check subsequences of length 2 to n
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    # Return the length of LPS
    return dp[0][n-1]

# Main function to handle input and output
def main():
    # Read input from stdin
    s = input().strip()
    
    # Calculate the length of the longest palindromic subsequence
    result = longest_palindromic_subsequence(s)
    
    # Print the result to stdout
    print(result)

if __name__ == "__main__":
    main()
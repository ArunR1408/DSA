'''
Longest Common Subsequence

Given two strings, 'x' and 'y'. Find the length of their Longest Common subsequence (LCS). The two strings contains only lowercase
letters. Write a program that takes in two strings as inputs and returns the length of their LCS.

Format:

input:

The input is a string of 'x' and 'y'.

Output:

Return the length of the LCS of 'x' and 'y'.

Example 1:

input:

ab

ababa

Output:

3

Explanation:

The length of the "Longest Common Subsequence" is 3 that is "aba".
'''

def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X, Y, m-1, n-1)
    else:
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))


# Driver code
if __name__ == '__main__':
    S1 = input()
    S2 = input()
    print(lcs(S1, S2, len(S1), len(S2)))

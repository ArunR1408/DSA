# Day7 Quiz Code

'''
You have n batches with some numbers written on them given in the form of array A, you have to distribute all the batches to n persons equally but before that you have to do one operation before giving ith batch-
When you are giving ith batch to ith person then you will get a number (A[i - 1] * A[i] * A[i + 1]) and if i-1th and i + 1th number goes out bound then just take their values as 1.

You have to print the maximum number you can make by distributing batches wisely by counting all number formed in above said manner for each batch.

Input Format:
First line of input contain one integer N - size of the array.
Second line of input will contain N space separated integers.

Output Format:
Print the maximum number you can make.

Sample Input 1:

4

3158

Sample Output 1:
167

Explanation:
A =[3,1,5,8] -- > [3,5,8] -- >[3,8] -- >[8] -- >[]
total number = 3*1*5+ 3*5*8+ 1*3*8+ 1*8*1 = 167

Sample Input 2:

2

15

Sample Output 2:
10

Constraints:
. n == Array length
. 1 <= n <= 500
. 0 <= A[i <= 100
'''
def mx(ns):
    ns = [1] + ns + [1]
    n = len(ns)
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n):
        for left in range(n - length):
            right = left + length
            for i in range(left + 1, right):
                dp[left][right] = max(dp[left][right],
                                      ns[left] * ns[i] * ns[right] +
                                      dp[left][i] + dp[i][right])

    return dp[0][n-1]

n = int(input())
ns = list(map(int, input().split()))
result = mx(ns)
print(result)
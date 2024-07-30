'''
Longest Increasing Subsequence

Given an integer array 'A'. Find the length of its Longest Increasing Subsequence of a sub-array from the given integer array. The
elements are sorted in monotonic increasing order. You need to create a function that takes two inputs - integer 'n' and an integer
array containing 'n' integers. To return the length of its LIS.

Format:

Input:

The integer input is 'n'. And Integer array A input, contains n integers.

Output:

Return the length of its LIS.

Constraint:

1 <= input1 <= 1000

'''

n = int(input())
#ex i/p
#l = [10, 22, 9, 33, 21, 50, 41, 60]

l = list(map(int,input().split()))

dp=[1]*n

for i in range(n):
    for j in range(i):
        if (l[j]<l[i]):
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))
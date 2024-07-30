'''
Q. Repeatedly find the sum of digits of a number until it becomes a single digit number (say sod). 
Then compute the factorial of sod and print it.

Input format
Integer n 
Output format
Number denoting the factorial of single digit

Sample Input
23
Sample Output
120

Test Cases
78 -> 20
84 -> 6
'''

import math

def sum_of_digits(n):
    # Function to calculate the sum of the digits of a number
    return sum(int(digit) for digit in str(n))

def single_digit_sum(n):
    # Function to repeatedly sum the digits until a single-digit is obtained
    while n > 9:
        n = sum_of_digits(n)
    return n

# Input
n = int(input("Enter an integer: "))

# Calculate the single-digit sum
sod = single_digit_sum(n)

# Calculate and print the factorial of the single-digit sum
result = math.factorial(sod)
print(result)


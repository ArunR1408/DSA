def longest_balanced_parentheses(s):
    # Stack to keep track of the indices of the parentheses
    stack = [-1]
    max_length = 0

    for i, char in enumerate(s):
        if char == '(':
            # Push the index of the '(' onto the stack
            stack.append(i)
        else:
            # Pop the last index from the stack
            stack.pop()
            if stack:
                # If the stack is not empty, calculate the length of the current balanced parentheses
                max_length = max(max_length, i - stack[-1])
            else:
                # If the stack is empty, push the current index onto the stack
                stack.append(i)

    return max_length

# Input string
expression = input()

# Output the longest length of balanced parentheses
result = longest_balanced_parentheses(expression)
print( result)

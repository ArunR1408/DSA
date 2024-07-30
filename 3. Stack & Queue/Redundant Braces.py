def has_redundant_braces(expression):
    # Create an empty stack
    stack = []

    for char in expression:
        # If current character is a closing bracket ')'
        if char == ')':
            top = stack.pop()
            elements_inside_braces = 0

            # Count elements inside the current pair of brackets
            while top != '(':
                elements_inside_braces += 1
                top = stack.pop()

            # If there are less than 2 elements inside the braces, they are redundant
            if elements_inside_braces < 2:
                return 'Yes'
        else:
            # Push other characters onto the stack
            stack.append(char)

    return 'No'

# Input string
expression = input()

# Output whether the expression has redundant braces or not
result = has_redundant_braces(expression)
print(result)

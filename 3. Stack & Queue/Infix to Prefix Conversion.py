def infix_to_prefix(expression):
    # Helper function to check the precedence of operators
    def precedence(op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0

    # Helper function to perform the infix to postfix conversion
    def infix_to_postfix(expression):
        stack = []
        postfix = []
        for char in expression:
            if char.isdigit():
                postfix.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
            else:
                while stack and precedence(stack[-1]) >= precedence(char):
                    postfix.append(stack.pop())
                stack.append(char)

        while stack:
            postfix.append(stack.pop())

        return ''.join(postfix)

    # Reverse the infix expression
    expression = expression[::-1]

    # Replace '(' with ')' and vice versa
    expression = ''.join(['(' if char == ')' else ')' if char == '(' else char for char in expression])

    # Convert the modified infix expression to postfix notation
    postfix_expression = infix_to_postfix(expression)

    # Reverse the postfix expression to get the prefix notation
    prefix_expression = postfix_expression[::-1]

    return prefix_expression

# Input string
expression = input()

# Output the corresponding prefix expression
result = infix_to_prefix(expression)
print(result)

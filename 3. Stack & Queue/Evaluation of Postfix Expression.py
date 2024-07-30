def evaluate_postfix(expression):
    stack = []
    for char in expression:
        if char.isdigit():  # Check if the character is an operand
            stack.append(int(char))
        else:  # The character is an operator
            right_operand = stack.pop()
            left_operand = stack.pop()
            
            if char == '+':
                result = left_operand + right_operand
            elif char == '-':
                result = left_operand - right_operand
            elif char == '*':
                result = left_operand * right_operand
            elif char == '/':
                result = left_operand // right_operand  # Integer division
            
            stack.append(result)
    
    return stack[0]  # The final result will be the only item left in the stack

# Input number of test cases
T = int(input().strip())

# Process each test case
for _ in range(T):
    postfix_expression = input().strip()
    result = evaluate_postfix(postfix_expression)
    print(result)

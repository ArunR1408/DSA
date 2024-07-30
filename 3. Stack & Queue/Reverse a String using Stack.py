def reverse_string_using_stack(input_string):
    # Create an empty stack
    stack = []

    # Push each character of the input string onto the stack
    for char in input_string:
        stack.append(char)

    # Pop each character from the stack and build the reversed string
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()

    return reversed_string

# Input string
input_string = input()

# Output the reversed string
output_string = reverse_string_using_stack(input_string)
print(output_string)

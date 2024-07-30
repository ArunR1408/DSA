def sum_of_natural_numbers(start, end):

  n = end - start + 1
  return n * (start + end) // 2

start, end = map(int, input().split())
result = sum_of_natural_numbers(start, end)
print(result)

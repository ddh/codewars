"""
Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

Examples
basic_op('+', 4, 7)         # Output: 11
basic_op('-', 15, 18)       # Output: -3
basic_op('*', 5, 5)         # Output: 25
basic_op('/', 49, 7)        # Output: 7
"""
def basic_op(operator, value1, value2):
  # code here
  if operator == '+':
    return value1 + value2
  if operator == '-':
    return value1 - value2
  if operator == '*':
    return value1 * value2
  if operator == '/':
    return value1 / value2

# driver
print(basic_op('+', 4, 7))         # Output: 11
print(basic_op('-', 15, 18))       # Output: -3
print(basic_op('*', 5, 5))         # Output: 25
print(basic_op('/', 49, 7))        # Output: 7

# Try doing this with only using addition: sum or +
def basic_op2(operator, value1, value2):
  if operator == '+':
    return value1 + value2
  if operator == '-':
    return value1 + -value2
  if operator == '*':
    return sum([value1 for n in range(value2)])
  if operator == '/':
    count = 0
    while value1 != 0:
      value1 += -value2
      count += 1
    return count

# driver
print(basic_op2('+', 4, 7))         # Output: 11
print(basic_op2('-', 15, 18))       # Output: -3
print(basic_op2('*', 5, 5))         # Output: 25
print(basic_op2('/', 49, 7))        # Output: 7
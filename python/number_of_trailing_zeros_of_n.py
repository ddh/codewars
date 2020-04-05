"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 * ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html

Examples
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.
"""
# Notes
# How do you get 10 = 2 * 5, 20 = 2 * 2 * 5, 30 = 2 * 3 * 5, 40 = 2 * 2 * 2 * 5. Notice there is a 2,5 in each case. Then 100, another pair of 2, 5
# Idea: Find the number of 2,5 pairs from the factors. The numer of pairs equals the number of 0s
# Or, just divide by 10 successfully until mod?
# eg 720 % 10 ==
# 1,[2],3,[2,2],[5],[2,3],7,[2,2,2],9,[2,5],11,12,13,14,15

def zeros(n):
  zero_count = 0
  ten_factor_pair = 0
  for num in range(1, n + 1):
    if num % 10 == 0:
      zero_count += 
    elif num % 2 == 0:
      ten_factor_pair += 1
    elif n % 5 == 0:
      ten_factor_pair += 1
  # while n % 10 == 0:
  #   zero_count += 1
  #   n = n // 10
  print(100/10)
  return zero_count +

# Driver
print(zeros(6)) # 1
print(zeros(12)) # 2
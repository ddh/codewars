def tribonacci(signature, n):
  tribonacci_numbers = signature
  for i in range(n):
    current_sum = sum(tribonacci_numbers[i:i+3])
    tribonacci_numbers.append(current_sum)
  return tribonacci_numbers[:n]

# Not so readable
def tribonacci_unreadable(signature, n):
  [signature.append(sum(signature[i:i+3])) for i in range(n)]
  return signature[:n]

print(tribonacci([1,1,1],10))
print(tribonacci_unreadable([1,1,1],10))
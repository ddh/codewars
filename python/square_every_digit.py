def square_digits(num):
  numbers = [char for char in str(num)]
  return int(''.join([str(int(number) ** 2) for number in numbers]))

square_digits(9119)
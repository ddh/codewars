def array_diff(a, b):
  return [x for y in b for x in a if x != y ]
  # z = []
  # for x in a:
  #   for y in b:
  #     if x != y:
  #       z.append(x)
  # return z
print(array_diff([1,2,2], [1]))


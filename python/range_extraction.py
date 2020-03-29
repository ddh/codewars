"""
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example ("12, 13, 15-17")
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
"""

# idea:
# save current_index
# if in range mode
#   is next number consecutive
#     # No? then exit range mode and append to string current number and append running string into array
# If not in range mode
#   # Check if possible range exist (three numbers)
#     # If possible range exists, turn on range mode and store 'currentnumber + -'
    # Else append current number

def solution(args):
  extracted_nums = []
  range_mode = False
  range_string = None
  for i, num in enumerate(args):
    if range_mode:
      # Break out of range mode if on last index or if next number is not contiguous
      if i == len(args) - 1 or args[i + 1] != num + 1:
        range_mode = False
        extracted_nums.append(f'{range_string}{str(num)}')
    else:
      # Toggle range mode if there's two numbers ahead and they are contiguous
      if i < len(args) - 2 and args[i + 2] - num == 2:
        range_mode = True
        range_string = str(f'{num}-')
      else:
        extracted_nums.append(str(num))
  return ','.join(extracted_nums)

# Driver
print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
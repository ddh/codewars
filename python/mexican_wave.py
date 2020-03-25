"""
Task
 	In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up.
Rules
 	1.  The input string will always be lower case but maybe empty.
  2.  If the character in the string is whitespace then pass over it as if it was an empty seat.
Example
  wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
  " gap " -> result = [" Gap ", " gAp ", " gaP "]

"""

def wave(people):
  current_stander = 0
  output = []
  while current_stander < len(people):
    if people[current_stander] != ' ':
      output.append(''.join([char.upper() if i == current_stander else char for i, char in enumerate(people)]))
    current_stander += 1
  return output

# Driver
print(wave("hel lo"))

# Post-submission notes:
print("h".isalpha()) # True
print("1".isalpha()) # False
print("-".isalpha()) # False
print("_".isalpha()) # False
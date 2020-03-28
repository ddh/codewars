"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
"""

def is_isogram(string):
    chars = {}
    for char in string.lower():
      if char in chars:
        return False
      chars[char] = True
    return True

# Driver:
print(is_isogram("Dermatoglyphics" )) # == true
print(is_isogram("aba" )) # == false
print(is_isogram("moOse" )) # == false

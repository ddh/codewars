def duplicate_count(text):
    chars = {}

    # For each character, increment occurrence in dictionary
    for char in text.lower():
      chars[char] = chars.get(char, 0) + 1 # Init with 0 if no value present

    # dictionary comprehension; finds the chars that have more than 1 occurrence
    return len({ k: v for k, v in chars.items() if v >= 2 })
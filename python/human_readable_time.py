"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""

def make_readable(seconds):
  HOURS_IN_SEC = 3600
  MIN_IN_SEC = 60

  hours = int(seconds / HOURS_IN_SEC)
  remaining_seconds = seconds - hours * HOURS_IN_SEC
  minutes = int(remaining_seconds / MIN_IN_SEC)
  remaining_seconds -= minutes * MIN_IN_SEC

  return f'{hours:02}:{minutes:02}:{remaining_seconds:02}'

# Driver
print(make_readable(0)) # "00:00:00"
print(make_readable(86399)) # "23:59:59"
print(make_readable(86399)) # "00:01:00"
print(make_readable(86399)) # "23:59:59"
print(make_readable(359999)) # 99:59:59"
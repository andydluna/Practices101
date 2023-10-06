"""
try: 
  # some line of codes
expect <ERROR1>:
  # handler <ERROR1>
except <ERROR2>:
  # handles <ERROR2>
else:
  # no exceptions were raised, the code ran successfully
finally:
  # do something in any case
"""

try:
  result = 2 / 0
except ZeroDivisionError:
  print('Cannot divide by zero!')
finally:
  result = 1

print(result)

try:
  raise Exception('An error!')
except Exception as error:
  print(error)

class DogNotFoundException(Exception):
  print('Inside')
  pass

try:
  raise DogNotFoundException()
except DogNotFoundException:
  print('Dog not fonud!')


#Program that calculates the sum of a list of numbers
def addNumbers(numbers):
  total = 0
  for n in numbers:
    total += n
  return total

print(addNumbers([8, 10, 2, 3]))
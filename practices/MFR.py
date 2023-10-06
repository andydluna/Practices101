from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

result = map(lambda a : a * 2, numbers)
#Best way to do it
#generator = (num * 2 for num in numbers)  

print(list(result))

result = filter(lambda n : n % 2 == 0, numbers)

print(list(result))

expenses = [
  ('Dinner', 80), ('Car repair', 120)
]

sum = reduce(lambda a, b: a[1] + b[1], expenses)

print(sum)

#Another example of reduce
strings = ['a1', 'b2', 'c3', 'd4', 'e5']
result = reduce(lambda a, b: f'{a}-{b}', strings, 'INIT')
print(result)
filename = '/Users/Andy/test.txt'

with open(filename, 'r') as file:
  content = file.read()
  print(content)
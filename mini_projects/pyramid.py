#Program that prints a pyramid using *
def pyramid(n):
  spaces = n-1
  for num in range(1, 2*n, 2):
    print(' '*spaces+'*'*num)
    spaces = spaces - 1

pyramid(10)
pyramid(5)
pyramid(25)

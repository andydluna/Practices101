'''
Practice of OOP using polymorphism
'''

class Shape():
  def __init__(self, base, height):
    self.base = base
    self.height = height

  def calcArea(self):
    return self.base * self.height

  def calcPerimeter(self):
    return self.base * 2 + self.height * 2

class Square(Shape):
  def __init__(self, length):
    super().__init__(length, length)

class Rectangle(Shape):
  def __init__(self, base, height):
    super().__init__(base, height)

class Triangle(Shape):
  def __init__(self, base, height, a, b, c):
    super().__init__(base, height)
    self.a = a
    self.b = b
    self.c = c

  def calcArea(self):
    return (self.base * self.height) / 2

  def calcPerimeter(self):
    return self.a + self.b + self.c

listOfShapes = [Square(5), Rectangle(5, 2), Triangle(5, 10, 10, 20, 30)]
for shape in listOfShapes:
  print(shape.calcArea(), shape.calcPerimeter())
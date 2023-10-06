'''
Practice using OOP and polymorphism
'''

class Mammal():
  def __init__(self, name):
    self.name = name

  def makeSound(self):
    return self.name + " does not have a registered sound."

class Dog(Mammal):
  def __init__(self, name):
    super().__init__(name)

  def makeSound(self):
    return "Woof!"

class Cat(Mammal):
  def __init__(self, name):
    super().__init__(name)

  def makeSound(self):
    return "Meow!"

class Rat(Mammal):
  def __init__(self, name):
    super().__init__(name)

  def makeSound(self):
    return "Squeak!"

class Giraffe(Mammal):
  def __init__(self, name):
    super().__init__(name)

listOfAnimals = [Dog('Naafiri'), Cat('Yuumi'), Rat('Twitch'), Giraffe('Melman')]
for animal in listOfAnimals:
  print(animal.makeSound())
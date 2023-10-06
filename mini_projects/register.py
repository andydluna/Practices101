'''
Program that gives a value to different items in a list
and adds them up returning the total sum

Practicing classes
'''
class Item:
  def __init__(self, name, price):
    self.name = name
    self.price = price


def addPrice(items):
  total = 0
  
  for item in items:
    total += item.price
      
  return total

print(addPrice([Item('APPLE', 3), Item('BANANA', 2), 
                Item('STRAWBERRY', 5), Item('PINEAPPLE', 1)]))
print(addPrice([Item('APPLE', 3), Item('BANANA', 2), 
                Item('STRAWBERRY', 5), Item('PINEAPPLE', 1), Item('NONE', 0)]))
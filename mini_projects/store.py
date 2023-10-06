'''
Program that uses an interface called Store to store 
a shopping cart and has functions to add, remove, and show the items from cart,
and display the total price of the items. 
'''
class Store:
  def __init__(self):
    self.__cart = []

  def addToCart(self, item):
    self.__cart.append(item)

  def removeFromCart(self, index):
    try:
      self.__cart.pop(int(index))
    except (IndexError, ValueError):
      print('Oops! That was not a valid index. Please try again...')

  def displayTotal(self):
    if (self.__cart != []):
      total = 0
      for item in self.__cart:
        total += float(item.price)
      print ('Total: ${0}'.format(total))
  
  def displayCart(self):
    if (self.__cart != []):
      for n in range(0, len(self.__cart)):
        item = self.__cart[n]
        print ('Item: #{0}: {1} ----- ${2}'.format(n, item.name, item.price))

'''
Class that stores an item given a name and a price
'''
class Item:
  def __init__(self, name, price):
    self.name = name
    self.price = price

store = Store()

print('Welcome to our store!')

# Loop that runs the program until the user types the exit command (x)
while(True):
  store.displayCart()
  store.displayTotal()

  print('Press a to add an item')
  print('Press r to remove an item')
  print('Press x to exit.')

  userInput = input('Please enter a command: ')

  if userInput == 'x':
    break
  elif userInput == 'a':
    itemName = input('Please give the item a name: ')
    try:
      itemPrice = float(input('Please provide a price for the item:  ')) 
      store.addToCart(Item(itemName, itemPrice))
    except ValueError:
      print('Oops! That was not a valid price value. Please try again...')
  elif userInput == 'r':
    index = input('Please enter the index of the item to remove: ')
    store.removeFromCart(index)
  else:
    print('Please provide a valid input')

  print('-'*30)
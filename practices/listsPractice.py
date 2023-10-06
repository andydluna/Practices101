listOfNumbers = []

listOfNumbers.append(5)
print(listOfNumbers)
listOfNumbers.append(50)
print(listOfNumbers)

listOfNumbers.insert(0, 10)
print(listOfNumbers)
listOfNumbers.insert(2, 10)
print(listOfNumbers)

listOfNumbers.extend([1, 2, 3, 4, 5])
print(listOfNumbers)

listOfNumbers.remove(10)
print(listOfNumbers)
listOfNumbers.remove(10)
print(listOfNumbers)

listOfNumbers.pop()
print(listOfNumbers)
listOfNumbers.pop(1)
print(listOfNumbers)

listOfNumbers.clear()
print(listOfNumbers)
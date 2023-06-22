myList = [1, 2, 3, 4, 5]
print(myList)

# Updating the list
myList[0] = 11
print(myList)

# inserting into the list
myList.insert(4, 55)
print(myList)

# append
myList.append(66)
print(myList)

# extend - add list to another list
myList2 = ['a', 'b', 'c']
myList.extend(myList2)
print(myList)
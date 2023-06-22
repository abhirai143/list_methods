# Remove method

list1 = ["apple", "banana", "cherry"]
list1.remove("banana")
print(list1) # ['apple', 'cherry']

# Pop method

list2 = ["apple", "banana", "cherry"]
list2.pop(1)
print(list2) # ['apple', 'cherry']

list2.pop() # remove last item in list
print(list2)

# Del method

list3 = ["apple", "banana", "cherry"]
del list3[0]
print(list3) # ['banana', 'cherry']

# delete entire list

del list3


# clear method - empties the list. The list still remains, but it has no content.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

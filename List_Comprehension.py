# without list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist1 = []

for x in fruits:
    if "a" in x:
        newlist1.append(x)

print(newlist1)


# after list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist2 = [x for x in fruits if "a" in x]

print(newlist2)

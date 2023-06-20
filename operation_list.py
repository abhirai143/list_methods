myList = list()
while (True):
    input = input('Enter a number ')
    if input == 'done': break
    value = float(input)
    myList.append(value)
avg = sum(myList) / len(myList)

print("average=", avg)
print(myList)

# Linear search method

myList=[10,20,30,40,50,60]
def search(list,value):
    for i in list:
        if i==value:
            return 'Element found at index ' + str(list.index(value))
    return 'Element not found'
print(search(myList,30))

#Using IN Operator

def searchIN(list,value):
    if value in list:
        return 'Element found at index' + str(list.index(value))
    return 'Element Not Found'
print(searchIN(myList,50))
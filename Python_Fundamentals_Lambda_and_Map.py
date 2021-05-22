# Code 1
oddEven = lambda x : print('Even') if(x % 2 == 0) else print('Odd')
oddEven(5)

oddEven(6)

# Code 2
def oddEven(x):
    if x%2 == 0:
        print('Even')
    else:
        print('Odd')

oddEven(5)

oddEven(6)  

# Code 3
listOfElements = [-1,2,-3]
listReturned = map(lambda x: abs(x),listOfElements)
print(list(listReturned))

[1, 2, 3]

# Code 4
listReturned = map(abs,listOfElements)
print(list(listReturned))

[1, 2, 3]

# Code 5
a = [1,2,3]
b = [1,2,3]
result = list(map(lambda x,y: x+y,a,b))

print(result)
[2, 4, 6]
# Code 1
from functools import reduce
def findMax(x,y):
    if x > y: return x
    else: return y
    
b = [3,2,4,5,1,6]

reduce(findMax,b)
6

# with lambda
reduce(lambda x,y: x if x > y else y,b)

# Code 2
a = [1,2,3,4,5,6]

b = list(filter(lambda x: x % 2 == 0,a))

print(b)
[2, 4, 6]

# Code 3
a = [0,1,False,True,'a']

b = list(filter(None,a))

print(b)
[1, True, 'a']
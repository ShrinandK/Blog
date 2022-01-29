# Decorators
# function defined
def upperFunc(func):
    # args and kwargs allow function to have any
    # arguments
    def innerFunc(*args,**kwargs):
        tempList = [varibs for varibs in args]
        if tempList[0] == 0 or tempList[1] == 0:
            return 'Zeros not allowed.'
        else:
            return func(*args,**kwargs)
    return innerFunc

# Decorator added to multiplyForCheck function
@upperFunc
def multiplyForCheck(a,b):
    return a*b

# Decorator added to addForCheck function
@upperFunc
def addForCheck(a,b):
    return a+b
    
# Calling the function
x = multiplyForCheck(3,2)
y = multiplyForCheck(3,0)
print(x)
print(y)
x = addForCheck(3,2)
y = addForCheck(3,0)
print(x)
print(y)

# Higher Order with Function as input

# define average function
def average(nums):
    return sum(nums)/len(nums)

# main function which can take any 
# function as input and runs that
def main(functionName,numList):
    result = functionName(numList)
    print(result)
    
# passing the average function to main function
main(average,[1,2,3,4])

# Higher Order with Returning function

# defining average function
def average(nums):
    return sum(nums)/len(nums)

# defining summation function
def summation(nums):
    return sum(nums)

# main function which returns function depending
# on the selection
def main(selection):
    if selection == 1:
        return average
    else:
        return summation
    
# calling option 1
returnFunction = main(1)
# the function returned here is average
print(returnFunction([1,2,3,4]))

# calling option 2
returnFunction = main(2)
# the function returned here is summation
print(returnFunction([1,2,3,4])) 

# Closures
# function defined with nested functions
def upperFunction(v):    
    def nestedFunction(a,b):        
        return a*b*v
    return nestedFunction

# creating closure
closureFunc = upperFunction(5)
# trying it out on different combinations 
print(closureFunc(3,3))
print(closureFunc(3,6))
print(closureFunc(4,6))
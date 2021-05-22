# Code 1
newString = 'Python'
individualChar = []
for letter in newString:
    individualChar.append(letter)
print(individualChar)

# Code 2
newString = 'Python'
individualChar = [letter for letter in newString]
print(individualChar)

# Code 3
numList = [1,2,3,4,5,6,7,8,9]
evenList = [num for num in numList if num % 2 == 0]
print(evenList)

# Code 4
studentScore = [45,50,35,60]
passFailList = [str(score) + ':Pass' if score > 40 else str(score) + ':Fail' for score in studentScore]
print(passFailList)

# Code 5
listOFList = [[1,2,3],[4,5,1]]
getSingleElement = [element for singleList in listOFList for element in singleList]
print(getSingleElement)

# Code 6
listOFList = [[1,2,3],[4,5,6]]
getSingleElement = [element for singleList in listOFList for element in singleList if element % 2 == 0]
print(getSingleElement)

# Code 7
studentList = ['A','B','C']
scoreList = [60,70,90]
studentDict = {}
for (key,value) in zip(studentList,scoreList):
    studentDict[key] = value
print(studentDict)

# Code 8
studentList = ['A','B','C']
scoreList = [60,70,90]
studentDict = {key:value for (key,value) in zip(studentList,scoreList)}
print(studentDict)

# Code 9
tempValueInDeg = {'CityA': 23,'CityB': 34, 'CityC': 13}
kelvinConst = 273
tempValueInKel = {key:value + kelvinConst for key,value in tempValueInDeg.items()}
print(tempValueInKel)

# Code 10
# if case
studentDict = {'A': 60, 'B': 70, 'C': 95}
newStudentDict = {key:value for (key,value) in studentDict.items() if value % 10 == 0}
print(newStudentDict)

# if-else case
studentDict = {'A': 30, 'B': 70, 'C': 95}
newStudentDict = {key:('Pass' if value > 40 else 'Fail') for (key,value) in studentDict.items()}
print(newStudentDict)

# Code 11
numSet = {1,2,3,4,5,6,7}
newSet = set()
for s in numSet:
    if s%2 == 0: 
        newSet.add(s)
print(newSet)

# Code 12
numSet = {1,2,3,4,5,6,7}
newSet = {s+2 if s % 2 == 0 else s+2 for s in numSet}
print(newSet)

#Note: a function can also accept another function as an argument.
# def doBreakfast(item, count, brush):
#     brush()
#     print(f"I'm having {count} {item} in the Breakfast")


# def doBrush():
#     print("I've done with brushing activity.")

# doBreakfast("Pao Bhaji", 3, doBrush)


import random

# def welcome(getName):
#     print(f"{getName()} - Welcome To Chitkara University!")

# def getName():
#     return random.choice(["Chintu", "Chunnu", "Pawan", "Bhola"])


# welcome(getName)


#Note: a function can also return another function.


# def welcome(getName):
#     def welcomeStudent():
#         print(f"{getName()} - Welcome To Chitkara University!")

#     return welcomeStudent

# def getName():
#     return random.choice(["Chintu", "Chunnu", "Pawan", "Bhola"])

# fun = welcome(getName)
# fun()

#Higher Order Function: A function which can take another function as an argument and also return another functon.
#Python Inbuilt Higher Order Function:- map(), filter()
#1. map(function, iterable)
#2. filter(function, iterable)

#1. map(function, iterable): it used to transform/modified/update the sequence/collection and return that transform collection/sequence.


#Example 1: Find out the square of each numbers in the below list into seperate list.

# nums = [1,2,3,4,5,6,7,8,9,10] 

#Traditional Method:

#1.
# def makeSquare(num):
#     return num**2

# squareList1 = []
# for i in nums:
#     squareList1.append(makeSquare(i))

#2.
# squareList2 = [x**2 for x in nums]

#3. Using HOF: map

#list(HOF) - it takes higher order function and return list.
# list1 = list(range(1, 11))
# print(list1)

# nums = [1,2,3,4,5,6,7,8,9,10] 

# def makeSquare1(num):
#     return num**2

# makeSquare2 = lambda num : num**2

# squareList3 = list(map(makeSquare1, nums))
# squareList3 = list(map(makeSquare2, nums))
# squareList3 = list(map(lambda num : num**2, nums))
# print(squareList3)


#Example 2: Given a list of numbers make square of those number which are even and keep rest number as it is into another list.

# def makeEvenSquare1(num):
#     if num%2==0:
#         return num**2
#     else:
#         return num

# makeEvenSquare2 = lambda num : num**2 if num%2==0 else num
    
# nums = [1,2,3,4,5,6,7,8,9,10]

# oddSqaureCumEvenSquareList = list(map(makeEvenSquare1, nums))
# oddSqaureCumEvenSquareList = list(map(makeEvenSquare2, nums))
# oddSqaureCumEvenSquareList = list(map(lambda num : num**2 if num%2==0 else num, nums))

# print(oddSqaureCumEvenSquareList)


#Example 3: Given a list of numbers make square of those number which are divisibleBy4 and keep rest number as it is into another list.

# restSameThreeDivisibleSquareList = list(map(lambda num : num**2 if num%3==0 else num, nums))
# print(restSameThreeDivisibleSquareList)

#2. filter(function, iterbale): it used to filter the element from list based on the condition and returns filtered list.

# nums = [1,2,3,4,5,6,7,8,9,10]

#Example 1: get the list of those elements only which are divisibleBy3

# def checkDivisibleByThree1(num):
#     return num%3==0

# checkDivisibleByThree2 = lambda num : num%3==0   

# onlyDivisibleBy3List = list(filter(checkDivisibleByThree1,nums))
# onlyDivisibleBy3List = list(filter(checkDivisibleByThree2,nums))
# onlyDivisibleBy3List = list(filter(lambda num : num%3==0,nums))
# print(onlyDivisibleBy3List)



#3. reduce(function, iterable): it reduces the list and return the single value.
#Note: above reduce() is not the inbuilt function of python, it comes from functools module.

from functools import reduce

# nums = [1,2,3,4,5]

# def findSum1(a,b):
#     return a+b

# findSum2 = lambda a, b: a + b 

# sum = reduce(findSum1, nums)
# sum = reduce(findSum2, nums)
# sum = reduce(lambda a, b: a + b , nums, 10)
# print(sum)

nums = [1,2,3,4,5,6,7,8,9,10]

#Example: find out the sum even number

# evenNums = list(filter(lambda num: num%2==0, nums))
# sum = reduce(lambda a , b : a + b, evenNums)
# evenNums = list(filter(lambda num: num%2==0, nums))
# sum = reduce(lambda a , b : a + b, list(filter(lambda num: num%2==0, nums)))
# print(sum)



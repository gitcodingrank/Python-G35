#Example: 

#Declared a function with name isEven
# def isEvenOrOdd(num):
#     if num%2==0:
#         print("Even")
#     else:
#         print("Odd")


# #Calling the Function
# #Argument: actual value that you pass to the function at the time of calling.
# isEvenOrOdd(5) #Odd
# isEvenOrOdd(6) #Even
# isEvenOrOdd(11) #Odd


#Student Task 1: Create a function that checks a number is prime or not.

# def isPrime(num):
#     count = 0
#     for i in range (1, num+1):
#         if num%i==0:
#             count+=1
#     if count==2:
#         print(f"{num} is Prime")
#     else:
#         print(f"{num} is not Prime")

# isPrime(5) #Its Prime
# isPrime(4) #Its Not Prime
# isPrime(6) #Its Not Prime


#Student Task 2: Create a function that checks a number is prime or not and print number from 1 to 20

# for i in range(1,21):
#     isPrime(i)


#Student Task 3: Create a function that prints the value of list in one line.

# def printListElementInOneLine(list):
#     for i in list:
#         print(i, end=' ')


# numsList = [1,2,3,4,5,6,7,8,9,10]
# printListElementInOneLine(numsList)

# print()

# names = ['Pankaj', 'Shivam', 'Rohan', 'Sushil', 'Chintu']
# printListElementInOneLine(names)


#Student Task 4: Create a function that accepts number list and your task is to print the sum and average of list element.

# def numberListSumAndAverage(numsList):
#     sum = 0
#     for num in numsList:
#         sum+=num
#     print("Sum of All Numbers:",sum)
#     print("Average of All Numbers:",sum/len(numsList))

# # numbers = [1,2,3,4,5,6,7,8,9,10]
# numberListSumAndAverage([1,2,3,4,5,6,7,8,9,10])

#Student Task 5: Create a function that accepts the list and count the number of element in the list.

# def countElementInTheList(list):
#     count = 0
#     for i in list:
#         count+=1
#     print("Total Number of Element in the List:",count)

# countElementInTheList([1,2,3,4,5,6,7,8,9,10])

#Student Task 6: Create a function that accepts the number list and also print the minimum number of the list.

# def printMinimumNumberInTheList(numList):
#     minValue = numList[0]
#     for i in range(1, len(numList)):
#         if minValue > numList[i]:
#             minValue = numList[i]
#     print("Minimum Value is:",minValue)

# numberList = [ 45,56,77,2,54,12,11,3,4,5,78]
# printMinimumNumberInTheList(numberList)

# printMinimumNumberInTheList([3,4,5,-1,34])

#Student Task 7: Create a function that accepts the number list and also print the maximum number of the list.

#Now, I want my function rather then executing the result immediately it must return that result so that i can execute whenever i need to execute.

#Solution: return expression

# def add(a, b):
#     return a+b

# result = add(2,5)
#           # 7
# print(result)


# def isEven(num):
#     if num%2==0:
#         return True
#     else:
#         return False

# result1 = isEven(12) 
             #Even

# if result1:
#     print("Number is Even")
# else:
#     print("Number is not Even")

# result2 = isEven(13)
             #Odd

# if isEven(13):
#     print("Number is Even")
# else:
#     print("Number is not Even")

# print(result1)
# print(result2)

#Problem Statement: Print even number from 1 to 10

# for i in range(1,11):
#     if isEven(i):
#         print(i,end=" ")


"""
In Python, There are two types of function:

1. User-Defined/Custom Function: These functions you create according to your requirement. 
2. Pre-Defined/Inbuilt Function: These functions are already created by some developer therefore rather than creating from the beginning you can use these functions.
"""

#User-Defined/Custom Function:
def countElementInList(numList):
    count=0
    for i in numList:
        count+=1
    print("Count is: ",count)

#Pre-Defined/Inbuilt Function

len(list)

#Inbuilt function of List


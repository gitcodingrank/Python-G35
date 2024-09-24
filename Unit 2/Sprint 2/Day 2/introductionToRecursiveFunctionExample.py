#Recursion: It is a technique using which you can divide complex problem into smaller sub-problems

#Recursion has two important parts:
#1. Recursive Function: It is just a function that calls itself during its execution.
#2. Base Condition: It is used to terminate/stop the function at some condition so that your function can not end up with infinite call.

"""
syntax:
def abc():
    if baseCondition:
        stop
    abc()

abc()
"""

#Example: find out the factorial of a number

# num = 5
# fact=1
# for i in range(1, num+1):
#     fact*=i
# print(fact)

#Using Recursion

# def findFactorial(num):
#     if num==1:
#         return 1
#     return num * findFactorial(num-1)

# print(findFactorial(5))


#Print Elements from a List Using Recursion

def printList(nameList, index):
    if index >= len(nameList):
        return
    print(nameList[index])
    printList(nameList, index+1)

names = ["Rahul", "Vaibhav", "Pavan", "Rizvi"]
printList(names, 0)

#Example: given a list of number of find print only even number using recursion.

numsList = [1,2,3,4,5,6,7,8,9,10]

# def printEvenNumberFromList(numbers, index):
#     if index >= len(numbers):
#         return
#     if numbers[index]%2==0:
#         print(numbers[index])
        
#     printEvenNumberFromList(numbers, index+1)

# printEvenNumberFromList(numsList,0)


"""
Task 5:
Define a function sum_of_natural_numbers(n) that returns the sum of the first n natural numbers.

Task 6:
Write a recursive function that takes a list and returns its reverse.

Task 7:
Count the Number of Digits in a Number

Task 8:
Sum of Digits of a Number

"""


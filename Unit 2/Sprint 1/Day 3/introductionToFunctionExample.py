#Function: it is block code which is related to specific functionality.

#Why Function?

#Logic for Prime Number
# num =5

# count = 0
# for i in range(1, num+1):
#     if num%2==0:
#         count+=1
# if count==2:
#     print("Its Prime")
# else:
#     print("Its Not Prime")

# print("Welcome to Python Function")

# num1 = 45
# num2 = 56

# print("Addition of Num1 and Num2: ", num1 + num2)

# number = 6
# count = 0
# for i in range(1, num+1):
#     if num%2==0:
#         count+=1
# if count==2:
#     print("Its Prime")
# else:
#     print("Its Not Prime")


# for i in range(1, 11):
#     print(i, end=" ")

# for table in range(1, 11):
#     print(2*table, end=" ")

# number1 = 7

# count = 0
# for i in range(1, num+1):
#     if num%2==0:
#         count+=1
# if count==2:
#     print("Its Prime")
# else:
    # print("Its Not Prime")

#Note: in above code, you're having to use prime number logic three 3 times what if you want to check for next 50 numbers then again you need to copy and paste the same code for next numbers, in this way you're making your code duplicate as well as lengthy which make your code harder to maintain.

#Solution: Function, using function you can promote reusability.


#Declaration of function in python:

"""
syntax:
def functionName():
    function body

"""

#Example 1: 

#Declaration of function
# def welcome():
#     print("Welcome to Chitkara University")

#Note: to use function, it is important to call it by its name
#Syntax: functionName()

#Calling the function
# welcome()
# welcome()
# welcome()
# welcome()


#Example 2:

# def playMusic():
#     print("Music started playing...")

# def pauseMusic():
#     print("Music has paused")

# def loopMusic():
#     print("Music has looped")

#Calling the above function

# playMusic()
# pauseMusic()
# playMusic()
# loopMusic()

# def add():
#     num1 = 45
#     num2 = 56
#     print(num1+num2)

# add()
# add()

#Once above functions are static function, therefore they can't be used dyanamically with different data.

#How to create dynamic function? - to create dynamic function, it is important to understand about function parameters and arguments.

#function parameter: at the time creating the function you also define parameter and these parameters are nothing but they are normal function variables.

#below function takes two parameters
def add(a,b):
    print(f"Sum of {a} and {b}: {a+b}")

#How to give value to above function parameters/variables: at the time of calling the function

num1 = 45
num2 = 5

#Here you are passing two arguments - num1 and num2
#Arguements: it is actual or original value you're passing to the function.
add(num1, num2)

add(12, 8) 

add(56, 70) 






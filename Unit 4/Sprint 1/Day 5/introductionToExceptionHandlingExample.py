#Exception Handling:- It is one of the critical part of every programming language that ensures your code to handle runtime errors gracefully without terminationg your application/program.

#Exception - An event that disrupts the normal flow of your program.


#Example:

# print("Welcome to India")
# print(4+5)
# #logic to check prime

# list = [1,2,3,4,4,5]
# element = list[8]

# print(f"list element at index 8 {element}")
#1000 lines of code

#Why Exception Handling:
#1. prevents from abrupt termination of program.
#2. you can provide meaningful msg if any errors occur.


#Syntax to handle expection:
#try - here you put the code that can have an error
#except: here you handle the error by providing some msg.
#else: if error is not there
#finally: it runs everytime with each try and except.

# name 

# print(name) #NameError

# file = open('any.txt', 'r')
# print(file) #FileNotFoundError

# value = int(input("Enter Number: "))
# print(value) #'a' - ValueError

# print(45/0) #ZeroDivisionError


"""
syntax:

try:
    #code that have error
except ErrorName:
    #handling the error

"""

#Example:
# try:
#     #code that have error
#     number = 45
#     # print(number/0)

#     print(number/2) #No Error

#     list = [1,2,3,4,5]
#     #print(list[6]) #IndexError
#     print(list[2])
# except ZeroDivisionError:
#     #handling the error
#     print("Number can't divide by zero")
# except IndexError:
#     print("Invalid Index, Please take the valid one")
# else:
#     print("When there is no error")
# finally:
#     print("it runs every time")


# print("Hello Everyone")


#Example 2:

# try:
#     a = int(input("Enter Number 1: "))
#     b = int(input("Enter Number 2: "))
#     addition = a + b
#     division = a/b
# except ValueError:
#     print("Take the valid number")
# except ZeroDivisionError:
#     print("Number can't divide by zero")
# else:
#     print(f"Addition Result is: {addition}")
#     print(f"Division Result is: {division}")

#Shorthand Way:

# try:
#     a = int(input("Enter Number 1: "))
#     b = int(input("Enter Number 2: "))
#     addition = a + b
#     division = a/b
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Error: {e}")
# else:
#     print(f"Addition Result is: {addition}")
#     print(f"Division Result is: {division}")


#Example: finally - it executes every time, here you can mention to close any important resourse

# print("Welcome to Applicaiton")
# file = None
# try:
#     file = open('data.txt', 'r')
#     print(file)
# except FileNotFoundError:
#     print("File doesn't exist. ")
# finally:
#     if file:
#         file.close()
#     print("File has closed, thank you for using.")


#How to raise exeption

# try:
#     age = int(input("Enter Age: "))
#     if age < 18:
#         raise ValueError('Age must be 18 or above')
#     else:
#         print("Registraction Successful")
# except ValueError as e:
#     print(f"Error: {e}")


#Problem: Create a program that can varify number if it is not valid kindly raise ValueError with meaningful msg.

#There are two types of error:
#1. Inbuilt Errors: TypeError, NameError, IndexError, FileNotFoundError, ZeroDivisioError and so on.
#2. Custom Error: We can also create our custom error.

#Example of customerError:

# class AgeIsTooSmall(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(message)


# try:
#     age = int(input("Enter Age: "))
#     if age < 18:
#         raise AgeIsTooSmall('Age must be 18 or above')
#     else:
#         print("Registraction Successful")
# except AgeIsTooSmall as e:
#     print(f"Error: {e}")


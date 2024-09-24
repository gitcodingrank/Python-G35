#passing arguments (Argument with Default Values, Keyword Argument, Arbitrary Arguments, Positional)

#Positional Arguments

# def printPersonalDetails(name, age, city):
#     print(f"Your Name is {name}")
#     print(f"Your Age is {age}")
#     print(f"Your City is {city}")

# #Positional Arguments
# printPersonalDetails("Rakesh", 45, "Noida")
# printPersonalDetails("Pawan", 44, "Delhi")
# printPersonalDetails(44, "Gurugram", "Deepak")


# #Default value for function parameters
# def printPersonalDetails(name="No Name Found", age=0, city="No City Found"):
#     print(f"Your Name is {name}")
#     print(f"Your Age is {age}")
#     print(f"Your City is {city}")

# printPersonalDetails()
# printPersonalDetails("Rakesh")
# printPersonalDetails("Rakesh",45)
# printPersonalDetails("Rakesh",45, "Gurugram")


# def printPersonalDetails(name, age, city):
#     print(f"Your Name is {name}")
#     print(f"Your Age is {age}")
#     print(f"Your City is {city}")


# printPersonalDetails("Rakesh",45, "Noida")
# print("------------------------------------")
# printPersonalDetails(45,"Rakesh", "Noida")

#keyword Arguments
# printPersonalDetails(name = "Rakesh", age = 45, city ="Noida")
# print("------------------------------------")
# printPersonalDetails(age = 45,name = "Rakesh", city= "Noida")

#Arbitrary Arguments: *variable_name - used for taking any number of argument in single variable and returns tuple

# def mySum(a,b,c,d):
#     return a+b+c+d

# print(mySum(23,45,12,5))
# print(mySum(23,45,12,5,56,45,34,23,34))

#sum(Iterable) - list/tuple

# def mySum(*numbers):
#     return sum(numbers)

# print(mySum(23,45,12,5))
# print(mySum(mySum(23,45,12,5,56,45,34,23,34)))

"""
Task 1:
Write a function introduce_person(name, age, city) that prints a sentence introducing a person.
Call the function using positional arguments and keyword arguments in different orders.

Task 2:

Write a function greet_person(name, greeting="Hello") that prints a greeting.
Call the function with:
Only the name argument.
Both name and greeting arguments.

Task 3:

Write a function sum_numbers(*args) that accepts any number of arguments and returns their sum.
Call the function with different numbers of arguments.

"""

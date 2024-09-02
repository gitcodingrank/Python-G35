#conditional statement: why are we gonna learb about this topic?
#Reason: so that on the basis of particular condition, we can give meaningful sttatement to the user.

#how to create condition: using comparison operator.


#check if student is having degree as MCA/BTECH

# degree = "mca"

# #create condition to check if age is greater or equal to 18
# age = 13
# condition1 = age >= 18

# print(condition1)

#check if student i

# condition2 = degree == "mca"
# print(condition2)

#there are following types of conditional statement:
#1. if statement
#2. if else statement
#3. if elif else statement

#more about conditional statement:
#nested if else statement.


#1. if statement: if the given condition is True then code inside if block will execute otherwise code inside if block will skip.

#Note: your python is indendation oriented programming language, in the case of some concept like conditional statement, loops, functions and others important concept you need to use proper indendation.
"""
syntax:

if condition :
    block of code

"""

#Example 1: check a number is negative or not.

# num = -10

# # condition = num < 0

# if num < 0:
#     print("Number is negative.")

#Example 2: check a number is odd or even

# num = 33

# if num % 2 == 0:
#     print("Starting of if Block")
#     print("Its Even Number") 
#     print("End of if Block")

#     print("Still inside if block")

# print("Out side the if block")


#Example 3: check if user is eligible for job if he is having degree as BTECH.

# degree = "BTECH"

# if degree == "BTECH":
#     print("You're eligible for first round of interview.")


#Conclusion: in the case of if statement, you're able to give meaningful statement when your given condition is true, in case of false condition its not showing any sign of msg.

#2. if else statement:  in the case of if else statement, if the given condition is true then code inside if block will execute otherwise code inside else block will execcute.

"""
syntax:

if condition :
    when condition is true
else:
    when conndition is false

"""

#Example: check a number is negative or positive

# num = -45

# if num > 0:
#     print("Number is positive.")
# else:
#     print("Number is negative.")

#Example: let user login if he is having below correct credential

# correctUsername = "admin"

# enteredUsername= input("Enter Username: ")

# #check condition for validation:

# if correctUsername == enteredUsername:
#     print("Logged in successfully.")
# else:
#     print("Invalid username.")


#Question 1: check a number is negative, positive, or zero

# Limitation of if else statement: if else statement is the best choice if you've only one independent condition or depenedent conditions. 

#independent conditions:  when one condition is not dependent on another condition:
#check day name of the week according to day number where first day starts with 1 as Monday.
#check a number is negative, positive, or zero


#depended conditions: one condition is dependent on another condition
#check if username and password is correct.
#print welcome to job: if you've followings things: degree: mca,  percentage >= 80, dsa: true


#check a number is negative, positive, or zero

# num = 0

# if num == 0:
#     print("Zero")
# else:
#     if num < 0:
#         print("Negative")
#     else:
#         print("Positive")

#print day of the week according to the day number where it starts with 1 as Monday.

# dayNumber = 10

# if dayNumber == 1:
#     print("Monday")
# else:
#     if dayNumber ==2:
#         print("Tuesday")
#     else:
#         if dayNumber ==3:
#             print("Wednesday")
#         else:
#             if dayNumber == 4:
#                 print("Thursday")
#             else:
#                 if dayNumber == 5:
#                     print("Friday")
#                 else:
#                     if dayNumber == 6:
#                         print("Saturday")
#                     else: 
#                         if dayNumber ==7:
#                             print("Sunday")
#                         else:
#                             print("Invalid day number.")

#Due to above limitation with if else statement we're learning about if elif else statement.

#3. if elif else statement: it is the best choice if you're more than one independent condition.
#if any of the condition is true then code inside that particular block will execute otherwise code inside else block will execute.


"""
syntax:

if condition1 :
    when condition1 is true
elif condition2:
    when connditio2 is false
elif condition3:
    when connditio2 is false
elif condition4:
    when connditio2 is false
elif condition5:
    when connditio2 is false
else:
    if any of above conditions are true.

"""

#Example: print day of the week according to the day number where it starts with 1 as Monday.

# dayNumber = 9

# if dayNumber == 1:
#     print("Monday")
# elif dayNumber ==2:
#     print("Tuesday")
# elif dayNumber ==3:
#     print("Wednesday")
# elif dayNumber ==4:
#     print("Thursday")
# elif dayNumber ==5:
#     print("Friday")
# elif dayNumber ==6:
#     print("Saturday")
# elif dayNumber ==7:
#     print("Sunday")
# else:
#     print("Invalid Day Number.")

#Example 2: given a letter in smallcap kindly print, it is vowel or consonant.
# letter = 'a'

# if letter == 'a':
#     print("Vowel")
# elif letter == 'e':
#     print("Vowel")
# elif letter == 'i':
#     print("Vowel")
# elif letter == 'o':
#     print("Vowel")
# elif letter == 'u':
#     print("Vowel")
# else:
#     print("Invalid Vowel.")

#Nested if else statement: once you've depenedent conditions, meaning that when one condition is related another condition.
#if inside another if


"""
syntax:

if condition1:
    if condition2:
    
    else:
else:    
"""

#Example 1: check a username and password is okay or not

# username = "student"
# password = "12345"

# if username == "admin":
#     if password =="12345":
#         print("Logged in successfully.")
#     else:
#         print("Invalid password")
# else:
#     print("Invalid username")


#Example 2:  eligible for job by following cretia
#degree: MCA + Percentage >= 80, DSA : TRUE
#degree: BTECH + Percentage >= 90

degree = "mca"
percentage = 80
isDSA = False

if degree == "mca":
    print("Degree has varified successfully.")
    if percentage >= 90:
        print("Percentage Varification has done")
        print("Welcome to Google")
    else:
        print("You've not  met the percentage criteria")
elif degree =="BTECH":
    print("Degree has varified successfully.")
    if percentage >= 80:
        print("Percentage Varification has done")
        if isDSA:
            print("DSA has varified successfully.")
            print("Welcome to Google.")
    else:
        print("You've not  met the DSA criteria")
else:
    print("Sorry you've not met the Degree Criteria")
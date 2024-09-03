#Problem 1: print the meaningful statement to the user according to following criteria
#Do Marriage: gender: male, age >= 21
#Do Marriage: gender: female, age >= 18
#Note: Handle proper invalid inputs.

# gender = input("Enter Gender: ")
# age = int(input("Enter Age: "))

# #conditions

# if gender =="male":
#     print("Male Gender has varified successfully.")
#     if age >= 21:
#         print("Male: Do Marriage")
#     else:
#         print("Male: You're not meeting the age criteria")
# elif gender =="female":
#     print("Female Gender has varified successfully.")
#     if age >= 18:
#         print("Female: Do Marriage")
#     else:
#         print("Female: You're not meeting the age criteria")
# else:
    # print("Invalid Gender.")

#Problem with Nested if else statement: your code looks less readable and harder to maintain.
#What is the solution: Logical Operator:


#Logiacal Opertor: if you've more condition dependent conditions then logical operator is the best choice.

#There are following types of logical operators:
#1. and 
#2. or 
#3. not

#1. and operator: in this case amongs many conditions if all the conditions are true then entire expression will be true if any of the condition is false then entire exrpession will be false.

"""
syntax:
condition1 and condition2 and condition3

A       B         A and B
TRUE  TRUE          TRUE
TRUE  FALSE         FALSE
FALSE TRUE          FALSE
FALSE FALSE         FALSE

Note: and operator always looks for next True value, if anywhere it finds False then it make entire expression as False.
"""

#Example 1: check username and password and print the proper msg to the user.


#Without using Logical and Operator:
# username = "admin"
# password = "12345"

# if username =="admin":
#     if password =="12345":
#         print("Logged in Successfully.")
#     else:
#         print("Invalid Password")
# else:
#     print("Invalid username")

#using logical and operator

# username = "admin"
# password = "1234"

# if username == "admin" and password =="12345":
#     print("Logged in Successfully.")
# else:
#     print("Invalid Credentials")


#Logical or operator: in this case amongs many conditions, if any of the codition is true then entire expression will be true and if none of the given codition is true then entire expression will false.

"""
syntax:
condition1 or condition2 or condition3

A       B         A or B
TRUE  TRUE          TRUE
TRUE  FALSE         TRUE
FALSE TRUE          TRUE
FALSE FALSE         FALSE

Note: or operator always looks first True value, if it doesn't find any True then it make entire expression as False.
"""

#Example: check a letter/character is vowel or consonant:

# letter = 't'

# if (letter == 'a') or (letter == 'e') or (letter == 'i') or (letter == 'o') or (letter == 'u'): 
#     print("Vowel")
# else:
#     print("Consonant")


#not operator: it negates the condition value, if the given condition is True then it will make it False and vice versa.

# isFriday = False

# if not isFriday:
#     print("Party")
# else:
#     print("No Party")
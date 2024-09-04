#Ternary Operator: it is used as conditional expression which is shorthand/concise way of if else statement.
#On python 2.5 version onward people started using this.

"""
synatx:
[Statement if true] if condition else [Statement if false]
"""

#Example 1: check a number is odd and even

# num = int(input("Enter Number: "))

#Without Ternary Operator:

# if num%2==0:
#     print("Even")
# else:
#     print("Odd")

#Using Ternary Operator:
# print("Even") if num%2==0 else print("Odd")

#Note: Ternary opeartor can also return the statement.
# num = int(input("Enter Number: "))
# print("Even" if num%2==0 else "Odd")

#Do Particular solution with the help ternary operator:

membership = input("Enter Membership(non-member/member): ")
amount = int(input("Enter Amount: "))

# if (membership == "member" and amount >100) or (membership =="non-member" and amount>200):
#     print("Eligible for Discount")
# else:
#     print("Not Eligible for Discount")

#Using Ternary Operator:

# print("Eligible for Discount") if (membership == "member" and amount > 100) or (membership =="non-member" and amount > 200) else print("Not Eligible for Discount")

# result = "Eligible for Discount" if (membership == "member" and amount > 100) or (membership =="non-member" and amount > 200) else "Not Eligible for Discount"

#print(result)

# print("Eligible for Discount" if (membership == "member" and amount > 100) or (membership =="non-member" and amount > 200) else "Not Eligible for Discount")


#Example: check a letter is vowel or consonant using ternary opertor.


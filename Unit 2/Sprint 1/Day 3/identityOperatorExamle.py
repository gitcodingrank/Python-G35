# #Identity Operator: it checks particular variable data belongs to particular reference/address in the memory.

# """
# name = "Rakesh"
# age = 45
# isMarried = True
# address1 = "Noida"
# address2 = "Noida"

# Note: Whenever you run your above code, then it occupies some space in the RAM that occupied space is known as address space/segment in the RAM.

# this address segment again has two important parts

#     Stack                      Heap
#   |2323232323232|-------->| "Rakesh"  |
#        name
#   |3423232323232|-------->   | 45  |
#        age
#   |34232323245343|-------->  | True  |
#        isMarried

#   |34232323232322|-------->  | "Noida"  |
#        address1  |
#                  |  
#        address2--

# """

# #There are following identity operator:
# #1. is - checks if two variable's references are same or not
# #2. is not - checks if two variable's references are not same

# #Example 1:

# # num1 = 45
# # num2 = 45

# #Comparision for equality:
# #1. == -always compare the value
# #2. is -always compare the references/addresses

# # print(num1 == num2) #True
# # print(num1 is num2) #True

# # print("num1 reference: ", id(num1)) 
# # print("num2 reference: ",id(num2)) 


# #Example 2:

# # num1 = 45
# # num2 = 56

# # print(num1 == num2) #False
# # print(num1 is not num2) #False

# # print("num1 reference: ", id(num1)) 
# # print("num2 reference: ",id(num2))


# #Example 3:

# num1 = 257
# num2 = int(input("Enter Number: ")) #257

# print(num1 == num2) #True
# print(num1 is num2) #True

# #Note: in python there is certain range for integer number if there are between -5 to 256 then they will belong to same address


# #Example 4:

# # num1 = 45.50
# # num2 = 45.50
# # num2 = float(input("Enter Number: ")) #45.50

# # print(num1 == num2) #True
# # print(num1 is num2) #False

# # print("num1 reference: ", id(num1)) 
# # print("num2 reference: ",id(num2)) 
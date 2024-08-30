#Comparison Operators: 
# It is used to perform comaprison between data values or it is used to create conditions
#It always returns boolean(either true or false) value as a result.
#True: when comparison is matching/meeting with criteria
#False: when comparison is not matching/meeting with criteria

#There are following types of Comparison Operators:
#1. > (greater than)
#2. < (less than)
#3. <=(less than or equal to )
#4. >=(greater than or equal to)
#5. == (equal to )
#6. != (not equal to )


#Example 1: check two numbers which are small and big

# num1 = 50
# num2 = 50

# result = num1 > num2
#True: When num1 is big
#False: When Num2 is big 

#print(result)
# print(num1 > num2)

#Note: in the case of greater than operator, it will only return true when one value is greater than another value

# print(num1 >= num2)

#Note: in the case of greater than or equal to operator, it will return true in two case if the first value is either greater than or equal to.

# print(45<56)

#Note: in the case of less than operator, it will only return true when one value is less than another value

# print(45<=45)

#Note: in the case of less than or equal to operator, it will return true in two case if the first value is either less than or equal to.

#Note: mainly we use these comparison operators(>,>=,<,<=) for comaparing numberic value.

# print(True>0)
# print(True>1)
# print(True>=1)


#Note: You can use these operator(==, !=) for comparing any type of data.

#==(equal to): it checks eqaulity


# print("rakesh"=="rakesh") #True
# print("rakesh"=="Rakesh") #False
# print("5"==5)
# print("5"!=5)


#Good Example 1: check if day is friday we will do party else will do study.

# isFriday = True
# print(isFriday==True) #True
# print(isFriday=="True") #False
# print(isFriday==False) #False
# #True: Party
# #False: Study

#Good Example: check a number is negative or positive

# num = -45
# print(num > 0)
# #True: Number is positive
# #False: Number is negative

#Good Example 3: check a number is even or odd
num = 20
# evenCondition = num % 2 == 0
#print(evenCondition)
print( num % 2 == 0)
#True: Num is even
#False: Num is odd

#Good Example 4: check a person is eligible for shopping according following criteria
#Eligible if you totalBill is less than or equal to 10000
#TotalBill = 9000 then let me know eligibility: ?
totalBill1 = 9000
print(totalBill1<=10000) #True
#True: Eligible for shopping
#False: Not Eligible for shopping

#TotalBill = 11000 then let me know eligibility: ?

totalBill2 =11000
print(totalBill2<=10000) #False
#True: Eligible for shopping
#False: Not Eligible for shopping


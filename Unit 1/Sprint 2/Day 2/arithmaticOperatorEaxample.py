#Arithmatic/Mathematical Operator: it is used to perform some mathematical calculation in python program.
#Operator: Sign(+, -, *, /, %, //)

#Note: Operator(+, -, *, /,%, //) operates with operands(data variables).
#In other way, particular operator perform particular operation with data variables.

#Example 1:

a = 20
b = 10

#Addition
#Operator: +(addition)
#Operands: a and b

add = a + b #here + operator performing addition with a and b and it will return resultant value.

#print(add) #30
print(a+b) #30


#subtraction

sub = a-b
print(sub) #10
print(f"subtraction is {sub}") #


#Division:

div = a / b
print(div) #2

#Floor Division
div1 = a//b
print(div1)

#Mutliplication

mul = a * b
print(mul) #200


#Good Example 1:


#Problem Statement: an offer is going on flipkart if you will buy any three product with atleast 3 quantity then you will get 30% discount, now find out what is the finalPayable price after discount according to following data.

product1Price = 500
product2Price = 200
product3Price = 1000

product1Quantity = 4
product2Quantity = 5
produc3Quantity = 3 

totalPrice = product1Price * product1Quantity + product2Price * product2Quantity + product3Price * produc3Quantity

print("Total Price is",totalPrice)

discount = totalPrice * 30 /100

print("30% Discount", discount)

finalPrice = totalPrice - discount

print("Total Payable Amount", finalPrice)


#Example 2: Mathematical Expression.

a = 4 
b = 5
c = 6
d = 7

result = a*b + b*c + b+d - c

# print(result)

#Example: Find out any power of any number.

num = 5
print(num*num)
print(num*num*num) #num^3

#exponentiation operator: **
#Syntax: variable_name**power

print(5**2) #25

print(5**3) #125
print(5**10) #9765625


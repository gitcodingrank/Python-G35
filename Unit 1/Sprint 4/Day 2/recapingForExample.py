#For Loop: there are following reasons:
#1. in the case while loop, we're having write below three part of the loop at different place which increases the length of the code.
#a. staratingPoint, b. where to stop(condition), c. step
#Note: but using for loop, you have good facility to write these three parts of the loop at one place which decreses the lines of code.
#2. In most of cases, due to bad use of above three important part it can go for inifinite loop.
#Note: in the case of for loop, this situation is not gonna come.


#Note: in simple term, we can say for loop is better to execute lines of code again and again in concise way.

"""
syntax:

for variable_name in sequence:
    #block of code.

Note: to decide the sequence as of now, you can use range function which works for following things:

range(n) #n is a number
default behavior
Case 1:
range(5) #sp = 0, where to stop: 4(sp<5), step: 1
Case 2:
range(1, 5)# sp= 1, where to stop: 4(sp<5), step: 1
Case 3:
range(1, 5, 2)# sp= 1, where to stop: 4(sp<5), step: 2

for variable_name in range(n):
    #block of code.

"""

#Example 1: print number between 1 to 10

# for sp in range(1,11):
#     print(sp)

#Process of for loop execution: sp---->check condition(true)---->execute block of code---->step increment/decrement--->check condition(true)----->execute block of code --->step increment/decrement--->check condition(true)---->block of code----->step increment/decrement---->check condition(false)----->come out of the loop.

#Example 2: print even number from 1 to 10

# for sp in range(1,11):
#     if sp%2==0:
#         print(sp)


#Example 2: print even number from 1 to 20 but go 2 step at a time.

# for sp in range(1,21,2):
#     if sp%2==0:
#         print(sp)

#Output: Nothing



#Example 2: print even number from 1 to 20 but go 3 step at a time.

# for sp in range(1,21,3):
#     if sp%2==0:
#         print(sp)

#Problem Statement: Write a Python program that prints all prime numbers between 1 and 50

#Logic to run loop from 1 50

for sp in range(1, 51):

    #Logic to check each number for prime
    count = 0
    for i in range(1, sp+1):
        if sp%i==0:
            count+=1
    if count==2:
        print(sp)
    

#Logic to check a number is prime or not.


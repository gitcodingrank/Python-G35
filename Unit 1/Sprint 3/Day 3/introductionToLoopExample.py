#why loop:
# if i ask you to print "Hello Everyone" 10 times.

# print("Hello Everyone") 
# print("Hello Everyone") 
# print("Hello Everyone") 
# print("Hello Everyone") 
# print("Hello Everyone") 
# print("Hello Everyone") 
# print("Hello Everyone") 
# print("Hello Everyone") 
# print("Hello Everyone") 

#What if i ask you to do same task 1000 times?
#in this way, you will be ended with duplicate/redundant code and which will make your code less readable and harder to maintain.

#Solution is loop: it is iterative statement which is used to execute block of code until the given condition is true.


#There are following types of loop:
#1. while loop
#2. for loop

#1. while loop: it is iterative statement which is used to execute block of code until the given condition is true.

"""
syntax: 
while condition:
    print("if condition is true")

"""

#Example 1: 

#Infinite loop:
# while True:
#     print("Hello Everyone")

#Note: loop do following continuously.
#Step 1: it checks the condition for executing block of code
#Step 2: it executes the block of code if condition is true
#Step 3: it again checks the condition and so on.

#Note: above process keeps on happening until the given condition is true.


#How to loop for particular times?, if you want to run loop for particular time you need to define three important part of loop:

#1. starting point
#2. condition: where to stop
#3. how many step you want to go in each round/iteration.

"""

^
1   2  3  4  5  6  7  8  9  10
"""

#Exmaple: print number from 1 to 10

# sp = 1

# while sp <= 10:
#     print(sp)
#     sp = sp + 1 #updating the sp value

#Above while loop will run for 10 times you can also say 10 rounds/10 iterations.

#Exmaple 2: print "Hello World" 10 times

# sp = 1

# while sp <= 10:
#     print("Hello World")
#     sp = sp + 1

#Examples: print number from 20 to 1

# sp = 20

# while sp >= 1:
#     print(sp)
#     sp = sp - 1


#Example 2: print only even from from 1 to 20

# sp = 1

# while sp <= 20:
#     #check condition to print only even number
#     if sp%2==0:
#         print(sp)
#     sp = sp + 1

#Example 2: print even and odd from from 1 to 20
# sp = 1

# while sp <= 20:
#     #check condition to print only even number
#     if sp%2==0:
#         print("Even Number", sp)
#     else:
#         print("Odd Number", sp)
#     sp = sp + 1


#Good Problem: print multiple of 3 form 1 to 20

# sp = 1

# while sp <= 20:
#     #check condition to print only multiple of 3
#     if sp%3==0:
#         print(sp)
#     sp = sp + 1


#Write a program to find out the table of 2
"""
2*1
2*2
2*3
2*4
2*5
2*6
2*7
2*8
2*9
2*10

"""

# sp=1

# while sp<=10:
#     print(2*sp)
#     sp = sp + 1


#Write a program to print table of any number:


#Write a program to find factorial of a number.
#n!
#5! - 5*4*3*2*1
#6! - 6*5*4*3*2*1

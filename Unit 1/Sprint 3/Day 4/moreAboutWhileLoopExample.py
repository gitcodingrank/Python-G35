#Example 1: print even number from 1 to 50
#Solution

# i = 1

# while i <=50:
#   if i%2==0:
#     print(i)
#   i+=1

#Example 2: find out the factorial of any number.
#5! = 5*4*3*2*1
#7! = 7*6*5*4*3*2*1

# sp = int(input("Enter Number to Find Factorial: "))
# fact = 1

#logic to find the factorial of any number
# while sp >= 1:
#   fact*= sp
#   sp-=1

# print(f"Factorial of {sp}: is {fact}")

"""
Visualization(Dry Run):
sp = 5
Round 1: 5 >= 1 True
            bag = 1*5 => 5
            sp = 5 - 1 =>4
Round 2: 4 >= 1 True
            bag = 5*4 => 20
            sp = 4 - 1 => 3
Round 3: 3 >= 1 True
            bag = 20*3 => 60
            sp = 3-1 => 2
Round 4: 2 >= 1 True
            bag = 60*2 => 120
            sp = 2-1 => 1
Round 5: 1 >= 1 True
             bag =  120 * 1 = 120
             sp = 1 - 1 => 0
Round 6: 0 >= 1 False (Come out of the loop)
"""

#Example 3: find out the total number of even number between 1 to 5

# sp = 1
# evenCounter = 0

# while sp <= 5:

#   #checking the even number and increasing the value of evenCounter if you find any number as even.
#   if sp%2==0:
#     evenCounter+=1
    
#   sp+=1

# print("Total Even Number: ", evenCounter)

"""
sp = 1
eventCounter = 0

Round 1: sp <= 5: True
           sp%2==0 False : Not Even Number
           sp = 1 + 1 => 2
Round 2: sp <= 5: True
           sp%2==0 True: Even Number
           eventCounter = 0 + 1 => 1
           sp = 2 + 1 => 3
Round 3: sp <= 5: True
             sp%2==0 False: Not Even Number
             sp = 3 + 1 => 4
Round 4: sp <= 5: True
            sp%2==0: True: Even Number
            evenCounter = 1 + 1 => 2
            sp = 4 + 1 => 5
Round 5: sp <= 5: True
            sp%2==0: False: Not Even Number
            sp = 5 + 1 => 6
Round 6: sp <= 5: False(Come out of the loop)

Output: Total Even Number: 2
"""

#Example 4: find out the sum of first 10 natural number
# 1 to 10

# sp = 1
# sum = 0

# while sp <= 10:
#   sum+=sp
#   sp+=1

# print(sum)


#Example 4: find out the sum of n natural number.

# sp = 1
# n = int(input("Enter Value of n: "))
# sum = 0

# while sp <= n:
#   sum+=sp
#   sp+=1

# print(sum)


#Example 5: check a number is prime or not.

num = int(input("Enter Number to Check Prime: "))
sp = 1
count = 0

while sp<=num:
  
  if(num%sp==0):
    count+=1
    
  sp+=1

#check number is prime or not on the basis of count value, if count value is exactly equal to 2 then we can say its prime

if count==2:
  print(f"{num} is prime number")
else:
  print(f"{num} is not prime number")
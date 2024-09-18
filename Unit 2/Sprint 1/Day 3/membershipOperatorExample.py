#Membership Operator: It is used to check in sequence if any element is the part of that sequence or not.
#If it is present then it retuns Boolean value as True if not as False

#There are following types of membership operator:
#1. in: it checks particular data is the part of sequence or not.
#2. not in: it checks if particular data must not be part of sequence.

"""
syntax:
data in/not in seqeunce(list, string, tuple)
"""

#Example 1:
nums = [1,2,3,4,5,6,7,8,9,10]
print(5 in nums) #True
print(11 in nums) #False


print(5 not in nums) #False
print(11 not in nums) #False

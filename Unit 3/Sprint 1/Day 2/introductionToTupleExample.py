#tuple - it is a data structure which is used to store collections of element but there is one difference between list and tuple, once you've created a tuple you can not do modification, updation, and addition of another element as tuple is immutable.

#other words - tuple is collection of ordered and immutable elements.

#Tuple characteristics:
#1. immutable
#2. ordered
#3. allow duplicate value
#4. support indexing.


#declaration of tuple


# nums = () #declared tuple with name nums
# print(nums)
# print(type(nums)) # <class 'tuple'>s
# print(len(nums))

# numsList = [1,2,3,4,5,6,7]
# print(f"before converting - {numsList}")

# nums = tuple(numsList)

# print(f"after converting - {nums}")

#Example: given numebrs tuple

# nums = (1,)
# print(nums)
# print(len(nums))

#Note: like list, it also follows 0 based indexing.

# nums = (1,2,3,4,5,6,7,8,9,10)

#accessing the element
# print(nums[1])

# #updating the element
# nums[1] = 10 #TypeError - tuple object doesn't support item assignment.
# print(nums)

#loop in tuple

#1st way:

# for item in nums:
#     print(item, end=" ")

# print()

# #2nd way:
# for i in range(len(nums)):
#     print(nums[i], end=" ")


#tuple slicing:
# nums = (1,2,3,4,5,6,3,4,5,2,4,2,3,42,7,8,9,10)

# print(nums[1:])
# print(nums[::-1])

#python inbuilt function for tuple:

# print(max(nums))
# print(min(nums))
# print(sum(nums))
# print(len(nums))



#tuple inbuilt function:

# print(nums.count(2))
# print(nums.index(2))

#packing and unpacking - list and tuple:

#list
# nums = [1,2,3,4,5,6]

# a, b, *c= nums
# print(a,b,c)

#tuple
# nums = (1,2,3,4,5,6)

# a, b, *c= nums
# print(a,b,c)


#Example: given number tuple, your task is to find out the the sum of all elements starting from index 2

# nums = (1,2,3,4,5,6,7,8,9,10)

# a, b, *c = nums
# print(sum(c))


#sorting:

# nums = (1,6,7,4,8,6)

# print(sorted(nums, key=None, reverse=True))

# numsTuple = [(1, "Delhi"), (2, "Punjab"), (3, "Indore"), (4, "Bangalore")]

# print(sorted(numsTuple, key=lambda x:x[1],reverse=True))


# str = "hello"

# print(sorted(str, reverse=True))











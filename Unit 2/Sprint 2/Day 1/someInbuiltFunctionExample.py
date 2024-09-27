#Inbuilt Functions for Iterable(List, Tuple)
#min(Iterable)

# numbers = [1,2,3,56,34,23,12,67,54]

# print(min(numbers))
# print(max(numbers))

#Assignment: find out the minimum and maximum value of the numbers list.

#sum

# numbers = [1,2,3,56,34,23,12,67,54]
# print(sum(numbers))

# def mySum(nums):
#     sum = 0
#     for i in nums:
#         sum+=i
#     return sum

# print(mySum(numbers))

# #or
# result = mySum(numbers)
# print(result)

#reverse()

# cities = ["Noida", "Delhi", "Harayana", "Gurugram"]

# def listReverse(list):
#     newList = []
#     for i in range(len(list)-1, -1,-1):
#         newList.append(list[i])
#     return newList

# result = listReverse(cities)
# print(result)

# print(listReverse(cities))
# nums = [1,2,2,1]

# result = abs(45.45)
# print(abs(-45))
# print(abs(-45.45))

# print(round(45.5644343, 3))

#any, all, etcs.

"""
Function vs Method
-Both are block of code which is related to specific functionality.
-In case of Functions, you can use them independenlty.
-In case of Methods, you can use them dependently

-Functions are not dependent on any object whereas Methods are depended on some object.
"""
#List Methods:
#append(), insert(), pop(),remove(element)  reverse(), copy(), sort(), count(), index()

nums = [1,2,3,4,5,6,7,8,9,10]
#syntax: list.methods()

# nums.append(45)
# print(nums) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 45]

# nums.remove(45)
# print(nums) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# nums.pop()#it removes from the end of the list.
# print(nums) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

# #nums.pop(index)it removes element from sepecific index in the list.
# nums.pop(1)
# print(nums) #[1, 3, 4, 5, 6, 7, 8, 9]

#Notes: pop() methods returns deleted/removed element as well.

# fruits = ["Papaya", "Apple", "Banana", "Orange"]
# print("Removed Element from Fruits List: ",fruits.pop()) #Orange
# print(fruits)
# fruits.reverse()
# print(fruits)

# newList = fruits.copy()

# print(newList)


# fruits = ["Papaya", "Apple","Orange", "Banana", "Orange"]

# # print(fruits.count("Orange1"))
# print(fruits.index("Papaya"))
# print(fruits.index("Apple1"))


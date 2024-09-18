#List Slicing: If you want to extract some portion of list.
#Syntax: list_name[START:END:STEP] - it returns new sliced list.

numbers = [1,2,3,4,5,6,7,8,9,10]

#Example 1: numbers[:] - default behavior: sp=0, end=len(numbers), step: 1

# newList = numbers[:] 
# print(newList)

# newList = numbers[1:] 
# print(newList)

# newList = numbers[1:4] 
# print(newList)

# newList = numbers[1:4:2] 
# print(newList)

# newList = numbers[:-1] 
# print(newList)

# newList = numbers[-1:-2:-1] 
# print(newList)

#List Comprehension: It is the concise way to create list and do operations on list.
#Syntax: [expression loop condition]

#Example 1: 

#Without using LC:

# numsList = []
# for num in range(1, 11):
#     numsList.append(num)
# print(numsList)

# #With using LC:
# numsList = [num for num in range(1,11)]
# print(numsList)

#Good Example 2:

# evnList = [num for num in range(1, 11) if num%2==0]
# print(evnList)

#Good Example 3:
# boolList =  [True, False, False, True, False]

# newList = [boolValue for boolValue in boolList if boolValue==False ]
# print(newList)

#Good Example 4: Given Number List, find out square of each number using LC

# numbers = [1,2,3,4,5]

# print([n**2 for n in numbers])

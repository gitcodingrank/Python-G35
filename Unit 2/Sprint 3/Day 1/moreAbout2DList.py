# """
# Given 2D list of numbers, where at index 0 list is [1,2,3,4,5], index 1 list is [6,7,8,9,10] and index 2 list is [11,12,13,14,15]

# Now perform following operation:
# 1. find out the numbers of Rows
# 2. find out the numbers of Columns
# 3. print the numbers row wise
# """

# #Solution

# #Consistent/same size Column
# nums = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15]
# ]

# rows = len(nums)
# print(rows)

# columns = len(nums[0])
# print(columns)

# #outer loop: rows
# for row in range(rows):
#     #inner loop: columns
#     for column in range(columns):
#         print(nums[row][column], end=" ")
#     print()

# """
# Given 2D list of numbers, where at index 0 list is [1,2,3,4,5], index 1 list is [6,7,8] and index 2 list is [11,12,13,14]

# Now perform following operation:
# 1. find out the numbers of Rows
# 2. find out the numbers of Columns
# 3. print the numbers row wise

# """

# #Solution

# #Non Consistent/Different size Column
# nums = [
#     [1,2,3,4,5],
#     [6,7,8],
#     [11,12,13,14]
# ]

# #Note: in the case of above example where column sizes are different, then for finding the columns you need to check for every rows seperatly.
# rows = len(nums)
# print(rows)

# row1Columns = len(nums[0])
# row2Columns = len(nums[1])
# row3Columns = len(nums[2])
# print(row1Columns)
# print(row2Columns)
# print(row3Columns)

# #outer loop: rows
# for row in range(rows):
#     #inner loop: columns
#     for column in range(len(nums[row])):
#         print(nums[row][column], end=" ")
#     print()


#Example 1:

nums = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]

#Problem 1: print the sum of each row in above example.

# #Without reduce
# for row in range(len(nums)):
#     sum = 0
#     for column in range(len(nums[0])):
#         sum+=nums[row][column]
#     print(f"Row {row+1} sum is {sum}")

# print("----------------------------------------------")

#Using reduce=
# from functools import reduce
# for row in range(len(nums)):
#     sum = reduce(lambda a,b:a+b, nums[row])
#     print(f"Row {row+1} sum is {sum}")


nums = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]
#Column1 - 1(nums[0][0]) + 6(nums[1][0]) + 11(nums[2][0])
#Column2 - 2(nums[0][1]) + 7(nums[1][1]) + 12(nums[2][1])
#Column3 - 3(nums[0][2]) + 8(nums[1][2]) + 13(nums[2][2])
#Column4 - 4(nums[0][3]) + 9(nums[1][3]) + 14(nums[2][3])
#Column5 - 5(nums[0][4]) + 10(nums[1][4]) + 15(nums[2][4])

column1Sum = 0
for row in range(len(nums)):
    column1Sum+=nums[row][0]

print(column1Sum)


column2Sum = 0
for row in range(len(nums)):
    column2Sum+=nums[row][1]

print(column2Sum)

#Problem 2: print the sum of each column in above example.



#Example 2:

nums = [
    [1,2,3,4,5],
    [6,7],
    [11,13,14,15],
    [45,23,12]
]

#Problem 1: print the sum of each row in above example.
#Problem 2: print the sum of each column in above example.





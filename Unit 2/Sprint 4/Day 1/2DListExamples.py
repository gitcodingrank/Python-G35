#below is the example of jagged list.

# nums = [
#     [1,2,3],
#     [4,5],
#     [6,7,8,9]
# ]



#Matrix Operations:

#Addition

# matrix1 = [
#     [1,2],
#     [3,4]
# ]

# matrix2 = [
#     [5,6],
#     [7,8]
# ]

# addMatrix = [
#     [0,0],
#     [0,0]
# ]

# for i in range(len(matrix1)):
#     for j in range(len(matrix1)):
#        addMatrix[i][j] = matrix1[i][j]+ matrix2[i][j]  

# print(addMatrix)


# #Subtraction

# matrix1 = [
#     [1,2],
#     [3,4]
# ]

# matrix2 = [
#     [5,6],
#     [7,8]
# ]

# subMatrix = [
#     [0,0],
#     [0,0]
# ]

# for i in range(len(matrix1)):
#     for j in range(len(matrix1)):
#        addMatrix[i][j] = matrix1[i][j] - matrix2[i][j]  

# print(subMatrix)


# #Multiplication

# matrix1 = [
#     [1,2],
#     [3,4]
# ]

# matrix2 = [
#     [5,6],
#     [7,8]
# ]

# mulMatrix = [
#     [0,0],
#     [0,0]
# ]

# for i in range(len(matrix1)):
#     for j in range(len(matrix2)):
#         for row in range(len(matrix1)):
#             mulMatrix[i][j] += matrix1[i][row] * matrix2[row][j]


# """
# Visualization/Dry Run:
# given i = 0, j = 0, row = 0
# matrix1Length = 2
# matrix2Length = 2 
# Round 1 - i < 2 True
#             j < 2 True
#                 row < 2 True
#                     mulMatrix[i][j] += matrix1[0][0] * matrix2[0][0] 
#                     row+=1 ---> row =1
#                     row < 2 True
#                      mulMatrix[i][j] += matrix1[0][1] * matrix2[1][0]
#                         row+=1 ---> row =2
#                         row < 2 False
#             j+= 1 ---> j=1

# Continued
# """


# #Example 2: Find out the diagonal sum of square matrix

# matrix = [
#     [5,6],
#     [7,8]
# ]

# """
# Sum1 = 5(matrix[0][0]) + 8(matrix[1][1])
# Sum2 = 6(matrix[0][1]) + 8(matrix[1][0])
# """

matrix = [
    [5,6,5,4,2],
    [7,8,5,6,3],
    [10,11,12,13,3],
]

"""
Visualization:- 
                5([0][0]) --6([0][1]) --5([0][2])--4([0][3])--2([0][4])--
                3([1][4]) --6([1][3]) --5([1][2])--8([1][1])--5([1][0])--
                10([2][0]) --11([2][1]) --12([2][2])--13([2][3])--3([2][4])
"""

for i in range(len(matrix)):
    if i%2==0:
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
    else:
        for k in range(len(matrix[0])-1,-1,-1):
            print(matrix[i][k], end=" ")
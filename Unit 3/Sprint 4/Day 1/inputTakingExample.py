#Problem 1:  10 test cases - 8 test cases - hidden

"""
test case 1
input:

row = 3
column = 3
list = [[1,2,3], [1,2,3], [4,5,6]]

output:


test case 2:

input:
row = 4
column = 3
list = [[1,2,3], [1,2,3], [4,5,6]]

"""


"""

input 
5 4 --- 
1 2 3 4
6 7 8 9
1 2 3 4
6 7 5 2
2 3 4 1

first - rows = int(input().split()[0])
second - list = []
for row in range(rows):
    list.append([int(num) for num in input().split()])
"""

rowIndex = 0
list = []
while True:
    row = input(f"Enter Element for Row {rowIndex}: ")
    list.append([int(num) for num in row.split()])
    res = input("Do you want to add more Rows(y/n): ")
    rowIndex+=1
    if res in ['n', 'N']:
        print("Your List is: ")
        print(list)
        break



#Bubble Sort Algorithm: it is simple algorithm to arrange the element in Asscending or descending order.
#It works by repeatedly swapping adjacent elements, if they are in wrong order.
#Asscending Order: smaller element will bubble up to its correct position in each pass
#Descending Order: bigger element will bubble up to its correct position in each pass


#How does it work?

#1. Intial Setup: Start with the entire list as unsorted.
#2. Compare with Adjacent Element: You will compare with adjacent element like (in Asscending order) - first element is greater than adjacent element then swap them, for descending order - first element is less than adjacent element then swap them.
#3. Repeat: In each pass, you will able to arrange the maximum/minimum at last, and keep on repeating above step until the list is sorted.


"""
Example: Asscending Order
numList = [5,6,1,7,4,9,0]
First Pass: [5,1,6,4,7,0,9] 6
Second Pass: [1,5,4,6,0,7,9] 5
Third Pass: [1,4,5,0,6,7,9] 4
Fourth Pass: [1,4,0,5,6,7,9] 3
Fifth Pass: [1,0,4,5,6,7,9] 2
Sixth Pass: [0,1,4,5,6,7,9] 1


numList = [5,6,1,7,4,9,0]

for i in range(len(numList)):
    for j in range(len(numList)-i-1):
        if numList[j] > numList[j+1]:
            #swap adjacent element
            numList[j], numList[j+1] = numList[j+1], numList[j]
"""


#Asscending Order
# numList = [5,6,1,7,4,9,0]

# for i in range(len(numList)):
#     for j in range(len(numList)-i-1):
#         if numList[j] > numList[j+1]:
#             #swap adjacent element
#             numList[j], numList[j+1] = numList[j+1], numList[j]
#     # print(numList)

# print(f"list has sorted: {numList}")


#Descending Order

# numList = [5,6,1,7,4,9,0]

# for i in range(len(numList)): #1*n
#     for j in range(len(numList)-i-1): #n*n
#         if numList[j] < numList[j+1]:
#             #swap adjacent element
#             numList[j], numList[j+1] = numList[j+1], numList[j]
#     # print(numList)

# print(f"list has sorted: {numList}")

#Time Complexity for Bubble Sort is O(n^2)


# numList = [1,2,4,3,5,6,7,8,9]

# for i in range(len(numList)): 
#     swapped = False
#     for j in range(len(numList)-i-1): 
#         if numList[j] > numList[j+1]:
#             swapped = True
#             print("Value is True")
#             numList[j], numList[j+1] = numList[j+1], numList[j]  
#     if not swapped:
#         print("List is already in sorted order.")
#         break

# print(f"list has sorted: {numList}")

numList = [1,2,4,3,5,6,7,8,9]





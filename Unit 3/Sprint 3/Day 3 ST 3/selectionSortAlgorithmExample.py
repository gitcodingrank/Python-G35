#Sorting Algorithm: It is used to arrange the element in specefic order, commonly in accessding or decending order.

#There are following sorting algorithms:
#1. Selection Sort
#2. Bubble Sort
#3. Insertion Sort
#4. Merge Sort
#5. Quick Sort

#1. Selection Sort: it is comparsion-based algorithm that works by dividing the list into sorted and unsorted part and repeatedly searching for the smallest element in the unsorted part and sway with first element of unsorted part until the sequence is sorted.

#How does it work?
#1. Intial Setup: Start with the entire list as unsorted.
#2. Find the Mininum Element: Find minimum element from the unsorted part.
#3. Swap: Swap the minimum element with first element of unsorted part.
#4. Repeat: Move to next minimum element and swap keep doing this process until list is sorted.


#Example:

"""
list = [4,1,5,3,2] # need to sort this in accessnding order.
First Pass: Smallest Element in [4,1,5,3,2] is 1 swap with 4: [1, 4, 5, 3, 2]
Second Pass: Smallest Element in [4,5,3,2] is 2 swap with 4: [1,2,5,3,4]
Third Pass: Smallest Element in [5, 3, 4] is 3 swap with 5: [1,2,3,5,4]
Fourth Pass: Smallest Element in [5,4] is 4 swap with 5: [1,2,3,4,5]

Pseudo Code:
for i in range(len(list)-1):
    smallIndex = i
    for j in range(1, len(list)):
        if (list[j] < list[smallIndex]):
            smallIndex = j
    list[i], list[smallIndex] = list[smallIndex], list[i]
"""


list = [4,1,5,3,2]


#Ascending Order
# for i in range(len(list)-1):
#     smallIndex = i
#     for j in range(i+1, len(list)):
#         if (list[j] < list[smallIndex]):
#             smallIndex = j
#     list[i], list[smallIndex] = list[smallIndex], list[i]

# print(list)

#Descending Order:

# for i in range(len(list)-1):
#     largIndex = i
#     for j in range(i+1, len(list)):
#         if (list[j] > list[largIndex]):
#             largIndex = j
#     list[i], list[smallIndex] = list[largIndex], list[i]

# print(list)

#Inbuilt Function for sorting: sorted(iterable, Key=None, reversed=False)



# a = 4
# b = 5

# # #using third variable
# # temp = a
# # a = b
# # b = temp

# # print(a,b)

# #without using third variable

# a, b = b, a
# print(a, b)
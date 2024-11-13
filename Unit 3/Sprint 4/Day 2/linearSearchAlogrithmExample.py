#Linear Search: It is simple algorithm that sequentially checks every element of the list, if it finds then return that element otherwise return some msg.

#How does it work?
#1. Intial Setup: Start with any list(sorted or unsorted)
#2. Compare the element: It compares the target element with each element of the list.
#3. Target Element: if it finds target element any where in the list then it returns that element otherwise it returns some msg("not found", "nahi mila", -1, False).


"""
Analogy 1:
Example: 
list = [4,25,33,10,12,21]
target = 33
Round 1: compare 33 with 4 like target == list[0]
Round 2: compare 33 with 25 like target == list[1]
Round 3: compare 33 with 33 like target == list[2] - return that element/index/msg(found, mil gya) 


Analogy 2:
Example: 
list = [4,25,33,10,12,21]
target = 99
Round 1: compare 99 with 4 like target == list[0]
Round 2: compare 99 with 25 like target == list[1]
Round 3: compare 99 with 33 like target == list[2]
Round 4: compare 99 with 10 like target == list[3]
Round 5: compare 99 with 12 like target == list[4]
Round 6: compare 99 with 21 like target == list[5]

At last your msg: not found/nahi mila/-1/False


Other Works: It checks each element one by one, If it finds then return that element else return some msg.

"""

#Example: Given a list below, your task is to create a function named linearSearch that takes list, and target value as parameters, find the target value, if it is there return the index otherwise return -1.

# list = [4,25,33,10,12,21]
# target = 99

# def linearSearch(list, target):
#     for i in range(len(list)):
#         if list[i] == target:
#             return i
#     return -1

# print(linearSearch(list, target))
# print(linearSearch(list, 12))


mobilesList = [{}, {}, {}, {}]
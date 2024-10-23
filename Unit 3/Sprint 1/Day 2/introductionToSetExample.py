#Set - It is collection of unordered unique elements and it doesn't take any duplicate element.

#declaration of set

# numsSet = {1,2,3,4,5,6,7, 6}
# print(numsSet) #{1, 2, 3, 4, 5, 6, 7}

#Example: given number list, your task is to convert into set.

# nums = [num for num in range(1,11)]

# numSet = set(nums)
# print(numSet)

#Note: it doesn't support indexing.
# print(numSet[0]) # TypeError: 'set' object is not subscriptable

# fruits = {"apple", "banana", "orange", "grapes"}

# print(fruits)

# #how to add element to the set?
# #using add(), update()

# #using add() - stynax - setName.add(element)

# fruits.add("Mango")
# print(fruits)

# #using update() - to add multiple elements

# fruits.update(['Guava', 'Papaya'])

# print(fruits)


#how to delete element from the set?
#remove(element), #discard(element)

# fruits.remove("apple")

# print(fruits)

# # fruits.remove("apple") #gives error if the element not present in the set

# fruits.discard("apple") #it doesn't give any error if the element not present in the set.


# fruits = {"apple", "banana", "orange", "grapes"}

# for element in fruits:
#     print(element, end=" ")

# print({"apple", "apple", "banana", "mango"})

# print({1,1,1,1,3,2,2,2,4})

#Set Operation in maths:

set1 = {1,2,3}
set2 = {3,4,5}

#union - |
print(set1 | set2)

#intersection - &
print(set1 & set2)








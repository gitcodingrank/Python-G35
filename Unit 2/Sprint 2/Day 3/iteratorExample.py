#Iterator: it is just a object which is used to traverse through collection/sequence(list, tuple, string, set) using its next(iteratorObject).

nums = [34, 23, 45, 34, 2, 7]

# for i in nums:
#     print(i, end="")

# for i in range(len(nums)):
#     print(i, end="")

#In above example to get the each element from the list, Iterator internally get the item from the ang print() display on console.

iterator = iter(nums)

print(next(iterator)) #34
print(next(iterator)) #23
print(next(iterator)) #45
print(next(iterator)) #34
print(next(iterator)) #2
print(next(iterator)) #7

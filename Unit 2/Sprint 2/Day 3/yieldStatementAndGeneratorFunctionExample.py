#yield statement: 

# def printEvenNumbers(nums):
#     for i in nums:
#         if i%2==0:
#             yield i

# evenValues = printEvenNumbers([1,2,3,4,5,6,7])
# # print(next(evenValues))
# # print(next(evenValues))
# # print(next(evenValues))

# for i in evenValues:
#     print(i, end=" ")



def printNumbers(nums, index):
    if index>=len(nums):
        return
    yield nums[index]
    printNumbers(nums, index+1)

numbers = printNumbers([1,2,3,4,5,6,7],0)
for i in numbers:
    print(i, end=" ")

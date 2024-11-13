#Binary Search Algorithm: It is an efficient algorithm that works on sorted list.
#How does it work - it divides the search interval into two halves, if it checks if the target element is matching with mid element then it returns the index of that element, if the element is greater than the target element then it checks in right half, otherwise it checks in left half.

#1. Intial Setup: Start with sorted list.
#2. Divide the search Interval: it divides the search element into two halves and following operation:
"""
    2.1
    - it checks if the target element is matching with mid element then it returns that element.
    2.2
    - if the target element is greater then mid element then it searches in right half otherwise it searches in left half.
  """
#3. Repeat: Keeps on repeating the above task until you find the element if the element is not there you can return some msg.


"""
list = [1, 2, 4, 7, 8, 10, 14, 56, 78]
target = 1

code:

low, high = 0, len(list)-1
while(low<=high):
    mid = (low+high)//2
    if target == list[mid]:
        print(mid)
        break
    elif target < list[mid]:
        high = mid -1
    else:
        low = mid + 1

"""

list = [1, 2, 4, 7, 8, 10, 14, 56, 78]
target = 7

low, high = 0, len(list)-1
bag = -1
while(low<=high):
    # mid = (low + high)//2
    mid = low + (high-low)//2
    if target == list[mid]:
        bag = mid
        break
    elif target < list[mid]:
        high = mid -1
    else:
        low = mid + 1

print(bag)
#1. return is like a big bom whereas break is like a small bom.

def printEvenNumbers(nums):
    print("Starting of loop")
    for i in nums:
        if i%2==0:
            print(i)
            return
    print("Ending of Loop")

printEvenNumbers([1,2,3,4,5,6])

#2. return can give some expression from function whereas break can't do this.
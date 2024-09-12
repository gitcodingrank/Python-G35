
#while/for-else: else block is always executed once while/for loop has completed successfully.

# sp = 1
# while sp <=10:
#     print(sp)
#     sp+=1
# else:
#     print("While loop has completed.")

#Note: if you use break statement in while/for loop anywhere and if it gets executed then else block will not execute.


#Example 1: find first even number from 1 to 10 if you find anywhere just print that even number if you don't find anywhere then print, there is no even number for this range.
sp = 1
while sp<=10:
    if sp%2==0:
        print("Even", sp)
        break
    sp+=1
else:
    print("there is no even number for this range.") 



# for i in range(1, 11, 1):
#     if i%2==0:
#         print("Even", i)
#         break
# else:
#     print("there is no even number for this range.") 
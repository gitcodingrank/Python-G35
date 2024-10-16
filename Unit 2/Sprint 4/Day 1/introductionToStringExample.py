#String- it is collection/sequence of characters(numbers + letters + special symbols) enclosed with single, double and triple quatation marks.

#Examples: 

favoriteLetter = 'R'
name="Rakesh"
address= "Noida, Uttar Pradesh",
pincode="201301"
accountNumber="121213121212",
ifscCode="BOB2311F"
panCard= "ATSD9232D"
adhaarCard="23233493343322"
password="rakesh@1234"
descript="""Mere Khajane ki Chawi Store Room m hai"""

#Note: Most of the time data that string type variable is holding, we don't perform any kind of mathematical calculations.


#Point 2: Like List, String also follows 0 based indexing, meaning that first letter is at 0 index and so on.

name = "Chintu"

# print(name)
# print(name[0])
# print(name[1])
# print(len(name))

for i in name:
    print(i,end=" ")

print("")
for i in range(len(name)):
    print(name[i],end=" ")
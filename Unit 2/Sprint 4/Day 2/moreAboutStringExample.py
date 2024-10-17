#Example 1: 

# name = "Pablo"

# print(name[0])
# print(name[2])

# #1st Way:
# for item in name:
#     print(item, end=" ")

# #2nd Way:
# for i in range(len(name)):
#     print(name[i], end=" ")

#Note: String is immutable whereas list is mutable, in other words- string is unchangable whereas list is changable, meaining that you can change the data inside list but can't inside string.

#Examples:

#list: mutable - you can modify the list

# personName = ['T','r','a','k','a','s','h']
# personName[0] = 'P'
# print(personName)

# print("-------------------------------")

# #String: immutable - you can't modify the String

# name = "Trakash"
# #name[0] = 'P' #modification of existing string
# #name = "Prakash" #reassignment/replacement
# name = 420 #reassignment/replacement
# print(name)

#Problem 1: given below string your task is to replace T with P

#input
# name = "Trakash"
# #output - "Prakash"

# # updatedName1 = "P" + name[1:]
# # print(updatedName1)

# nameList = []
# for n in name:
#     nameList.append(n)

# nameList[0] = "P"

# updatedName = ""
# for i in nameList:
#     updatedName+=i

# print(updatedName)


#Problem 2: given string in small case, you need to make it capital

#input - name = "chitkara"
#output - "CHITKARA"

#solution:

name = "chitkara"
smallCaseLetter = "abcdefghijklmnopqrstuvwxyz"
capitalCaseLetter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

updateName = ""
for char in name:
    for i in range(len(smallCaseLetter)):
        if char == smallCaseLetter[i]:
            updateName+=capitalCaseLetter[i]

print(updateName)


#Problem 3: give list of fruits in small case your task is to make those string  in capital case.

#input - fruits = ["apple", "banana", "orange", "guava", "grapes"]
#output - fruits = ["APPLE", "BANANA", "ORANGE", "GUAVA", "GRAPES"]

#solution:

fruits = ["apple", "banana", "orange", "guava", "grapes"]

def makeStringCapital(str):       
    smallCaseLetter = "abcdefghijklmnopqrstuvwxyz"
    capitalCaseLetter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    updateName = ""
    for char in str:
        for i in range(len(smallCaseLetter)):
            if char == smallCaseLetter[i]:
                updateName+=capitalCaseLetter[i]
    return updateName

for i in range(len(fruits)):
    fruits[i] = makeStringCapital(fruits[i])

print(fruits)


#Problem:
#input - fruits = ["APPLE", "BANANA", "ORANGE", "GUAVA", "GRAPES"]
#output - fruits = ["apple", "banana", "orange", "guava", "grapes"]

    


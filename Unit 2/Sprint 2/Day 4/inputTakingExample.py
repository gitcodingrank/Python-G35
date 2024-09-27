# values = input("Enter Values: ")
# print(values, type(values))

sentence = "He is not studying Python"
list1 = sentence.split(" ")
print(list1)

#split(seperator) = it seperates the string by some seperator and convert into list.
#values = 23 12 34 23 35
# list1 = values.split(" ")
# print(list)

#1st: List Comprehension:
# intList = [int(num) for num in list]
# print(intList[0], type(intList[0]))

#2nd: using map()

# intList =  list(map(lambda x:int(x), list1))
# print(intList[0], type(intList[0]))



# values = [int(x) for x in input("Enter Values: ").split(" ")]
values = list(map(lambda x: int(x), input("Enter Values: ").split(" ")))
print(values, values[0], type(values[0]))
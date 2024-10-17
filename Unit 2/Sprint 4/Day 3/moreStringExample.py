#Problem 1: Given a string blow, your task is to check that the given string is palindrome or not.

# str1 = "madam"
# str2 = "car"
# print("Palindrome" if str1==str1[::-1] else "Not Palidrom")
# print("Palindrome" if str2==str2[::-1] else "Not Palidrom")

#Problem 2: given a string below, your task is to find out number of vowel in the string

str = "rishikesh"
vowels = "aeiou"

# count = 0
# for char in str:
#     if char in vowels:
#         count+=1

# print(f"Vowels in {str} is {count}")

#using list comperhension
# print(sum([1 for char in str if char in vowels]))


#String formating:
# #1. f-string
# # name = "Chaman"
# # city = "Noida"
# # msg = f"Hey, I'm {name} from {city}"

# #2. format()
# name = "Chaman"
# city = "Noida"
# msg = "Hey, I'm {} from {}".format(name, city)

# #3. string concatination
# name = "Chaman"
# city = "Noida"
# msg = "Hey, I'm "+name+" from "+city


#String inbuilt Functions:

#1. upper() - it makes particular string capital and returns the new string.
# str = "chitkara"
# print(str.upper())

#2. lower() - it makes particular string small and returns the new string.
# str = "CHITKARA"
# print(str.lower())

#3. split(bySeparator) - it is used to convert string into list.

# value = "12 13 14 15"
# result = value.split(" ")
# print(result)
# print([int(char) for char in result])
# print(list(map(lambda num: int(num), result)))

# name = "a-b-c-d"
# print(name.split("-")) # ['a','b','c','d']
# print(name.split("b")) # 

#4. capitalize() - it is used to make capital the first letter of the string.

# name = "chitkara"
# print(name.capitalize())  #Chitkara

#5. title() - it makes the first letter of each word in the string as capital.

# name = "chaman kumar singh"

# print(name.title()) #Chaman Kumar Singh

#6. endsWith() - it checks if particular string ends with particular string, and it returns True or False.

# str = "Hello World"

# print(str.endswith("World"))
# print(str.endswith("Worl"))
# print(str.endswith("d"))

#6. startsWith() - it checks if particular string starts with particular string, and it returns True or False.

# str = "Hello World"

# print(str.startswith("Hello")) #True
# print(str.startswith("lo")) #False
# print(str.startswith("H")) #True

#Example:- given list of string filter those string which are string which J, and make these strings a small.

#input - langs = ["Java", "Python", "Javascript", "C", "Php"]
#output - ["java", "javascript"]

langs = ["Java", "Python", "Javascript", "C", "Php"]

#Using HOF
# print(list(map(lambda str:str.lower(), list(filter(lambda str: str.startswith("J"), langs)))))

#Using List Comprehension
# print([str.lower() for str in langs if str.startswith("J")])





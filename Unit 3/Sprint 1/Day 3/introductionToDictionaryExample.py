#Dictionary - it is a data structure which is used to store the data in the form key-value pairs.


#Declaration of Dictionary:

# student = dict()
# print(student)
# print(type(student))

#Note: dictionary is collection of items/enteries, where each item/entery is collection of key and value.

#item/entry syntax: "key":value

#Note: 
#1. keys are always of string type whereas value can be of any type.

#2. keys are unique in dictionary wheres value you can take duplicate as well.

# student = {
#     "name": "Pablo",
#     "marks": 450,
#     "city": "Noida",
#     "skills": ["HTML", "CSS", "JS"],
#     "isMarried":True,
#     "subjects":("Maths", "Science", "English", "Computer")
# }

#print(student)

#How to access particular key's value in the dicitionary?
#solution - using key name
#syntax - dictionaryName["keyName"]

# print(student["name"])
# print(student["skills"])
# print(student["isMarried"])

# print(student["age"]) #KeyError: 'age'

#using get("keyName", defaultValue-None)

# print(student.get("name"))
# print(student.get("age")) #None
# print(student.get("age", "This key is not present in the dicitionary")) #This key is not present in the dicitionary

# student = {}

#How to add/update item/entery to the above student dictionary?
#1. dictionaryName["KeyName"] = value


# student["name"] = "Pawan"
# student["age"] = 34
# student["skills"] = ["HTML", "CSS", "JS", "React", "Python"]
# print(student)
# print(len(student))

# #2. to add/update multiple entries/items - update({})

# #additing the data.
# student.update({'city':"Noida", "isMarried":True})

# print(student)

# #updation
# student.update({'name':"chaman", "isMarried":False})

# print(student)

# student["name"] = "chintu"

# print(student)


#deleting the item/entry in the dicitonary

# person = {
#     "name": "chunnu",
#     "fatherName":"chaman lal",
#     "motherName": "munni devi",
#     "society":"Gopuldham"
# }

#1. del dictionaryName["keyName"]

# print(person)

# del person["motherName"]

# print(person)


#2. pop('keyName') - it deletes particular entry by keyName and also return value associated to that key.

# print(person)

# deletedKeyValue = person.pop('motherName')
# print(deletedKeyValue)

# print(person)

#3. popItem() - it deletes most recent added entry/item and return that entry in the form tuple.

# print(person)

# deletedRecentAddedItem = person.popitem()
# print(deletedRecentAddedItem)

# print(person)


#dicitionary inbuilt function -

# student = {
#     "name": "Pablo",
#     "marks": 450,
#     "city": "Noida",
#     "skills": ["HTML", "CSS", "JS"],
#     "isMarried":True,
#     "subjects":("Maths", "Science", "English", "Computer")
# }

#1. keys() - it returns all the keys of dictionary in the below format:
#dict_keys(['name', 'marks', 'city', 'skills', 'isMarried', 'subjects'])


# print(student.keys()) # dict_keys(['name', 'marks', 'city', 'skills', 'isMarried', 'subjects'])

# print(list(student.keys())) # ['name', 'marks', 'city', 'skills', 'isMarried', 'subjects']

# print(list(student.keys())[0])

#2. values() - it returns the value of the dictionary

# print(student.values()) #dict_values(['Pablo', 450, 'Noida', ['HTML', 'CSS', 'JS'], True, ('Maths', 'Science', 'English', 'Computer')])

# print(list(student.values()))

#3. items() - it returns items/entries(key-values) of dicitonary


#print(student.items()) #dict_items([('name', 'Pablo'), ('marks', 450), ('city', 'Noida'), ('skills', ['HTML', 'CSS', 'JS']), ('isMarried', True), ('subjects', ('Maths', 'Science', 'English', 'Computer'))])

# print(list(student.items()))


#inner dictionary:


employee1 = {
    "name":"Pawan Kumar",
    "department":"IT",
    "salary":"100000",
    "skills":["Problem Solving", "Web Devlopment"],
    "address":{
        "city":"Noida",
        "state":"Uttar Pradesh",
        "pincode":"201301"
    }
}

# print(employee1["address"]["city"])

# employee2 = {
#     "name":"Pawan Kumar",
#     "department":"IT",
#     "salary":"100000",
#     "skills":["Problem Solving", "Web Devlopment"],
#     "address":{
#         "homeAddress":{
#             "city":"Noida",
#             "state":"Uttar Pradesh",
#             "pincode":"201301"
#         },
#         "officeAddress":{
#             "city":"Delhi",
#             "state":"Delhi",
#             "pincode":"453422"
#         }
#     }
# }

# print(employee2["address"]["homeAddress"]["pincode"])
# print(employee2["address"]["officeAddress"]["city"])



#Examples: given student dicitonary below, your task is to print key and value in your format.

# student = {
#     "name": "Pablo",
#     "marks": 450,
#     "city": "Noida",
#     "skills": ["HTML", "CSS", "JS"],
#     "isMarried":True,
#     "subjects":("Maths", "Science", "English", "Computer")
# }

# for key, value in student.items():
#     print(f"key - {key} and value - {value}")


#Given student dictionary print only value of the dictionary using loop.

# for value in student.values():
#     print(value)


#Problem 1: print only those students which has marks greater than or equal to 350
studentList = [
    {"name":"Rakesh", "marks":450},
    {"name":"Pawan", "marks":120},
    {"name":"Suman", "marks":350},
    {"name":"Rohan", "marks":50}
               ]

for item in studentList:
    if item["marks"] >= 350:
        print(item)

#Problem 2: print only those students which has marks less than or equal to 350










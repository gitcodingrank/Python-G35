#Any Doubt in Dictionary?

#Understanding JSON format and its relationship with dictionary

#JSON - JSON(Javascript Object Notation) is lightweight data format which is used to store and exchange the data, its easy for humans to read and write, and machines to parse and generate.

#Note: it is data exchange format which is use to communicate between client and server.

#json format: it is a string or textual data.

#dictionary Example:

# student = {"name":"chaman","age":34,"city":"Noida"}

# #json student:

# student = '{"name":"chaman","age":34,"city":"Noida"}'


# #How to convert dictionary to json?

# import json

# python_student = {"name":"chaman","age":34,"city":"Noida"}

# print(python_student)
# print(f"python dictionary: {type(python_student)}")

# json_student = json.dumps(python_student)

# print(json_student)
# print(f"Json : {type(json_student)}")
# print(json_student[0])

#how to convert json to python dicitionary?
#json.loads(json)

# python_dictionary = json.loads(json_student)
# print(python_dictionary)
# print(type(python_dictionary))



#Examples: Given a list of student dictionary

studentList = [
    {
        "name":"Ramesh",
        "highestScore":450,
        "city":"Noida",
        "skills":["HTML", "CSS", "JS"]
    },
    {
        "name":"Punit",
        "highestScore":459,
        "city":"Delhi",
        "skills":["REACT", "JAVA", "PYTHON"]
    },
    {
        "name":"Gungun",
        "highestScore":159,
        "city":"Gurugram",
        "skills":["HTML", "CSS", "PYTHON"]
    },
    {
        "name":"Sargam",
        "highestScore":345,
        "city":"Ambala",
        "skills":["PYTHON", "AI", "HTML", "CSS", "JS"]
    },
    {
        "name":"Chintu",
        "highestScore":250,
        "city":"Delhi",
        "skills":["PYTHON"]
    },
    {
        "name":"Krishna",
        "highestScore":344,
        "city":"Noida",
        "skills":[".NET"]
    }
]



# print(studentList[1]["skills"])

#Problem 1: print the name and city of those students who belong to Delhi

#1st Solution: using normal loop

# for student in studentList:
#     if student["city"] == "Delhi":
#         print(f"Student Name: {student["name"]}, Student City: {student["city"]}")

#2nd List Comprehension:

# for stu in [student for student in studentList if student["city"] == "Delhi"]:
#     print(f"Student Name: {stu["name"]}, Student City: {stu["city"]}")

#3rd HOF: filter

# for stu in list(filter(lambda student: student["city"]=="Delhi", studentList)):
#     print(f"Student Name: {stu["name"]}, Student City: {stu["city"]}")


#Problem 2: print the name and city of those students who are skilled in Python.


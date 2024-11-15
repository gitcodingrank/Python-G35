#Some Advanced Modes: r+, w+, a+


#Note: How does cursor move?
#Curosor moves in both the cases (reading and writing).


#Mode: r+ - file opened for both reading and writing, if the file doesn't exist, it gives error.

#Note: in this case your cursor is beggining of file.
#Note: It doesn't erase(clear) the data on file opening.


# file = open('data.txt', 'r+')
# print(file.tell())
# print(file.read())
# print(file.tell()) #29
# # file.write("Let's Play Code")
# # print(file.tell())
# file.seek(0)
# file.write("Goto Chitkara")
# print(file.tell())
#file.close()


#Mode: w+ - opened with file in both reading and writing mode, if file doesn't exist then it creates the file.

#Note: on opening the file, it clears the data.
#Note: cursor points at beginning of the file.


# file = open('data.txt', 'w+')
# print(file.tell()) #0
# file.write("Java is complex")
# print(file.tell()) #15
# file.seek(0)
# print(file.read())


#Mode - a+ - opened the file for both reading and writing, if file doesn't exist, it creates the file.

#Note: on opening the file, it doesn't clear(truncate) the data.
#Note: by default cursor is at end of the file.

# file = open('data.txt', 'a+')
# print(file.read())
# file.seek(0)
# # print(file.read())
# print(file.tell())
# file.write("Chitkara")
# print(file.tell())


#Modern Way to open the file in any mode:

# with open('data.txt', 'r') as file:
#     print(file.read())


# students = ['Pablo', 'Bob', 'Raman', 'Kunal']

#Without JSON
# with open('data.txt', 'r+') as file:
#     file.write(" ".join(students))
#     file.seek(0)

#     #Logic to add new Student
#     data = file.read()
#     file.seek(0)
#     studentList = data.split()
#     studentList.append("Chintu")
#     file.write(" ".join(studentList))


#With JSON

# import json

# students = ['Pablo', 'Bob', 'Raman', 'Kunal']

# with open('data.txt', 'r+') as file:
#     # file.write(json.dumps(students))
#     file.seek(0)

#     #Logic to add new Student
#     studentList = json.loads(file.read())
#     print(studentList[0])
    # studentList.append("Chintu")
    # file.seek(0)
    # file.write(json.dumps(studentList))



#Example: 

import json

def readData():
    with open('students.json', 'r') as file:
        return json.loads(file.read())
    
def writeData(student):
    with open('students.json', 'r+') as file:
        studentsData = readData() 
        studentsData["students"].append(student)
        print(studentsData)
        file.write(json.dumps(studentsData))
        file.truncate()


writeData({"name":"Khushi", "marks": 123})













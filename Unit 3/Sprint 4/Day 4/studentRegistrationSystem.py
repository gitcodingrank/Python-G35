#Application - Student Registration System.
import uuid
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

def menu():
    print("1. Add Student")
    print("2. Get Student By Id")
    print("3. Get All Students")
    print("4. Update Student By Id")
    print("5. Delete Student By Id")
    print("6. Exit")


def addStudent():
    student = {}
    student["id"] = str(uuid.uuid4().int)[:10:]
    student["name"] = input("Enter Student Name: ")
    student["city"] = input("Enter Student City: ")
    student["marks"] = input("Enter Student Marks: ")
    writeData(student)
    print("Student has added successfully.")

def getStudentById():
    pass

def getAllStudents():
    for student in readData()["students"]:
        print(f"Student Name: {student["name"]}")
        print(f"Student City: {student["city"]}")
        print(f"Student Marks: {student["marks"]}")
        print("-----------------------------------")
def updateStudentById():
    pass

def deleteStudentById():
    pass


while True:
    menu()
    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        addStudent()
    elif choice == 2:
        getStudentById()
    elif choice == 3:
        getAllStudents()
    elif choice == 4:
        updateStudentById()
    elif choice == 5:
        deleteStudentById()
    elif choice == 6:
        res = input("Do you want to continue(y/n): ")
        if res in ['n', 'N']:
            print("Thank you using application..")
            break
    else:
        print("Invalid Input, please try again.")
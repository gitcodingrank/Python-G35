#Class - Blueprint/Structure to create object of same Blurprint/Structure.

"""
Syntax:
class ClassName:
    #class body

"""

# class Student:
#     #Class Attribute/Variable
#     state = "up"
#     def __init__(self, name, age, city):
#         #Instance Attributes/Variables
#         self.name = name
#         self.age = age
#         self.city = city

#     def __str__(self):
#         return f"Student Name: {self.name}, Age: {self.age}"


#Instance Attributes/Variables
#print(Student.name)
#Note: to access instance attribute/variable, it is important to create object

#Class Attributes/Variables
#Note: not neccessary to create the object.
# print(Student.state)


#Creation of object:
"""
Syntax:

variable/reference/instance = ClassName()
"""

# student1 = Student("Pawan", 45, "Noida")
#Note: here student1 is reference of Student class object.
# print(student1.name)
# print(student1.age)
# print(student1.city)
# print(student1.state)

#print(student1) #<__main__.Student object at 0x0000025619FE5F70>
#After overriding the __str__ function:
# print(student1)

# student2 = Student("Rakesh", 23, "Haryana")
# print(student2)


# class Account:

#     #How it looks/states/properties/attributes
#     #Class Attributes
#     bankName = "SBI"
#     ifscCode = "SBIN0045D"
#     def __init__(self, name, balance, accNumber):
#         #Instance Attributes
#         self.accountHolderName = name
#         self.availableBalance = balance
#         self.accountNumber = accNumber

#     #How it acts/behaviors/functionalities/methods
#     def depositAmount(self, accNumber, amount):
#         if self.accountNumber == accNumber:
#             self.availableBalance+=amount
#         else:
#             print("Invalid Credentials")

#     def withdrawalAmount(self, accNumber, amount):
#         if self.accountNumber == accNumber and self.availableBalance >= amount:
#             self.availableBalance-=amount
#         else:
#             print("Invalid Credentials")

#     def checkBalance(self, accNumber):
#         if self.accountNumber == accNumber:
#             return self.availableBalance
#         else:
#             return "Invalid Credentials"
        

# #Creating the object
# chamanAccount = Account("Chaman", 5000, "123456789")
# print(chamanAccount.checkBalance("123456789"))
# chamanAccount.depositAmount("123456789", 4000)
# print(chamanAccount.checkBalance("123456789"))

# print("----------------------------------------------------")

# rakeshAccount = Account("Rakesh", 4000, "12345")
# print(rakeshAccount.checkBalance("12345"))
# rakeshAccount.depositAmount("12345", 1000)
# print(rakeshAccount.checkBalance("12345"))


#Problem: Create a Employee Class with Instance attributes - employeeName, salary, departement, and also create 5 different objects.

# class Employee:
#     companyName = "TCS"
#     def __init__(self, name, salary, depart):
#         self.employeeName = name
#         self.employeeSalary = salary
#         self.department = depart


# employee1 = Employee("Rakesh", 50000, "Sales")
# print(employee1.employeeName)

# #Updating the object attribute value
# employee1.employeeName = "Pawan"
# print(employee1.employeeName)
# print(employee1.companyName)

#Updating the class Attribute
# employee1.companyName = "Wipro"
# Employee.companyName = "Wipro"
# print(employee1.companyName)

# print("-----------------------------------------------")

# employee2 = Employee('Suman', 40000, "IT")
# print(employee2.companyName)

#Good Problem: 

studentList = []


class Student:
    def __init__(self, id, name, age, city):
        #Instance Attributes/Variables
        self.rollNumber = id
        self.studentName = name
        self.studentAge = age
        self.studentCity = city
    
    def __str__(self):
        return f"Name: {self.studentName}, Age: {self.studentAge}, City: {self.studentCity}"

studentList.append(Student(12, 'Rakesh', 18, 'Noida'))
studentList.append(Student(45, 'Chaman', 23, 'Delhi'))
studentList.append(Student(34, 'Hitesh', 23, 'Haryana'))

# print(studentList[0])

for student in studentList:
    if student.studentCity == "Noida":
        print(student)


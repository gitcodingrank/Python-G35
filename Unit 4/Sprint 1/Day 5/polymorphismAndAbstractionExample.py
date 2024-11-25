#Polymorphism: As name suggests, one method can perform different task with different object.

#There are two types of polymorpshim:
#1. method overloading - [Discussed] - Python doesn't support it.
#2. method overriding -[Pending] - achieved by Inheritance.

# #Example: 
# class Vehicle:
#     def drive(self):
#         print("Vehicle is running.")


# class Bike(Vehicle):
#     # pass
#     #overridden the parent class method - method overriding.
#     def drive(self):
#         print("Bike is running.")

# class Car(Vehicle):
#     # pass
#     #overridden the parent class method - method overriding.
#     def drive(self):
#         print("Car is running.")

# bike = Bike()
# bike.drive()

# car = Car()
# car.drive()


#Abstraction: it hides the complex/code implementation and show only essential information to the user.

#Examples : Tv remote, ATM

#Note: you can achieve abstraction in python using abstract class.

#Abstract Class: its similar to other class but it contains abstract method with no implementation.
#Note: you can not create the object of abstract class.

#Abstract method: Abstract has no implementation in the abstract class, these methods are overridden by child class/implemented class.

#Note: to use abstract class in python, we need to use abc module in python.

# from abc import ABC, abstractmethod

# #User presentation
# #Abstract class
# class Shape(ABC):
    
#     @abstractmethod
#     def area(self): #unimplemented method
#         pass

#     @abstractmethod
#     def perimeter(self): #unimplemented method
#         pass

# # shape = Shape() #can't create the object of abstract class

# #implementationClass
# class Rectangle(Shape):

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width
    

# rectangle = Rectangle(5, 4)
# print(rectangle.area())


#Student Management System: 
#Student - addStudent,getStudent, getAllStudent, deleteStudent, updateStudent


# from abc import ABC, abstractmethod

# #Encapsulated class
# class Student:
#     pass



# class StudentService(ABC):

#     @abstractmethod
#     def addStudent(self):
#         pass

#     @abstractmethod
#     def getStudent(self):
#         pass

#     @abstractmethod
#     def getAllStudent(self):
#         pass

#     @abstractmethod
#     def deleteStudent(self):
#         pass

#     @abstractmethod
#     def updateStudent(self):
#         pass


# class StudentImplementationClass(StudentService):

#         def addStudent(self, student):
#             #provide impelmentation
#             pass

#         def getStudent(self):
#             #provide impelmentation
#             pass

#         def getAllStudent(self):
#             #provide impelmentation
#             pass

#         def deleteStudent(self):
#             #provide impelmentation
#             pass

#         def updateStudent(self):
#             #provide impelmentation
#             pass


# student1 = Student('name', 45, "Noida")

# implementationClass = StudentImplementationClass()
# implementationClass.addStudent(student)
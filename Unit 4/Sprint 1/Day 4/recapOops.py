#Problem 1: Create a student class that encapsulates student's name and grades and implement method to set grade and find the average.

class Student:
    def __init__(self, name):
        self.__name = name
        self.__grades = []
    
    def add_grade(self, grade):
        if 0 <= grade <=100:
            self.__grades.append(grade)
        else:
            print("Kindly provide the valid grade between 0 to 100")
    
    def find_average(self):
        return sum(self.__grades)/len(self.__grades) if len(self.__grades) > 0 else 0
    

student1 = Student('Rakesh')
student1.add_grade(10)
student1.add_grade(20)
student1.add_grade(30)
student1.add_grade(40)

print(student1.find_average())

#Problem: Create a Employee Class that encapsulate employee's name, salary, and deparment and provide getter and setter methods to access and modify the attribute.

#Solution - try by yourself


#Problem 3: Create a base/parent/super class 'Shape' with a method area() then create two child/derived/subclasses Circle and Rectangle, and implement the area() method differently for each.


# class Shape:
#     def area(self):
#         pass

# class Circle(Shape):
#     pi  = 3.14
#     def __init__(self, redius):
#         self.redius = redius

#     def area(self):
#         return self.pi * (self.redius ** 2)

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

# circle = Circle(5)
# print(circle.area())

# rectangle = Rectangle(20, 10)
# print(rectangle.area())


#Problem 4: Create a base/super/parent class 'Vehicle' with an attribute speed and a method drive() then create two child/subclasses/derived classes Car and Bike and implement drive method accroding the class.

# class Vehicle:
#     def __init__(self, speed):
#         self.speed = speed
    
#     def drive(self):
#         return f"Vehicle is running at speed {self.speed} km/h"

# class Bike(Vehicle):
#     def drive(self):
#         return f"Bike is running at speed {self.speed} km/h"
#     # pass
    

# class Car(Vehicle):
#     def drive(self):
#         return f"Car is running at speed {self.speed} km/h"
    
# bike = Bike(60)
# print(bike.drive())

# car = Car(90)
# print(car.drive())
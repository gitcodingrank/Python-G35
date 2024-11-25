#Polymorphism: it is combination of two words one is 'poly' which means 'many' and second is morphim which means 'forms'.
#in simple word, we can polymorphsim shows/perfoms different behavior according to the object.
#Other Worlds: One method perfrom different task according to the object.


#There are two types of polymorphism:
#1. Method Overloading - python doesn't support this feature but any how we can acchieve this using default argument operator.
#2. Method Overriding - Using Inheritance


#1. Method Overloading - same method different task according to object

#Example:

# print(len([1,2,3,4,5,67,34])) #7
# print(len("hello")) #5


# class Maths:
#     def findSum(*args):
#         return sum([args[num] for num in range(1, len(args))])
            

# maths = Maths()
# print(maths.findSum(1,12,3,4,5))#25
# print(maths.findSum(1,2)) #3
# print(maths.findSum(1,2,3)) #6


#Till Now in Object Oriented Programming:
#Object, Class, Encapsulation, Inheritance, Polymorphism[Pending], Abstraction[Pending]


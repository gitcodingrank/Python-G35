#Important Pillars of Object Oriented Programming:
#1. Encapsulation
#2. Inheritance
#3. Polymorphism
#4. Abstraction

#1. Encapsulation
#Why Encapsulation

# class Account:
#     __bankName = "SBI"
#     ifscCode = "SBIN0045F"
#     def __init__(self, name, balance, accNumber):
#         self.accountHolderName = name
#         self.__availableBalance = balance #private instance attribute
#         self.accountNumber = accNumber

# account1 = Account("Rohan", 5000, "12345")
# # print(account1.__availableBalance)
# # print(account1.__bankName)

# #Encapsulation - It is used to bundle all the properties and behaviors(methods) as a single unit by making them private so that none can access outside the class.
# #In Short - It is the process of making methods and variables as private.

# #Note: as a developer, it is mendatory to have the fully encapsulated class.

# """
# full encapsulated class:
# 1. make all the instance attribute/variable as private
# 2. make all the class attribute/variable as private
# 3. make all the instance methods as private [Optional and according to your intelligence]
# 4. define getter and setter methods to access the data
# """


# # class Account:
# #     __bankName = "SBI"
# #     __ifscCode = "SBIN0045F"
# #     def __init__(self, name, balance, accNumber):
# #         self.__accountHolderName = name
# #         self.__availableBalance = balance #private instance attribute
# #         self.__accountNumber = accNumber

# #     def depositAmount(self, accNumber, amount):
# #         if self.__accountNumber == accNumber:
# #             self.__availableBalance+=amount
# #         else:
# #             print("Invalid Credentials")

# #     def withdrawalAmount(self, accNumber, amount):
# #         if self.__accountNumber == accNumber and self.__availableBalance >= amount:
# #             self.__availableBalance-=amount
# #         else:
# #             print("Invalid Credentials")

# #     def checkBalance(self, accNumber):
# #         if self.__accountNumber == accNumber:
# #             return self.__availableBalance
# #         else:
# #             return "Invalid Credentials"
# #     #getter method - to get the data of instance and class variable
# #     def getAccountHolderName(self):
# #         return self.__accountHolderName
    
# #     def getAccountNumber(self):
# #         return self.__accountNumber
    
# #     def getAvailableBalance(self):
# #         return self.__availableBalanceBalance
    
# #     #setter methods - to set the value of instance and class variable.

# #     def setAccountHolderName(self, name):
# #         self.__accountHolderName = name
    
# #     def setAccountNumber(self, accNumber):
# #         self.__accountNumber = accNumber

# #     def setAvailableBalance(self, balance):
# #         self.__availableBalanceBalance = balance
        

# # pawanAccount = Account('Pawan', 5000, "12345")
# # # print(pawanAccount.checkBalance("12345"))
# # print(pawanAccount.getAccountHolderName())
# # pawanAccount.setAccountHolderName("Pawan Kumar")
# # print(pawanAccount.getAccountHolderName())


# class User:
#     def __init__(self, name):
#         self.name = name
#         self.__loginStatus = False
    
#     def __verifyEmail(self, username):
#         #validation logic
#         return True

#     def __verifyPassword(self, password):
#         #validation logic
#         return True

#     def login(self, username, password):
#         isVerified = False
#         isVerified = self.__verifyEmail(username) and self.__verifyPassword(password)

#         if isVerified:
#             self.__username = username
#             self.__password = password
#             self.__loginStatus = True
#             print("Logged In Successfully")
#         else:
#             print("Invalid username and password")
    
#     def logout(self):
#         self.__loginStatus = False
#         print("Logged out successfully")
    
#     def printUserDetails(self):
#         if self.__loginStatus:
#             print(f"Name: {self.name}")
#             print(f"Username: {self.__username}")
#             print(f"Password: {self.__password}")
#         else:
#             print("You're logged out, please login")


# user1 = User('rakesh')
# # print(user1.username)
# # print(user1.password)
# user1.login('rakesh@gmail.com', "12345")
# # print(user1.username)
# # print(user1.password)

# # print(user1.verifyEmail("radom@agdladfjssf"))
# user1.logout()
# user1.printUserDetails()


#Inheritance: it allows class to use/inheritate the property of parent class.
#Note: rather than owning its better to owe.

"""
Example: Cat Family - Tiger - Lion

class Cat:
    #Same Property
    fur=True
    jump=True
    legs = 4
    tail = True
    #Differnt Property
    name = Cat

class Tiger:
    #Same Property
    #Note - can use from Cat class using inheritance
    #Differnt Property
    name = Tiger

class Lion:
    #Same Property
    #Note - can use from Cat class using inheritance
    #Differnt Property
    name = Lion
 
"""


class Cat: #parent class
    fur=True
    jump=True
    legs = 4
    tail = True
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Name: {self.name}, Fur: {self.fur}, Jump: {self.jump}"

class Tiger(Cat): #child/concrete class
    pass

class Lion(Cat):
    pass

cat = Cat("Cat")
tiger = Tiger("Tiger")
lion = Lion("Lion")

print(cat)
print(tiger)
print(lion)




#Python support various kind of programming paradigm(way of writing code) to develop an application like:

#1. Proceduture Programming.
#2. Functional Programming.
#3. Object Oriented Programming.

#Why Object Oriented Programming?
#Note: Object is the first citizen in case of object oriented programing.

#What is "object"?

#Reason 1: Object is real world entity and in each real world object, we have two common things, first how they look, and second how they act.

"""
Example: 
Laptop: Object
How it looks/state/properties:
    brandName
    color
    wieght
    Ram
    Rom
    Processor
How it acts/behaviors/functionalities:
    playMusic
    writeDocument
    writeCode
    developApplication

Mobile: Object
How it looks/state/properties:
    brandName
    modelName
    frontCamera
    backCamera
    battery
    Ram
    display
How it acts/behaviors/functionalities:
    videoCall
    audioCall
    doMsg
    playVideo
    playMusic

Account: Object
How it looks/state/properties:
    accountHolderName
    availableBalance
    ifscCode
    accountType
    adhaarNumber
    panNumber
How it acts/behaviors/functionalities:
    depositMoney
    checkBalance
    withdrawalMoney
    checkLoanEligibilty

Before Object Oriented Programming, we're having to write these state and behaviour sepereatly

Example:

"""
#Example
#Account: Object

#how it acts/behaviours/functionalities

def depositAmount(accountNumber,availBalance,amount):
    if accountNumber=="123456789":
        availBalance+=amount
        print(f"{amount} has credited to your account {accountNumber} successfully")
        return availBalance
    else:
        print(f"invalid account number {accountNumber}")
        return availBalance

def withdrawalAmount(accountNumber,availBalance, amount):
    if accountNumber=="123456789":
        if availBalance>=amount:
            availBalance-=amount
            print(f"{amount} has debited from your account {accountNumber} successfully")
            return availBalance
        else:
            print("Insufficient Fund.")
            return availBalance
    else:
        print(f"invalid account number {accountNumber}")
        return availBalance

def checkBalance(accountNumber, availBalance):
    if accountNumber=="123456789":
        print(f"Available Balance is {availBalance}")
    else:
        print("Invalid Account Number")



#how it looks/state/properties
accountNumber = "123456789"
availableBalance = 5000


#Operations
checkBalance(accountNumber, availableBalance)
availableBalance = depositAmount(accountNumber, availableBalance, 5000)
checkBalance(accountNumber, availableBalance)
withdrawalAmount(accountNumber, availableBalance, 11000)
checkBalance(accountNumber, availableBalance)

#In this way your data is not secure and reusable.

#But with help of object oriented programming we can bind these state and behavior as single entity and can also use it again and again.



#Object Oriented Programming: It is one of most popular programming paradigm to develop and application.

#Why OOPS:
#Reusability
#Modalarity
#Data Security
#Encapsulation
#Inheritance
#Data Abstraction

#class: it is blueprint/structure to create objects.

#object: it is an instance of class, which has two things state and behavior.
#Note: you can create n numbers of object of a class.

class Mobile:
    #state and behaviors
    pass


#obejects
mobileOne = Mobile()





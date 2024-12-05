#csv - comman seperated values - to store the data in the tabular format(rows and columns).

import csv

#read the csv file.

# data = [
#     ["Name", "Email", "City"],
#     ["Pawan", "pawan@gmail.com", "Noida"],
#     ["Rakesh", "rakesh@gmail.com", "Delhi"]
#     ]
# with open('data.csv', 'w', newline='') as file:
#     writer = csv.writer(file,)

#     # writer.writeheader()
#     writer.writerows(data)

# with open('data.csv', 'r') as file:
#     # print(file.read())
#     reader  = csv.reader(file)
#     for row in reader:
#         print(row)

# data = [
#     {'name':"Rakesh", 'email':"rakesh@gmail.com", 'city':"Noida"},
#     {'name':"Rohan", 'email':"rohan@gmail.com", 'city':"Delhi"},
#     {'name':"Pawan", 'email':"pawan@gmail.com", 'city':"Haryana"},
#     {'name':"Rishabh", 'email':"rishabh@gmail.com", 'city':"Noida"}
# ]

# #convert dictionary data into csv file
# with open('data.csv', 'w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "email", "city"])
#     writer.writeheader()
#     writer.writerows(data)

#convert csv file data into dictionary
# list = []
# with open('data.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         list.append(row)

# print(list)


#how to delete the file.

# import os



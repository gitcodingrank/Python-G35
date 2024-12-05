#csv: comman seperated values - to store the data in the tabular format(rows and columns)
"""
syntax: csv looks like below
Name, Email, City
Rakesh, rakesh@gmail.com, Noida
"""

# import csv


#reading the csv file
# with open('data.csv', 'r') as file:
#     data = csv.reader(file)
    
#     for row in data:
#         print(row)

#writing the csv file

# data = [['Name', 'Email', 'City'], ['Chaman', 'chaman@gmail.com', 'Noida']]

# with open('data.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
    
#     writer.writerows(data)

# with open('data.csv', 'w', newline='') as file:
#     csv.DictWriter(file)
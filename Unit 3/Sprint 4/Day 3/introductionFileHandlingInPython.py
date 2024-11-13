#FIle Handling: This a way to interact with your files in your computer where you can perform reading, writing and modification operation on file using this concept.


#Opening and Closing the Files:
# Syntax - open(file, mode)
#mode - read(r), writing(w), appending(a)


#Reading Mode
# file = open('note.txt', 'r')
# # print(file)
# #<_io.TextIOWrapper name='note.txt' mode='r' encoding='cp1252'>
# print(file.read())
# file.write("Hello Students")


#Writing Mode
#mode -w - before writing anything, it erases the entire file data.
# file = open('note.txt', 'w')
# #print(file)
# #<_io.TextIOWrapper name='note.txt' mode='w' encoding='cp1252'>
# file.write("Learning Python")

#Appending Data
#mode - a - it doesn't erase the data of the file while writing else it add the data end of the existing data in the file.

# file = open('./note.txt', 'a')
# file.write("\nSaerching using Binary Search")

#Example: 

#Positioning in the File.
#tell() - it returns the cursor position, by default your cursor position is at 0
#seek(position) - it is used to reset the position of the cursor

# file = open('note.txt', 'r')
# print(file.tell()) 
# file.seek(5)
# print(file.tell())
# print(file.read())


# file = open('note.txt', 'r')
# # print(file.readline())
# # print(file.readline())
# # print(file.readline())

# print(file.readlines())


#Problem: given a file named note.txt, you need to replace the data python as Java
"""
note.txt:
# --------
# I am learning Python
# Python is Easy To Learn
# """

# file1 = open('note.txt', 'r')
# data = file1.read()
# # print(type(data))
# modifiedData = data.replace('Python', 'Java')
# print(modifiedData)

# file2 = open('note.txt', 'w')
# file2.write(modifiedData)




#Important File Modes:
"""
| Mode | Description |
| ---   | -----------| 
| `'r'` | Read-only mode |
| `'w'` | Write-only mode (overwrites file) |
| `'a'` | Append mode |
| `'r+'`| Read and write without clearing, it writes the data from the end of the file |
| `'w+'`| Write and read (clears file), starting of the file. |
| `'a+'`| Append and read |
"""

# file = open('note.txt', 'r+')
# print(file.read())
# print(f"Before Adding Cursor: {file.tell()}")
# file.write("Data is complex")
# print(f"After Adding Cursor: {file.tell()}")


# file = open('note.txt', 'r+')
# #print(file.read())
# #file.seek(0)
# file.write("Chintu is Geneous")
# print(f"After Adding Cursor: {file.tell()}")


file = open('note.txt', 'w+')
# print(file.read())
# print(file.tell())
# file.write("I am going to Patna")
# print(file.read())
# print(file.readline())
# file.seek(0)
# print(file.read())



file = open('note.txt', 'a+')
# print(file.read())
file.write("Data is Available")
# print(file.read())


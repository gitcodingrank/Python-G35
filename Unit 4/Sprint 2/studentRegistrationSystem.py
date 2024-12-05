from tkinter import *
from tkinter.messagebox import showerror, showinfo, showwarning
import uuid
import os
import json
import csv
    #os - renameFile, deleteFile, check file is there or not.
    
def getStudents():
    if not os.path.exists('student.json'):
          with open('student.json', 'w') as file:
            file.write(json.dumps({"students":[]}))
    with open('student.json', 'r') as file:
         return json.loads(file.read())
        

def registerStudent():
    try:
        student = {}
        student["id"] = str(uuid.uuid4().int)[:15:]
        student["name"] = name.get()
        student["email"] = email.get()
        student["city"] = city.get()

        if not all([student["name"], student["city"], student["email"]]):
            raise ValueError("You can't leave any field empty.")
        
        #code to add student into student.json file
        data = getStudents()
        #data = { "students":[]}
        foundStudents = list(filter(lambda stu: stu["email"]==student["email"], data["students"]))
        if len(foundStudents)>0:
            showwarning(title="Student Already Exists", message="Can't add the duplicate student with email.")
            return

        data["students"].append(student)

        with open('student.json', 'w') as file:
             json.dump(data, file, indent=4)
             showinfo(title="Registered Successfully", message="Student has successfully registered")

    except ValueError as e:
            showwarning(title="All Fields Required", message=f"{str(e)}")

def downloadStudentDataInCsv():
    studentData = getStudents()["students"]
    print(studentData)

    with open('data.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id","name", "email", "city"])
        writer.writeheader()
        writer.writerows(studentData)
        showinfo(title="Successfully Downloaed",message="data.csv file has downloaded in the current folder.")


win = Tk()
win.title("Student Registration System")
# win.config(bg="teal")


#to keep window on center of the entire system screen.
width = 800
height = 500
screenWidth = win.winfo_screenwidth()
screenHeight = win.winfo_screenheight()
x = int(screenWidth/2 - width/2)
y = int(screenHeight/2 - height/2)
win.geometry(f"{width}x{height}+{x}+{y}")

lb = Label(win, text = "Welcome to Student Registration System", bg="red", fg="white", font=(30))
lb.pack(side=TOP, fill=X, ipady=20)

#Frame is like div/box
registrationFrame = Frame(win, bg="teal")
registrationFrame.place(relx=.5, rely=.5, anchor="center", width=500, height=300)

name = StringVar()
email = StringVar()
city = StringVar()

#name
nameLabel = Label(registrationFrame, text="Enter Name:",font=(25), bg="teal", fg="white")
nameLabel.place(x=20, y=40)
nameEntry = Entry(registrationFrame, font=(25), textvariable=name)
nameEntry.place(x=140, y=40, width=300, height=30)

#email
emailLabel = Label(registrationFrame, text="Enter Email:",font=(25), bg="teal", fg="white")
emailLabel.place(x=20, y=90)
emailEntry = Entry(registrationFrame, font=(25), textvariable=email)
emailEntry.place(x=140, y=90, width=300, height=30)


#email
cityLabel = Label(registrationFrame, text="Enter City:",font=(25), bg="teal", fg="white")
cityLabel.place(x=20, y=140)
cityEntry = Entry(registrationFrame, font=(25), textvariable=city)
cityEntry.place(x=140, y=140, width=300, height=30)


btn = Button(registrationFrame, text="Register Student", command=registerStudent, bg="yellow", font=(25))
btn.place(x=20, y=200, width=200, height=30)

csvBtn = Button(registrationFrame, text="Download Student Data", command=downloadStudentDataInCsv, bg="white", font=(25))
csvBtn.place(x=20, y=240, width=250, height=30)

win.mainloop()
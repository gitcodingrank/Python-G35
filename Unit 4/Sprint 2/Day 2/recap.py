from tkinter import *

# def clickFun():
#     lb.config(text="Somebody has clicked on button")

def showText():
    print(boxText.get())
    lb.config(text=boxText.get())


def showGender():
    print(gender.get())


win = Tk()
win.title("Chitkar University")
win.config(bg="teal")


#to keep window on center of the entire system screen.
width = 800
height = 500
screenWidth = win.winfo_screenwidth()
screenHeight = win.winfo_screenheight()
x = int(screenWidth/2 - width/2)
y = int(screenHeight/2 - height/2)
win.geometry(f"{width}x{height}+{x}+{y}")

#widget/tag/element = Lable, Frame, Button, Entry, Text, RadioButton, Checkbox etc.
#Label: its a widget which is used to show text
# lb1 = Label(win, text = "Welcome to Chitkara University", font=('Roboto', 25, "bold"), bg="red", fg="white")
# lb1.place(x=100, y=20)

# lb2 = Label(win, text = "Python Programming", font=('Roboto', 25, "bold"), bg="yellow")
# lb2.place(x=100, y=70)

# btn = Button(win, text = "Click Me", font=(25), relief="raised", cursor="hand2", command=clickFun)
# btn.place(x=10, y=20, width=200, height=60)

# lb = Label(win, text="", font=(25), bg="teal")
# lb.place(x=10, y=100)


#tkinter variables: StringVar(), IntVar(), DoubleVar(), BooleanVar()

# name = StringVar(value = "Rakesh Kumar")
# print(name.get())
# name.set("Pawan Kumar")
# print(name.get())


# age = IntVar(value = 34)
# print(age.get())
# age.set(35)
# print(age.get())


# salary = DoubleVar(value = 59000.34)
# print(salary.get())
# salary.set(100000)
# print(salary.get())


# isMarried = BooleanVar(value = False)
# print(isMarried.get())
# isMarried.set(True)
# print(isMarried.get())


# boxText = StringVar()

#Entry - like input box
# box = Entry(win, font=(25), textvariable=boxText)
# box.place(x=20, y=20, width=300, height=30)

# btn = Button(win, text="Show Text", command=showText)
# btn.place(x=20, y=70)

# lb = Label(win, text="", font=(25), bg="teal")
# lb.place(x=20, y=100)

# gender = StringVar()

# maleRadio = Radiobutton(win, text="Male", variable=gender, value="Male", command=showGender)
# maleRadio.place(x=20, y=140)

# femaleRadio = Radiobutton(win, text="Female", variable=gender, value="Female", command=showGender)
# femaleRadio.place(x=20, y=180)





win.mainloop()
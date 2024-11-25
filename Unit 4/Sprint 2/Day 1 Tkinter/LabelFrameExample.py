from tkinter import *


root = Tk()
width = 800
height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")


#LabelFrame

labelFrame = LabelFrame(root, bg="teal")
# labelFrame.place(x=100, y=100, height=400, width=700)
labelFrame.place(relx=.5,rely=.5, height=400, width=400, anchor='n')

lb1 = Label(labelFrame, text="Hello Everyone", bg="teal", fg="white",font=(20))
lb1.place(x=20, y=20)

lb2 = Label(labelFrame, text="Chitkara University", bg="teal", fg="white",font=(20))
lb2.place(x=20, y=50)



root.mainloop()
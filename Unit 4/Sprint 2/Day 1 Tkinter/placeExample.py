from tkinter import *

root = Tk()
width = 500
height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")


# lb1 = Label(root, text="Name", font=(30), bg="whitesmoke",fg="black", relief='sunken', bd=5)
# lb1.place(x=200, y=200, width=200, height=40)


lb1 = Label(root, text="Name", font=(30), bg="whitesmoke",fg="black", relief='sunken', bd=5, cursor="plus")
lb1.place(relx=.5,rely=.5, width=500, height=200, anchor='n')





root.mainloop()
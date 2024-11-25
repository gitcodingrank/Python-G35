from tkinter import *

root = Tk()
width = 500
height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")


lb1 = Label(root, text="Name", font=(30), bg="red",fg="white")
lb1.grid(row=0, column=0, padx=10)

lb2 = Label(root, text="City", font=(30), bg="red",fg="white")
lb2.grid(row=0, column=1, padx=10)

lb3 = Label(root, text="Chaman", font=(30), bg="red",fg="white")
lb3.grid(row=1, column=0, padx=10, pady=10)

lb4 = Label(root, text="Noida", font=(30), bg="red",fg="white")
lb4.grid(row=1, column=1, pady=10, padx=10)



root.mainloop()
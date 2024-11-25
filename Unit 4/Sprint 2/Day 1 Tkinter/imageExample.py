from tkinter import *

# Create the main window
win = Tk()
win.title("Image Example")
win.geometry("400x400")

# Load the image
img = PhotoImage(file="example.png")

# Create a label to display the image
label = Label(win, image=img)
label.pack()  # Automatically places the label

win.mainloop()
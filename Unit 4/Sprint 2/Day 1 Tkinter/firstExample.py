#To use Tkinter, its neccessary to import it

# from tkinter import Tk, ttk
from tkinter import *

root = Tk()
root.title("Chitkara University")
# root.config(bg="yellow")
root['bg'] = "red"
# root.geometry("800x500+200+50")

#to keep the initial window on center:
width = 500
height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")

# root.resizable(False, False)
# root.attributes('-alpha', 0.1) 

root.mainloop()
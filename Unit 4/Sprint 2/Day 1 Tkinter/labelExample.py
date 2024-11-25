from tkinter import *


win = Tk()

width = 800
height = 500
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)
win.geometry(f"{width}x{height}+{x}+{y}")

win["bg"] = 'cyan'

#Label: It is like p/headings which is used to show text on window.

lb1 = Label(win, text = "Chiktara University", font=('Time New Roman', 30, 'bold'), bg="yellow")
# lb1.pack(ipadx=30, ipady=50, side=TOP, padx=50, pady=50)
lb1.pack(side=LEFT, fill=Y)

# lb2 = Label(win, text = "Body", font=('Time New Roman', 30, 'bold'), bg="red")
# # lb1.pack(ipadx=30, ipady=50, side=TOP, padx=50, pady=50)
# lb2.pack(side=TOP, fill=BOTH, expand=True)


lb3 = Label(win, text = "Python Programming", font=('Time New Roman', 30, 'bold'), bg="red")
# lb1.pack(ipadx=30, ipady=50, side=TOP, padx=50, pady=50)
lb3.pack(side=RIGHT, fill=Y)
 

win.mainloop()
from tkinter import Frame, Label, Tk
from time import strftime

# Creating frame and labels
root = Tk()
root.title("Digital Clock")
root.configure(background="#041014")
clock = Label(root, font=("technology", 40),background="#041014", foreground="#2fff05")
clock.pack()
Label(root, text="---Digital Clock---", font=("Ubuntu", 12),
      background="#041014", foreground="#2fff05").pack(anchor="s")

def time_config():
    """Update current time"""
    clock.config(text=strftime("%H:%M:%S"))
    clock.after(100, time_config)

time_config()
root.mainloop()
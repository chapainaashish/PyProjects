# Digital Clock using tkinter and date time module

from datetime import date
from tkinter import Frame, Label, Tk
from time import strftime
from tkinter.constants import RAISED, SUNKEN, TOP


# Configuring windodw
root = Tk()
root.geometry("400x200")
root.configure(background="black")
root.title("Digital Clock")

# Creating Frame
frame2 = Frame(root, bg="black", relief=RAISED)
frame2.pack(side=TOP)

# Adding header
root_text = Label(
    frame2,
    text="Digital Clock",
    font=("ubuntu", 20),
    background="black",
    foreground="green",
)
root_text.pack(anchor="s")

# Configuring Clock Label
clock = Label(
    frame2, background="black", fg="green", font=("ubuntu", 25), relief=SUNKEN
)
clock.pack()

# Configuring Date Label
date_label = Label(frame2, background="black", fg="green", font=("ubuntu", 10))
date_label.pack()


def time_config():
    """Configuring Current Date and Time"""
    # setting label text as curren time
    clock.config(text=strftime("%H: %M: %S"))

    # calling function again and again
    clock.after(100, time_config)

    # setting label text as current date
    date_label.config(text=date.today().strftime("%B %d, %Y"))
    date_label.update()


time_config()
root.mainloop()

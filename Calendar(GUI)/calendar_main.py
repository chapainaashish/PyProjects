# Author: Aashish Sharma
# Github: https://github.com/aasis2520c

# A GUI based calendar
import calendar
from tkinter import Entry, Tk, Label, Button, IntVar
# Customizing root window
root = Tk()
root.geometry("200x150")
root.configure(background="black")
root.title("Calendar")


def year_submit():
    # Customizing new window and displaying calendar
    new_root = Tk()
    new_root.geometry("900x900")
    new_root.configure(background="black")
    new_root.title(f"Calendar {year_field.get()}")

    # Adding label and displaying it
    year_calendar = Label(new_root, text=calendar.calendar(
        int(year_field.get())), foreground="white", background="black", font=("consolas", "12", "bold"))
    year_calendar.pack()


# Adding header
root_text = Label(root, text="Calendar", background="black",
                  fg="white", font=("garuda", 18, "bold"))
root_text.pack(anchor="s")

# Initializing Label
name = Label(root, text="Year", background="black", foreground="white")
name.pack(anchor="s")

yearvar = IntVar()
# Creating Entry field
year_field = Entry(root, background="black",
                   textvariable=yearvar, foreground="white")
year_field.pack(anchor="s")

# Creating button
submit_button = Button(root, text="Enter", background="black",
                       foreground="white", command=year_submit)
submit_button.pack(anchor="s", pady=10)


root.mainloop()

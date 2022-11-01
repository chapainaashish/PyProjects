# Author: Aashish Sharma
# Github: https://github.com/aasis2520c

# A GUI based calendar
import calendar
from tkinter import Entry, Tk, Label, Button, IntVar
# Customizing root window
root = Tk()
root.geometry("200x200")
root.configure(background="black")
root.title("Calendar")

class month:
    def __init__(self, root, year, id):
        self.month = Label(root, 
            text=calendar.month(year, id, w=3, l=1), 
            justify="left", anchor="n",
            foreground="white", background="black", font=("consolas", "11", "bold"))
    def print_month(self, r, c):
        self.month.grid(row=r, column= c, sticky="n", pady=10, padx=10)

def close(event):
    quit()

def year_submit():
    # Customizing new window and displaying calendar
    new_root = Tk()
    new_root.geometry("900x900")
    new_root.configure(background="black")
    new_root.title(f"Calendar {year_field.get()}")

    theyear = int(year_field.get())
    #
    months=[]
    for m in range(1,13):
        months.append(month(new_root, theyear, m))
        months[m-1].print_month((m-1) // 3, (m-1) % 3)


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
Button(root, text="Quit", command=root.quit).pack()
root.bind('<Escape>',close)

root.mainloop()
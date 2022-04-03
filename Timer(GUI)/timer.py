# Timer GUI with tkinter
from tkinter import Tk, Label, Button, IntVar, Entry


def timer(*event):
    import time
    # getting entry field value
    user_hour = int(hour_field.get())
    user_min = int(minute_field.get())
    user_sec = int(second_field.get())
    while True:
        # Handling invalid input
        if user_min > 60 or user_sec > 60:
            timing_text.config(text="Enter Valid Input!", foreground="red")
            timing_text.update()
            timing_text.grid(row=12, column=1)
            break

        # Terminating timer if hour become less than 0
        if user_hour == -1:
            timing_text.config(text="Time Over!", foreground="red")
            timing_text.update()
            timing_text.grid(row=12, column=1)
            break
        # Reducing hours as the value of minute
        if user_min == -1:
            user_hour = user_hour - 1
            user_min = 59
            continue

        # Reducing minutes as the value of second
        if user_sec == -1:
            user_min = user_min - 1
            user_sec = 59
            continue

        else:
            # Displaying Timing Information
            timing = f"{user_hour}:{user_min}:{user_sec}"
            timing_text.config(text=timing, foreground="green")
            timing_text.update()
            timing_text.grid(row=11, column=1)
            time.sleep(1)
            # Reducing second for each iteration
            user_sec -= 1


# Coustomizing window
root = Tk()
root.geometry("588x433")
root.minsize(588, 433)
root.maxsize(688, 533)
root.configure(background="black")
root.title("Timer")

# Adding header
root_text = Label(root, text="Timer", background="black",
                  fg="white", font=("garuda", 25))
root_text.grid(column=1)

# Adding Label
# Hoor, Minute, Second
hour = Label(root, text="Hour\t|HH|",
             background="black", foreground="white")
minute = Label(root, text="Minutes\t|MM|",
               background="black", foreground="white")
second = Label(root, text="Seconds\t |SS|",
               background="black", foreground="white")

# Packing label as grid
hour.grid(row=5, column=0, ipadx=40)
minute.grid(row=6, column=0)
second.grid(row=7, column=0)

# Setting variable
hour_var = IntVar()
minute_var = IntVar()
second_var = IntVar()

# Creating Entry field
hour_field = Entry(root, textvariable=hour_var,
                   background="black", foreground="white")
minute_field = Entry(root, textvariable=minute_var,
                     background="black", foreground="white")
second_field = Entry(root, textvariable=second_var,
                     background="black", foreground="white")

# Packing Entry field as grid
hour_field.grid(row=5, column=1, pady=3, ipadx=30)
minute_field.grid(row=6, column=1, pady=3, ipadx=30)
second_field.grid(row=7, column=1, pady=3, ipadx=30)

# Creating and Packing Submit Button
submit_button = Button(root, text="Start", background="black",
                       foreground="white", command=timer)
submit_button.grid(row=10, column=1, pady=15, ipadx=10)

# Creating Timer Label
timing_text = Label(root, background="black", fg="green",
                    font=("garuda", 20, "bold"))

# Handling Keyboard Input
# ENTER --> "<Return>"
# Just for User Exprience, Not Mandatory
# *event should be passed to handle keyboard event
hour_field.bind("<Return>", func=hour_field.focus_set())
hour_field.bind("<Return>", lambda event: minute_field.focus_set())
minute_field.bind("<Return>", lambda event: second_field.focus_set())
second_field.bind("<Return>", lambda event: submit_button.focus_set())
# Running timer function if <Return> key is pressed
submit_button.bind("<Return>", func=timer)

root.mainloop()

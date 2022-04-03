from tkinter import Tk, Label, Entry, Button
from tkinter.constants import TOP

# UI development
# Customizing root window
root = Tk()
root.geometry("588x433")
root.configure(background="black")
root.title("Youtube Video Downloader")

# Adding header
root_text = Label(root, text="Youtube Video Downloader", background="black",
                  fg="white", font=("ubuntu", 28, "bold"))
root_text.pack(side=TOP, pady=40)

# Intializing Label
name = Label(root, text="Video link", background="black",
             foreground="white", font=("ubuntu", 15))
name.pack()
# Creating Entry Field
name_field = Entry(root, background="black", foreground="white")
name_field.pack(pady=3, ipadx=90)


# Creating Button
submit_button = Button(root, text="Submit", background="black",
                       foreground="green", font=("ubuntu", 10))
submit_button.pack(pady=15)

# Focusing on entry field "Enter" is pressed/"<Return>"
name_field.bind("<Return>", func=name_field.focus_set())


root.mainloop()

# Author: Aashish Sharma
# Github: https://github.com/aasis2520c
# Note pad using tkinter in python

import os
from tkinter.constants import BOTH, END, RIGHT, Y
from tkinter import Menu, Scrollbar, Text, Tk, messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename


class Notepad(Tk):
    """To design GUI based notepad using tkinter"""

    def __init__(self):
        super().__init__()
        self.geometry("744x650")
        self.title("Notepad")
        self.text = None # will be initialized in text_area()
        self.file = None # instance variable to store file path

    def text_area(self):
        """Creates editable text area"""
        self.text = Text(self, undo=True)
        self.text.pack(expand=True, fill=BOTH)
        # Setting scroll bar
        scrollbar = Scrollbar(self.text, command=self.text.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.text.config(yscrollcommand=scrollbar.set)
        self.file = None

    def __new_file(self):
        # create new file and pass title as "Untitled"
        self.title("Untitled-Notepad")
        self.file = None
        self.text.delete(1.0, END)

    def __save_file(self):
        """Saves Opened file"""
        if self.file == None:
            self.file = asksaveasfilename(initialfile="Untitiled.txt", defaultextension=".txt", filetypes=[
                ("All Files", "*.*"), ("Text Documents", "*.txt")])
            if self.file == "":
                self.file = None
            else:
                # Open file as write mode --> add user inputted text --> save it --> change window title as file title
                txt = open(self.file, "w")
                txt.write(self.text.get(1.0, END))
                txt.close()
                self.title(os.path.basename(self.file) + "-Notepad")
        else:
            txt = open(self.file, "w")
            txt.write(self.text.get(1.0, END))
            txt.close()

    def __open_file(self):
        """Opens the save file"""
        self.file = askopenfilename(defaultextension=".txt", filetypes=[
                               ("All Files", "*.*"), ("Text Documents", "*.txt")])
        if self.file == "":
            self.file = None

        else:
            # Open file as read mode --> add file text into editor text area
            self.title(os.path.basename(self.file) + "-Notepad")
            self.text.delete(1.0, END)
            txt = open(self.file, "r")
            self.text.insert(1.0, txt.read())
            txt.close()

    def menu_create(self):
        # Creating main menu
        menu_bar = Menu(self)
        file_menu = Menu(menu_bar, tearoff=0)
        edit_menu = Menu(menu_bar, tearoff=0)
        help_menu = Menu(menu_bar, tearoff=0)

        # adding command to file menu
        file_menu.add_command(label="New", command=self.__new_file)
        file_menu.add_command(label="Open", command=self.__open_file)
        file_menu.add_command(label="Save", command=self.__save_file)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # adding command to edit menu
        edit_menu.add_command(
            label="Cut", command=lambda: self.text.event_generate(("<<Cut>>")))
        edit_menu.add_command(
            label="Copy", command=lambda: self.text.event_generate(("<<Copy>>")))
        edit_menu.add_command(
            label="Paste", command=lambda: self.text.event_generate(("<<Paste>>")))
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        # adding command to help menu
        help_menu.add_command(label="Online Manual", command=lambda: messagebox.showinfo(
            "Online Manual", "Please visit 'https://github.com/aasis2520c'"))
        help_menu.add_command(label="Support us", command=lambda: messagebox.showinfo(
            "Supoort us", "Great! Rate us in Store"))
        help_menu.add_command(label="Report Bug", command=lambda: messagebox.showinfo(
            "Report us", "Please, leave your issue in 'https://github.com/aasis2520c'"))
        help_menu.add_command(label="About", command=lambda: messagebox.showinfo(
            "About us", "Developed and Designed by Aashish <3"))
        menu_bar.add_cascade(label="Help", menu=help_menu)
        menu_bar.add_command(label="Exit", command=self.destroy)
        self.config(menu=menu_bar)


if __name__ == '__main__':
    window = Notepad()
    window.text_area()
    window.menu_create()
    window.mainloop()

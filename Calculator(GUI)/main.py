from tkinter import Button, Entry, Frame, StringVar, Tk
from tkinter.constants import LEFT


class Calculator(Tk):
    """To design GUI based calculator using tkinter"""

    def __init__(self):
        super().__init__()
        self.geometry("344x450")
        self.configure(background="black")
        self.title("Calculator")

    def entry_create(self):
        """Create Entry Field for Input"""
        global entry_value
        entry_value = StringVar()
        global entry_screen
        entry_screen = Entry(
            self,
            foreground="white",
            background="black",
            textvariable=entry_value,
            font=("lucida, 30"),
        )
        entry_screen.pack(fill="x", padx=8, pady=8, ipady=10)

    def __click(self, event):
        """Handling click event"""
        text = event.widget.cget("text")
        if text == "\tC       ":
            entry_value.set("")
            entry_screen.update()
        elif text == " =":
            self.__equal_to()
        else:
            entry_value.set(entry_value.get() + text)

    def __equal_to(self):
        """Handles equal to operation"""
        try:
            if entry_value.get().isdigit():
                value = int(entry_value.get())
            else:
                value = eval(entry_value.get())
                entry_value.set(value)
                entry_screen.update()
        except:
            entry_value.set("Error")
            entry_screen.update()

    def create_button(self):
        """Creates Calculator Buttons"""
        buttons = [
            ["\tC       ", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "+"],
            [" 1", "2", "3", "- "],
            ["0", ".", "%", " ="],
        ]
        for row in buttons:
            frame = Frame(self, background="black")
            frame.pack()
            for button in row:
                button_key = Button(
                    frame,
                    background="black",
                    foreground="white",
                    text=button,
                    font=("ubuntu, 15 bold"),
                )
                button_key.pack(side=LEFT, padx=3, pady=5, ipadx=13, ipady=10)
                button_key.bind("<Button-1>", self.__click)


if __name__ == "__main__":
    window = Calculator()
    window.entry_create()
    window.create_button()
    window.mainloop()

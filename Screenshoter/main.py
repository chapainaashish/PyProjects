
from tkinter import Button, Label, Tk
import numpy as np
import cv2 as cv
import pyautogui


class Screenshot(Tk):
    """Take Screenshot"""

    def __init__(self):
        super().__init__()
        self.geometry("288x233")
        self.configure(background="black")
        self.title("Screenshoter")
        self._time = 5

    def _show_info(self):
        info.config(text=f"Taking Screenshot in {self._time} seconds")
        self._time -= 1
        if self._time >= 0:
            info.after(1000, self._show_info)
        else:
            self._screenshot()
            info.config(
                text="Screenshot Taken \nSaved on Current Working Directory", foreground="green")

    def _screenshot(self):
        image = pyautogui.screenshot()
        converted_image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
        cv.imwrite("screenshot.png", converted_image)

    def create_ui(self):
        """Creates Buttons and Labels"""
        Button(self, text="Capture", background="black", foreground="white",
               font=("ubuntu", 15), command=self._show_info).pack(pady=50)

        global info
        info = Label(self,
                     background="black", foreground="white", font=("ubuntu", 10))
        info.pack()


if __name__ == '__main__':
    screenshot = Screenshot()
    screenshot.create_ui()
    screenshot.mainloop()

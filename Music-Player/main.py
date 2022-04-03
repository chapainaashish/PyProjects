"""
Author: Aashish Sharma
Music Player
Module Used: Tkinter, Pygame
"""

from tkinter import Tk, Label, Button
from tkinter.constants import TOP
from tkinter.filedialog import askopenfile
from pygame import mixer


class MusicPlayer(Tk):
    """Play and Load Music"""

    def __init__(self):
        super().__init__()
        self.geometry("388x433")
        self.configure(background="black")
        self.title("Music Player")
        self.music_file = None

    def __file_open(self):
        """Opens music file from filedialog"""
        self.music_file = askopenfile(
            defaultextension=".mp3", filetypes=[("Music", "*.mp3")])
        mixer.init()
        mixer.music.load(self.music_file)
        mixer.music.play()

    def create_ui(self):
        """Creates User Interface"""
        Label(self, text="Music Player", background="black",
              fg="white", font=("ubuntu", 18, "bold")).pack(side=TOP, pady=40)

        _command = {
            "Load": self.__file_open,
            "Play": lambda: mixer.music.unpause(),
            "Pause": lambda: mixer.music.pause(),
            "Quit": self.destroy
        }

        # Creating Button
        for key, value in _command.items():
            Button(self, text=key, background="black",
                   foreground="white", font=("ubuntu", 10), command=value).pack(pady=10)


if __name__ == '__main__':
    player = MusicPlayer()
    player.create_ui()
    player.mainloop()

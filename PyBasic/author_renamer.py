# This was just automation tool made to add author name at file header

import os

files_path = str(input("Enter the directory files_path: "))
sentences = [
    "# Author: Aashish Chapain\n",
    "# Github: https://github.com/chapainaashish\n",
    "\n",
]

for file in os.listdir(files_path):
    if os.path.splitext(file)[1] == ".py":
        garbage_file = "dummy_file.py"
        with open(files_path + file, "r") as read_object, open(
            files_path + garbage_file, "a"
        ) as write_object:
            for line in sentences:
                write_object.write(line)

            for text in read_object:
                write_object.write(text)

        os.remove(files_path + file)
        os.rename(files_path + garbage_file, files_path + file)

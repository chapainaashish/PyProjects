# rename folder which have space and replace '-'
import os

files_path = str(input("Enter the directory files_path: "))


for folder in os.listdir(files_path):
    new_name = folder.replace(" ", "-")
    os.rename(f"/home/aashish/Documents/Python-Journey/Python-Projects/{folder}",
              f"/home/aashish/Documents/Python-Journey/Python-Projects/{new_name}")

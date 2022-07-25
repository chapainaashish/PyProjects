# rename folder which have space and replace '-'
import os

files_path = str(input("Enter the directory files_path: "))


for folder in os.listdir(files_path):
    new_name = folder.replace(" ", "-")
    os.rename(f"{files_path}/{folder}",
              f"{files_path}/{new_name}")

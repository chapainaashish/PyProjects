import os

files_path ="/home/aashish/Documents/C-Journey/C"

for file in os.listdir(files_path):
    if os.path.splitext(file)[1] == ".cpp":
        new_name = file.replace("cpp", "c")
        os.rename(f"/home/aashish/Documents/C-Journey/C/{file}", f"/home/aashish/Documents/C-Journey/C/{new_name}")

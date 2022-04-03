# Author: Aashish Sharma
# Github: https://github.com/aasis2520c
# Duplicate file remover

def file_renamer(path):
    """Function remove duplicate files"""
    import os
    # files_list = [file for file in os.listdir(path)]
    files_list = []
    for file in os.listdir(path):
        # if files name found in list it will be removed
        if file in files_list:
            os.remove(file)
            print(f"{file} has been removed")
        else:
            files_list.append(file)


if __name__ == '__main__':
    files_path = str(input("Enter the directory path: "))
    file_renamer(files_path)
    print("Done! \nCheck your files...")

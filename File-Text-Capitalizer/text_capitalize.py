# Program to capitalize every first word of sentence of txt file


import os


def bulk_rename(path):
    files = os.listdir(path)
    for user_file in files:
        if os.path.splitext(user_file)[1] == ".txt":
            capitalize_list = []

            # first reading txt line and captializing it and saving sentences in list
            with open(f"{path}{user_file}", "r+") as f:
                j = f.readlines()
                for line in j:
                    capitalize_line = line.capitalize()
                    capitalize_list.append(capitalize_line)

            # resetting txt file so that we can append our capitalize txt file
            with open(f"{path}{user_file}", "w") as f:
                f.write("")

            # writing capitalize sentences into txt file
            with open(f"{path}{user_file}", "a") as f:
                for sentence in capitalize_list:
                    f.write(sentence)


if __name__ == '__main__':
    path = input("Enter the path of txt files: ")
    bulk_rename(path)

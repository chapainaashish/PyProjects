# Program to capitalize every first word of sentence of txt file


import os


def bulk_rename(path, overwrite=True):
    files = os.listdir(path)
    for user_file in files:
        if os.path.splitext(user_file)[1] == ".txt":
            capitalize_list = []

            # first reading txt line and captializing it and saving sentences in list
            user_file_path = os.path.join(path, user_file)
            with open(user_file_path, "r+") as f_in:
                j = f_in.readlines()
                for line in j:
                    capitalize_line = line.capitalize()
                    capitalize_list.append(capitalize_line)
            f_in.close()
            
            if overwrite:
                out_file_path = user_file_path
            else:
                out_file_path = os.path.splitext(user_file)[0] + "_new"+ os.path.splitext(user_file)[1]
            # resetting txt file so that we can append our capitalize txt file
            with open(out_file_path, "w") as f_out:
                f_out.write("")

            # writing capitalize sentences into txt file
            with open(out_file_path, "a") as f_out:
                for sentence in capitalize_list:
                    f_out.write(sentence)


if __name__ == '__main__':
    path = input("Enter the path of txt files: ")
    ow = input("Overwrite existing files? Type Yes")
    bulk_rename(path, ow == "Yes")

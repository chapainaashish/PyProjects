# import os
#
# files_path ="/home/aashish/Documents/C-Journey/C"
#
# for file in os.listdir(files_path):
#     if os.path.splitext(file)[1] == ".cpp":
#         new_name = file.replace("cpp", "c")
#         os.rename(f"/home/aashish/Documents/C-Journey/C/{file}", f"/home/aashish/Documents/C-Journey/C/{new_name}"

`

first_student = 0
second_student = 0
none_student = 0

student_list = [23, 45, 67, 89, 90]

for marks in student_list:

    if marks >= 80:
        first_student = first_student + 1

    if 60 <= marks < 80:
        second_student = second_student + 1

    if marks < 60:
        none_student = none_student + 1


print(f"First division student: {first_student}")
print(f"second division student: {second_student}")
print(f"none division student: {none_student}")






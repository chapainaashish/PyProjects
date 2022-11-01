# Program that randomizes persons last name with another person first name

import random

userwish = int(input("Enter the number of person you want to add: "))
firstname = []
lastname = []

for i in range(userwish):
    name = str(input("Enter your name: ")).split(" ")

    firstname.append(name[0])

    try:
        lastname.append(f"{name[1]} {name[2]}")

    except:
        lastname.append(name[1])


for fname in firstname:
    lname = random.choice(lastname)
    print(f"{fname} {lname}")

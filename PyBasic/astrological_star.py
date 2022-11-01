# Printing astrological star according to user input

star_value = int(input("Input how many star you want to shine: "))
user_order = int(input("Input '0' for ascending and '1' for descending; "))

if user_order == 0:
    for i in range(0, star_value + 1):
        print(i * "*")

elif user_order == 1:
    for i in range(star_value, 0, -1):
        print(i * "*")

else:
    print("Sorry, Check your input!")

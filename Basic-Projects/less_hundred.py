# program to take input as long as user input less than 100

while True:
    user_input = int(input("input the number: "))
    if user_input < 100:
        print('oooopssss......sorry')
        continue
    else:
        print('yo... did it')
        break
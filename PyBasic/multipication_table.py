# Display the multipication table of up to the given number
num = int(input("Enter the number to multiply; "))
for i in range(num, 0, -1):
    for j in range(1, 11):
        print(f"{i} * {j} = {j*i}")

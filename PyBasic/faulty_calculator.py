"""
Faulty Calculator
Calculator which solve all the problems correctly except
the following ones:
45 * 3 = 555, 56+9 = 77, 56/6 = 4

"""

num1 = int(input("Input the first number: "))
num2 = int(input("Input the second number: "))
user_sign = str(input("input the sign: "))

if num1 == 45 and num2 == 3 and user_sign == "*":
    print(555)

elif num1 == 56 and num2 == 9 and user_sign == "+":
    print(77)

elif num1 == 56 and num2 == 6 and user_sign == "/":
    print(4)

elif user_sign == "+":
    print(num1 + num2)


elif user_sign == "-":
    print(num1 - num2)


elif user_sign == "/":
    print(num1 / num2)

else:
    print("Wrong Input!")

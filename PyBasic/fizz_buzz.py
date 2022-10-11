# Fizz buzz  in python
# Programmer: Aashish Sharma


def fizz_buzz(user_input):
    if user_input % 3 == 0 and user_input % 5 == 0:
        return "Fizz Buzz"
    if user_input % 3 == 0:
        return "Fizz"
    if user_input % 5 == 0:
        return "Buzz"

    return user_input


number = int(input("Enter a number: "))
print(fizz_buzz(number))

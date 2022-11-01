# Program to find closest  palindrome of given number


def palindromefunc(total_input):
    """This function can be used to find the greater closest palindrome of given number."""

    for i in range(0, total_input):
        user_length = input("\nEnter the number you want to palindrome: ")
        initial_input = int(user_length)
        user_palindrome = str(user_length)[::-1]

        while int(user_length) != int(user_palindrome):
            user_length = int(user_length) + 1
            user_palindrome = str(user_length)[::-1]
        print(
            f"You have entered {initial_input} as input and closest greater palindrome of this number is {user_palindrome}"
        )


if __name__ == "__main__":
    total_input = int(input("Enter how many numbers you want to palindrome: "))
    palindromefunc(total_input)

"""Program to find prime number or not"""


def find_prime(num):
    """Program to find number prime or not"""
    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"

    return "Prime"


user_input = int(input("Enter a number: "))

print(find_prime(user_input))

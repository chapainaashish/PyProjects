# Author: Aashish Sharma
# Github: https://github.com/aasis2520c

# program to find closest greater and closest smaller palindrome of given number
#         # logic used ---- first increasing user length by 1 then reversing increased length by
#         # converting into string and comparing it. continue;
#         # reversing the number by typecasting it into string [::-1]


class Palindrome:
    """Return the closest greater and smaller  palindrome number of user input."""

    def __init__(self, digit):
        self.digit = digit
        self._greater = self.digit
        self._smaller = self.digit

    def great_palindrome(self):
        greatest_palindrome = str(self._greater)[::-1]
        while int(self._greater) != int(greatest_palindrome):
            self._greater += 1
            greatest_palindrome = str(self._greater)[::-1]
        return greatest_palindrome

    def small_palindrome(self):
        smallest_palindrome = str(self._smaller)[::-1]
        while int(self._smaller) != int(smallest_palindrome):
            self._smaller -= 1
            smallest_palindrome = str(self._smaller)[::-1]
        return smallest_palindrome

    def all_palindrom(self):
        return self.small_palindrome(), self.great_palindrome()

    @property
    def digit(self):
        return self._digit

    # if the digit is negative first we will get 'digit' by using @property decorator
    # then we will check the value using '@digit.setter' by using setter
    @digit.setter
    def digit(self, value):
        if value < 0:
            raise ValueError
        self._digit = value


if __name__ == '__main__':
    try:
        user_digit = int(input("Enter a digit: "))
        palindrome = Palindrome(user_digit)
        print("Closest Smallest Palindrome: " + palindrome.small_palindrome())
        print("Closest Greatest Palindrome: " + palindrome.great_palindrome())
        print(
            f"Closest Smallest & Greatest Palindrome:{palindrome.all_palindrom()}")

    except ValueError:
        print("Enter valid input!")

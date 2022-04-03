# guess the number two player version
import random

def guess_num(player_name, secret_number):
        print(f"\n'{player_name}' Turn")
        user_input = int(input("Guess a number between 0 to 100: "))

        if user_input == secret_number:
            print(f"Congratulation, '{player_name}' won the match.\nThe secret number was '{secret_number}' ")
            exit()

        elif user_input < secret_number:
            print(
                f"'{user_input}' is lower than secret number\t\t")
            return
            
        elif user_input > secret_number:
            print(
                f"'{user_input}' is greater than secret number\t\t")
            return


print("\n--------------Guess The Number Game------------------\n")
player1 = str(input("Enter Player 1 Name: ")).capitalize()
player2 = str(input("Enter Player 2 Name: ")).capitalize()
secretnum = random.randint(1, 100)

user_chance = 9

while user_chance >= 0:
    user_chance = user_chance - 1
    if user_chance % 2 == 0:
        guess_num(player1, secretnum)
        continue

    elif user_chance % 2 == 1:
        guess_num(player2, secretnum)
        continue

print("\nGame Over !!!")
print(f"The secret number was '{secretnum}'")
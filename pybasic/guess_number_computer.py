# guess the number with computer
# Programmer: Aashish Sharma

def guess_number(user_chance, user_difficulty):
    """function to guess a number between 0  to 100"""
    import random
    original_chance = user_chance
    secret_number = random.randint(0, 100)

    while 0 < user_chance:
        user_chance = user_chance - 1
        user_input = int(input("Guess a number between 0 to 100: "))
        if user_chance == 0 and user_input != secret_number:
            print(
                f"Sorry, You lost \nThe secret number was {secret_number}\t\t Difficulty level was {user_difficulty}")
        elif user_input == secret_number:
            print(
                f"Congratulation, You did it in {original_chance - user_chance} attempts \nThe secret number was {secret_number} ")
            break
        elif user_input < secret_number:
            print(
                f"It is lower than secret number\t\t Remaining lifes: {user_chance}\t\t Difficulty level: {user_difficulty}")
            continue
        elif user_input > secret_number:
            print(
                f"It is greater than secret number\t\t Remaining lifes: {user_chance}\t\t Difficulty level: {user_difficulty}")
            continue


try:
    print("WELCOME TO GUESS THE NUMBER GAME")
    user_difficulty = int(input(
        "Please, Choose your difficulty; \n'1' for EASY \n'2' for MEDIUM \n'3' for HARD\n"))
    if user_difficulty == 1:
        user_difficulty = "EASY"
        user_chance = 8
    elif user_difficulty == 2:
        user_difficulty = "MEDIUM"
        user_chance = 5
    elif user_difficulty == 3:
        user_difficulty = "HARD"
        user_chance = 3
    else:
        print("Sorry, Wrong Input")
    guess_number(user_chance, user_difficulty)
except:
    print("SORRY, WRONG INPUT")

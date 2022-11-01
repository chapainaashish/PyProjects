# rock paper scissors
print("WELCOME TO ROCK, PAPER, SCISSOR\n")
chances = 10
user_point = 0
computer_point = 0
while chances > 0:
    import random
    chances = chances - 1
    computer_choice = random.choice(['r', 'p', 's'])
    user_input = input("\nEnter 'r' for rock \nEnter 'p' for paper \nEnter 's' for scissor \nYour input--> ")

    if (user_input == 'r' and computer_choice == 's') or (user_input == 's' and computer_choice == 'p') or (user_input == 'p' and computer_choice == 'r'):
        user_point = user_point + 1
        print(f"\t\t\tCONGRATULATION!.... You won\n\t\t\tYour Point: {user_point} \n\t\t\tComputer Point: {computer_point}\n\t\t\tRemaining chances: {chances}\n")

    elif (user_input == 's' and computer_choice == 'r') or (user_input == 'p' and computer_choice == 's') or (user_input == 'r' and computer_choice == 'p'):
        computer_point = computer_point + 1
        print(f"\t\t\tOOPS!.... You lost\n\t\t\tYour Point: {user_point} \n\t\t\tComputer Point: {computer_point}\n\t\t\tRemaining chances: {chances}\n")

    elif user_input == computer_choice:
        print(f"\t\t\tWHEW!.... Match drawn\n\t\t\tYour Point: {user_point} \n\t\t\tComputer Point: {computer_point}\n\t\t\tRemaining chances: {chances}\n")

    else:
        print("SORRY!.... Wrong input")

if user_point > computer_point:
    print(f"You Won! \nYour total points: {user_point}\nComputer total points: {computer_point}")
    
elif user_point < computer_point:
    print(f"You Lost! \nYour total points: {user_point}\nComputer total points: {computer_point}")

else:
    print(f"Match Drawn! \nYour total points: {user_point}\nComputer total points: {computer_point}")
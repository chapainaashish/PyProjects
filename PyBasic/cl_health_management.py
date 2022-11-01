# Health management system using command line

from datetime import datetime
from pathlib import Path


def time_date():
    return datetime.now()


def health(user_action):
    """health management function"""
    user_file = Path(
        f"dependencies_files/{user_name}_{user_choice}.txt"
    )  # providing path

    # reading user file txt
    if user_action == 0:
        print(user_file.read_text())

    # writing on file txt
    elif user_action == 1:
        user_input = input(f"Enter the {user_choice} you want to add: ")
        user_file.write_text(f"[{time_date()}] - {user_input}\n")
        print(f"You have successfully written {user_input} as {user_choice}")


if __name__ == "__main__":
    user_name = input("Please, Enter your name: ")
    print(f"Welcome to Health Management System '{user_name.capitalize()}'")
    user_choice = input("Enter your activities to access them: ")
    user_action = int(
        input(
            f"Enter '0' to show your {user_choice} and '1' for create your {user_choice}: "
        )
    )
    health(user_action)

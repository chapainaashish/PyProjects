# Calculate your age according the input
user_input = str(input("Enter your age or birth date: "))

# if user input is age
if user_input.isnumeric() and (0 < int(user_input) < 100):

    # finding out user birth date
    user_dob = 2022 - int(user_input)

    # well, basically age limit is 100
    age_limit = user_dob + 100

    print(
        f"You have entered your ages as {user_input}\n\
        Your birth date should be {user_dob}"
    )

    user_action = str(
        input("Enter the year in future or past to calculate your ages: ")
    )

    # finding out user year in user inputted year
    if user_action.isnumeric() and (int(user_dob) < int(user_action) < age_limit):
        user_age = int(user_action) - int(user_dob)
        print(f"Your age should be {user_age} in {user_action}")

    print(
        f'You have entered the wrong date, Your age should be minimum 1 year and maximum 100 years. Error"{user_action}"'
    )


# if user enter birth date
elif user_input.isnumeric() and (1920 < int(user_input) < 2022):

    print(f"You have entered your birth date as {user_input}")
    user_action = str(input("Enter the year to calculate your ages: "))

    age_limit = int(user_input) + 100

    if user_action.isnumeric() and (int(user_input) < int(user_action) <= age_limit):
        user_output = int(user_action) - int(user_input)
        print(f"Your age should be {user_output} in {user_action}")
    else:
        print(
            f'You have entered the wrong date, Your age should be \
            minimum 1 year and maximum 100 years. Error"{user_action}"'
        )

else:
    print("OOPS!... Check your birth certificate")

# countdown timer

def countdown(user_hour, user_min, user_sec):
    """Function for countdown timer"""
    import time
    while True:
        if user_hour == -1:
            print("\nTIME OVER !!!")
            break
        if user_min == -1:
            user_hour = user_hour - 1
            user_min = 59
            continue
        if user_sec== -1:
            user_min = user_min - 1
            user_sec= 59
            continue
        time.sleep(1)
        print(f"REMAINING TIME: {user_hour}:{user_min}:{user_sec}", end = ' \r')
        user_sec= user_sec- 1

user_hour = int(input("Enter the hour---> "))
user_min = int(input(f"Enter the minute---> {user_hour}:"))
user_sec = int(input(f"Enter the second---> {user_hour}:{user_min}:"))

countdown(user_hour, user_min, user_sec)
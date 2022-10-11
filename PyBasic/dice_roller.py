# Dice rolling simulator
# Programmer: Aashish Sharma
import time


def roll_dice():
    import random
    num = random.randint(1, 6)

    if num == 1:
        return "ONE"
    elif num == 2:
        return "TWO"
    elif num == 3:
        return "THREE"
    elif num == 4:
        return "FOUR"
    elif num == 5:
        return "FIVE"
    else:
        return "SIX"


if __name__ == '__main__':
    while True:
        time.sleep(1)
        print(roll_dice())
        continue

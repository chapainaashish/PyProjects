# fake multipication table


def wrongfunc(number):
    import random

    wronglist = []
    wrongmultipier = random.randint(3, 9)
    wrongnumber = random.randint(2, 8)
    for i in range(1, 11):
        if i == wrongmultipier:
            wronglist.append((i * number) + wrongnumber)
        else:
            wronglist.append(number * i)
    return wronglist


def iscorrect(number):
    rightlist = []
    for i in range(1, 11):
        rightlist.append(number * i)
    return rightlist


number = 6
wronglist = wrongfunc(number)
rightlist = iscorrect(number)
print(wronglist)
print(rightlist)

i = -1
while i <= 8:
    i += 1
    if wronglist[i] == rightlist[i]:
        pass
    else:
        print(f"error at {wronglist[i]} in index {i}")
        print(f"Right multipication is {rightlist[i]}")

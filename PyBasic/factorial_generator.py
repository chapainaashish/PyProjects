# Pogram using generator to find factorial number of given number
# Programmer: Aashish Sharma


def recur(n):
    a = 1
    for i in range(n):
        a = a * (i + 1)
        yield a


number = int(input("Enter the number: "))
l = recur(number)
l.__next__()
l.__next__()
l.__next__()

print("factorial of number is")
print(l.__next__())

# Program to input integer in list and print the sum of even number in the list
# Programmer: Aashish Sharma

list_length = int(input('Enter the length of list; '))
number_list = []
for i in range(list_length):
    lstelement = int(input("Enter a number; "))
    number_list.append(lstelement)

totalsum = 0
for element in number_list:
    if element % 2 == 0:
        totalsum = totalsum + element

print(totalsum)

# program to display integer which is less than 6 from list

list1 = ["aasis", 5, 8, 10, 2, 56, 7]

for item in list1:
    if str(item).isnumeric() and item < 6:
        print(item)

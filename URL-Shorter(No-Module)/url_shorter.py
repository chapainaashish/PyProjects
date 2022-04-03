# Author: Aashish Sharma
# Github: https://github.com/aasis2520c

# program to shorten given url and print it domain name

"""
url-sample--
https://www.youtube.com/watch?v=aqvDTCpNRek&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME

"""

# taking input from the user
urlinput = str(input("Enter the URL, Please: "))

if "http" in urlinput:            # if there is full url like 'https://www.youtube.com/watch?v'
    slash = 0                                       # intializing 'slash' to count it
    print("Shorten URL;")
    for element in urlinput:
        if element == "/":
            slash = slash + 1
            if slash == 3:
                break
            else:
                print(element, end="")
                continue
        else:
            print(element, end="")
            continue
    print("\n")

# if there is direct url like 'www.youtube.com/dfie/dfo'
elif "www" in urlinput:
    print("Shorten URL;")
    for element in urlinput:
        if element == "/":
            break
        else:
            print(element, end="")
            continue
    print("\n")

else:
    print("Please, Enter valid URL...")

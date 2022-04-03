# Updating number with their spelling in given sentence
# Programmer: Aashish Sharma

dict1 = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}

codedmsg = str(input("Enter the sentence: "))

for char in codedmsg:
    if char in dict1.keys():
        codedmsg = codedmsg.replace(char, dict1[char])
    else:
        continue
print(f"The modified sentence is: {codedmsg}")

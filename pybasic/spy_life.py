# the spy life
# first reverse it and only accept alphabet and whitespace

codedmsg = str(input("Enter the coded message: "))[::-1]
print(codedmsg)
decodemsg = ""
for char in codedmsg:
    if char.isspace() or char.isalpha():
        decodemsg = decodemsg + char
    else:
        continue

print(f"The decoded message is: {decodemsg}")



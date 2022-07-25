# program to find most repeated character in the given sentence
from pprint import pprint

sentence = str(input("Enter the sentence: ")).replace(" ", "")

max_dict = {}
for char in sentence:
    char_len = sentence.count(char)
    max_dict[char] = char_len

sorted_dict = dict(sorted(max_dict.items(), key=lambda item: item[1]))

for value in sorted_dict.items():
    pass

print(f"The most repaeated character is {value}")

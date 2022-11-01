# program to print the most lengthy word from sentence

input_list = str(input("Enter a sentence: ")).split(" ")

word_name = [word for word in input_list]
word_length = [len(word_len) for word_len in input_list]

combined_list = list(zip(word_length, word_name))

# sorting list first and printing first element of list
print(f"Lengthy word in the sentence is '{sorted(combined_list, reverse=True)[0][1]}'")

password = "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"

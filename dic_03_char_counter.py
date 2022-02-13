# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}
word_count_2 = {}
# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

# Your code goes here ...
for character in text.casefold():
    if character.isalnum():
        word_count[character] = word_count.setdefault(character, 0) + 1
    else:
        pass


for character in text.casefold():
    if character.isalnum():
        if character in word_count_2:
            word_count_2[character] += 1
        else:
            word_count_2[character] = 1
    else:
        pass


# Printing the dictionary
print()
for letter, count in sorted(word_count.items()):
    print(letter, count)

print()
for letter, count in sorted(word_count_2.items()):
    print(letter, count)
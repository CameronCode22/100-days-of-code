import random

# TODO1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
    'u', 'v', 'w', 'x', 'y', 'z'
]

# List of 10 random words
words_list = ['flub', 'zink', 'vopra', 'blanx', 'curil', 'jomed', 'spren', 'wilty', 'drost', 'gaxen']

chosen_word = words_list[random.randint(0, 9)]

print(chosen_word)
import random

# TODO1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
    'u', 'v', 'w', 'x', 'y', 'z'
]

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# List of 10 random words
words_list = ['flub', 'zink', 'vopra', 'blanx', 'curil', 'jomed', 'spren', 'wilty', 'drost', 'gaxen']

chosen_word = words_list[random.randint(0, 9)]

print(chosen_word)

blank_word = []
for i in range(0, len(chosen_word)):
    blank_word.append("_")
print(' '.join(blank_word))
print(blank_word)


completed_flag = False
failed_flag = False
num_guess = 0

while not completed_flag and not failed_flag:

    letter = input("Guess a letter: ").lower()
    correct_guess = False

    # Check if the guessed letter is in the chosen_word
    for i in range(len(chosen_word)):
        if letter == chosen_word[i]:
            print("Correct Guess")
            blank_word[i] = letter
            print(' '.join(blank_word))
            correct_guess = True

    # Check if the word is fully guessed
    if ''.join(blank_word) == chosen_word:
        completed_flag = True

    # Handle wrong guess
    if not correct_guess:
        num_guess += 1
        print(f"Wrong guess. Number of wrong guesses: {num_guess}")
        if num_guess == len(HANGMANPICS):
            failed_flag = True

    #Print hangman_art
    print(HANGMANPICS[num_guess - 1] if num_guess > 0 else HANGMANPICS[0])

# Game end
if completed_flag:
    print("You won! Congratulations!")
elif failed_flag:
    print("You lost! The word was:", chosen_word)



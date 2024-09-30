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

blank_word = []
for i in range(0, len(chosen_word)):
    blank_word.append("_")
print(' '.join(blank_word))
print(blank_word)


# TODO2 - Ask the user to guess a letter and assign their answer to a variable called guess, make guess lowercase
completed_flag = False
failed_flag = False
num_guess = 0
while not completed_flag:

    letter = input("guess a letter").lower()

    # TODO3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is, "Wrong" if it's not

    for i in range(0,len(chosen_word)):
        if letter == chosen_word[i]:
            print("Correct Guess")
            blank_word[i] = letter
            #update blank word
            print(' '.join(blank_word))
            joined_blank = str(''.join(blank_word))
            print(joined_blank)
            num_guess += 1
            print(num_guess)
            if chosen_word == joined_blank:
                completed_flag = True
            elif num_guess == 10:
                failed_flag = True
                
            
            break
    if completed_flag == True:
        print("You won! congratulations")
    elif failed_flag == True:
        print("You lost! Try again!")


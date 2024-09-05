import random
import day4.ascii_art as ascii_art

#rock = 0
#paper = 1
#scissors = 2

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors"))
computer_choice = random.randint(0, 2)

# print the computer choice
print("Computer Choice: ")
if computer_choice == 0:
    ascii_art.print_rock()
elif computer_choice == 1:
    ascii_art.print_paper()
elif computer_choice == 2:
    ascii_art.print_scissors()

#print user choice
print("Your choice")
if user_choice == 0:
    ascii_art.print_rock()
elif user_choice == 1:
    ascii_art.print_paper()
elif user_choice == 2:
    ascii_art.print_scissors()


if user_choice == computer_choice:
    print("Draw, try again")
elif user_choice == 0:
    if computer_choice == 2:
        print("you won!")
    else:
        print("You lost!, try again!")
elif user_choice == 1:
    if computer_choice == 0:
        print("You won!")
    else:
        print("You lost!")
elif user_choice == 2:
    if computer_choice == 1:
        print("You won!")
    else:
        print("You lost!")



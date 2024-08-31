print("Welcome to Treasure island. Your mission is to find the treasure.")

direction = input("Would you like to go left 'L' or right 'R'").lower()
    
if direction == "l":
    question_2 = input("Swim or wait?").lower()
    if question_2 == "wait":
        question_3 = input("which door: Red, Yellow, Blue").lower()
        if question_3 == "yellow":
            print("you Win!")
        elif question_3 == "red":
            print("Burned by fire. Game Over")
        elif question_3 == "blue":
            print("Eaten by beasts. Game Over")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game over")
else:
    print("Fall into hole. Game Over.")
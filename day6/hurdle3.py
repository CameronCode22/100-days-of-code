def jump():
    for i in range(1, 4):
        turn_left()
    move()
    for i in range(1, 4):
        turn_left()
       
    
def find_max():
    turn_left()
    while wall_on_right():
        if wall_in_front():
            turn_left()
        elif at_goal():
            break
        else:
            move()
    


while not at_goal():
        while front_is_clear():
            if at_goal():
                break
            else:
                move()

        while wall_in_front():
                find_max()
                if at_goal():
                    break
                else:
                    jump()
        
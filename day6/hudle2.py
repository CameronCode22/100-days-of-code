def jump():
    turn_left()
    move()
    for i in range(3):
        turn_left()
    move()
    for i in range(3):
        turn_left()
    move ()
    turn_left()


while not at_goal():
    while front_is_clear():
        move()

    while wall_in_front():
        jump()
        










        
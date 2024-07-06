from logic import Game

start = Game()
mat = start.start_game()
mat = start.add_new_2(mat)


a = ''' Movement key
        W or w - for up
        A or a - for left
        S or s - for down
        D or d - for right \n >>'''


game_over = False
while game_over == False:
    mat = start.add_new_2(mat)
    start.get_current_state(mat)
    game_over = start.is_game_over(mat)
    if game_over == True:
        print(' Game over ')
        break
    user_input = str(input(a))
    print('input user',user_input)
    
    if user_input == "W" or user_input == "w":
        print(" i am up ")
        mat = start.up(mat)
        
    if user_input == "S" or user_input == "s":
        print(" i am down ")
        mat = start.down(mat)

    if user_input == "A" or user_input == "a":
        print(" i am left ")
        mat = start.left(mat)
        
    if user_input == "D" or user_input == "d":
        print(" i am rught ")
        mat = start.right(mat)


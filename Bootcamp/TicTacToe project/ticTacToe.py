import os
import random

def clear():
    os.system('cls')
# Step 1: Write a function that can print out a board. Set up your board as a list, 
# where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
def display_board(board):
    clear()
    print('   |   |')
    print(' ' + board[1]+' | '+board[2]+' | '+board[3])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[4]+' | '+board[5]+' | '+board[6])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |')

# test_board = [' ']*10

# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'.
#  Think about using while loops to co
# ntinually ask until you get a correct answer.
def player_input():
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    marker = ' '
    #KEEP ASKING PLAYER 1 TO CHOOSE X or O
    while marker != 'X' and marker != 'O':
        marker = input('PLAYER 1, choose X or O:  ').upper()    
    # ASSIGN PLAYER 2 THE OPOSSITE MARKER
    player1 = marker
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
# here we are using tupling packing and assign 'X' or 'O' to player 1 and 2
# player1_marker , player2_marker = player_input()
# print(player1_marker)
# print(player2_marker)

# -------------------------------------------------------------------------------
# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'),
#  and a desired position (number 1-9) and assigns it to the board.
def place_marker(board,marker,position):
    board[position] = marker

# TEST Step 3: run the place marker function using test parameters and display the modified board
# place_marker(test_board,'X',2)
# place_marker(test_board,'X',5)
# place_marker(test_board,'X',8)
# display_board(test_board)

# Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
def win_check(board, mark):
    # win tic tac toe?
    #first check all rows, and check if they all share the same marker?
    win = ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
    #second, columns check, if they all share the same marker?
            (board[3] == board[6] == board[9] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[1] == board[4] == board[7] == mark) or
    #third, we have 2 diagonals to check if they share the same marker.
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))
    return win
# TEST Step 4: run the win_check function against our test_board - it should return True
# print(win_check(test_board,'O'))

# Step 5: Write a function that uses the random module to randomly decide which player goes first.
# You may want to lookup random.randint() Return a string of which player went first.
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.
def space_check(board,position):
    return board[position] == ' '

# Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    # BOARD IS FULL IF WE RETURN FULL
    return True

# Step 8: Write a function that asks for a player's next position (as a number 1-9)
# and then uses the function from step 6 to check if it's a free position. If it is,
# then return the position for later use.
def player_choice(board):
    position = 0
    
    while position not in range(1,10) or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))
    return position

# Step 9: Write a function that asks the player if they want to play again
# and returns a boolean True if they do want to play again.

def replay():
    return input("Play again? enter YES or NO: ").lower().startswith('y')

# Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!
print('Welcome to TIC TAC TOE!')
# WHILE LOOP TP KEEP THE GAME RUNNING
while True:
    # PLAY THE GAME

    ## SET EVEYTHING UP (BOARD, WHOS FIRST, CHOOSE MARKERS)
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Ready to Play? yes or no? ')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    ## GAME PLAY
    while game_on:
        if turn == 'Player 1':
        ###PLAYER 1 TURN 
            #show the board

            display_board(the_board)
            # choose a position
            print('player1 turn')
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board,player1_marker,position)
            # check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON')
                game_on = False
            # Or check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("THE WITCH HAS WON")
                    game_on = False
                else:
                    # no tie no win? then next player's turn
                    turn = 'Player 2'
        else:
            ###PLAYER 2 TURN
            #show the board
            display_board(the_board)
            # choose a position
            print('player 2')
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board,player2_marker,position)
            # check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON')
                game_on = False
            # Or check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("THE WITCH HAS WON")
                    game_on = False
                else:
                    # no tie no win? then next player's turn
                    turn = 'Player 1'
        

    if not replay():
        break
    # BREAK OUT OF THE WHILE LOOP ON replay()




from random import randint # import random values from random

board=[]

for x in range(5): # prints board
    board.append(["0"]*5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let the game begin"
print_board(board)

def random_row(board): #random row
    return randint(0, len(board) -1)

def random_col(board): #random col
    return randint(0,len(board[0]) -1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col


for turn in range(4): # loop for tracking turns
    guess_row = int(raw_input("Guess row"))
    guess_col = int(raw_input("Guess col"))
    print "turn", turn + 1
    if guess_row == ship_row and guess_col == ship_col: # loop for guessing battleship
        print "Congratulations! You sank my battleship"
        break
    else:
        if (guess_row < 0 or guess_row >4) or (guess_col >4):
            print "Oops, thats not even in the ocean"
        elif (board[guess_row][guess_col] == "X"):
            print "You guessed that already"
        else:
            print "you missed my battleship"
            board[guess_row][guess_col] = "X"
            if turn == 3:
                print "game over"

            print_board(board)
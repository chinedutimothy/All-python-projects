import random 

possible_numbers = [1,2,3,4,5,6,7,8,9]
board = [[1,2,3], [4,5,6], [7,8,9]]
rows = 3
cols = 3

def print_game_board():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(cols):
            print("", board[x][y], end= " |")
    print("\n+---+---+---+")


def gamecheck():
    if (board[1] == board[2] and board[2]== board[3]) or (board[4] == board[5] and board[5]== board[6])\
        or (board[7] == board[8] and board[8]== board[9]) or (board[1] == board[4] and board[4]== board[7])\
        or (board[1] == board[5] and board[5]== board[9]) or (board[2] == board[5] and board[5]== board[8])\
        or (board[3] == board[6] and board[6]== board[9]) or (board[3] == board[5] and board[7]== board[3]):
        print ("human wins")
    else: 
        print("draw")
    
    
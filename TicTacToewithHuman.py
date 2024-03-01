#TicTacToe with 2 players
#using def

import time #Time module for a slight delay in both players input

#1.) print the board 
print("Welcome to TicTacToe")
board = [str(i) for i in range(1, 10)]

def printBoard(board):
    for i in range(0, len(board), 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("-" * 9)

#2.) check for wins

def checkWin(board):
    winning_combination = [
        [0,1,2], [3,4,5], [6,7,8], #for rows
        [0,3,6], [1,4,7], [2,5,8], #for cols
        [0,4,8], [2,4,6] #for diagonals
                      ]
    
    for combo in winning_combination:
        if all(board[pos] == 'X' for pos in combo):
            return "Player1 wins"
        elif all(board[pos] == 'O' for pos in combo):
            return "Player2 wins"
    if all(pos in ['X', 'O'] for pos in board):
        return "It's a Tie"
    return "Game is still Running"


#3.) Collecting users input

def usersInput(board):
    playersMoves = []

    while True:
        print("\n Available Numbers")
        printBoard(board)

        time.sleep(0.5)

        players = input("Player1; Select from the following numbers: ")

        try:
            playersInput = int(players)
            if playersInput < 1 or playersInput > 9 or board[playersInput - 1] in ['X', 'O']:
                print("Invalid Selection, Select from the following available numbers")
                continue
            board[playersInput - 1] = 'X'
            playersMoves.append(playersInput)
            
            #Check for the result 
            result = checkWin(board)
            if result != "Game is still Running":
                printBoard(board)
                print(result)

        except ValueError:
            print("Invalid entry")

        #Check if the game is over after player move
        if result != "Game is still Running":
            break

        print("\n Available numbers")
        printBoard(board)

        while True:
            
            time.sleep(0.5)
            players = input("PLayer2; Select from the following numbers: ")
            try:
                playersInput = int(players)
                if playersInput < 1 or playersInput > 9 or board[playersInput - 1] in ['X', 'O']:
                    print("Invalid Selection, Select from the following available numbers")
                    printBoard(board)
                    continue
                board[playersInput - 1] = 'O'
                break
            except ValueError:
                print("Invalid entry")

            result = checkWin(board)

            if result != "Game is still Running":
                printBoard(board)
                print(result)
                break

usersInput(board)

            


#Creating a TicTacToe with AI
import random #random module for the ai's selection
import time #time module for a delay in the ai's selection

#1.) we print the board
board = [str(i) for i in range(1,10)]

#board = [1,2,3,4,5,6,7,8,9]

def printBoard(board):
    for i in range(0, len(board), 3):
        print(" | ".join(map(str, board[i:i+3])))
        if i<6:
            print("-" * 9)



#2.) Check for wins
            
def Checkwin(board):
    winning_combination = [
        [0,1,2], [3,4,5], [6,7,8], #for rows
        [0,3,6], [1,4,7], [2,5,8], #for cols
        [0,4,8], [2,4,6] #for diagonals
    ]

    for combo in winning_combination:
        if all(board[pos] == 'X' for pos in combo): #for board positions in X in the combo makes the player a winner
            return "Player wins"
        elif all(board[pos] == 'O' for pos in combo): #for board position in O in the combo makes AI the winner
            return "AI wins"
    if all(pos in 'X' and 'O' for pos in board): #if the board is filled with  X and O wihout a combination then it is a tie
        return "It's a Tie"
    return "Game is still running" #or else the game is still running

#3.) player's input

def userInput(board):
   playerMoves = []
   aiMoves = []

   while True:
       print("\nAvailable Numbers") 
       printBoard(board)

       player = input("Select from the following available number: ")

       try:
           playerInput = int(player)
           if playerInput < 1 or playerInput > 9 or board[playerInput - 1] in ['X', 'O']:
               print("Invalid selection")
               continue
           board[playerInput - 1] = 'X'
           playerMoves.append(playerInput)
       except ValueError:
           print("Invalid entry")
           continue

       result = Checkwin(board)
       if result != "Game is still running":
           printBoard(board)
           print(result)
           break
       
       ai = random.randint(1, 9)
       time.sleep(2)
       while board[ai - 1] in ['X', 'O']:
           ai = random.randint(1, 9)
           time.sleep(2)
       board[ai - 1] = 'O'    
       aiMoves.append(ai)

       result = Checkwin(board)
       if result != "Game is still running":
           printBoard(board)
           print(result)
           break
       

userInput(board)

       
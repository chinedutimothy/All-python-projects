import time

board = [str(i) for i in range (1, 10)]

def printBoard(board):
    for i in range(0, len(board), 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("-" * 9)

def checkWin(board):
    winning_combination = [
        [0,1,2], [3,4,5], [6,7,8], #for rows
        [0,3,6], [1,4,7], [2,5,8], #for cols
        [0,4,8], [2,4,6] #for diagonals
    ]
    for combo in winning_combination:
        if all(board[pos] == 'X' for pos in combo): #for board positions in X in the combo makes the player a winner
            return "Player 1 wins"
        elif all(board[pos] == 'O' for pos in combo): #for board position in O in the combo makes Player 2 (or AI) the winner
            return "Player 2 (or AI) wins"
    if all(pos in ['X', 'O'] for pos in board): #if the board is filled with X and O without a combination then it is a tie
        return "It's a Tie"
    return "Game is still running" #or else the game is still running

def userInput(board):
    playerMoves = []

    while True:
        print("\nAvailable Numbers") 
        printBoard(board)

        time.sleep(1)

        player = input("Player 1, select from the following available number: ")

        try:
            playerInput = int(player)
            if playerInput < 1 or playerInput > 9 or board[playerInput - 1] in ['X', 'O']:
                print("Invalid selection")
                continue
            board[playerInput - 1] = 'X'
            playerMoves.append(playerInput)

            result = checkWin(board)
            if result != "Game is still running":
                printBoard(board)
                print(result)
                break
        except ValueError:
            print("Invalid entry")

        # Check if the game has ended after Player 1's move
        if result != "Game is still running":
            break

        print("\nAvailable Numbers") 
        printBoard(board)

        while True:
            time.sleep(1)
            player = input("Player 2, select from the following available number: ")

            try:
                playerInput = int(player)
                if playerInput < 1 or playerInput > 9 or board[playerInput - 1] in ['X', 'O']:
                    print("Invalid selection")
                    continue
                board[playerInput - 1] = 'O'
                break
            except ValueError:
                print("Invalid entry")

            result = checkWin(board)
            if result != "Game is still running":
                printBoard(board)
                print(result)
                break

userInput(board)

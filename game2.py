import random
import time

Total_Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Print the board
def printBoard(board):
    for i in range(0, len(board), 3):
        print(" ".join(map(str, board[i:i+3])))

# Print the available numbers on board
def printAvailableNumbers(board):
    print("Available Numbers")
    printBoard(board)

# Determine the winner
def checkWin(player1_move, player2_move):
    winning_combinations = [
          [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [3, 5, 7]              # Diagonals
    ]
    
    for combo in winning_combinations:
        if all(num in player1_move for num in combo):
            return "Player1 wins"
        elif all(num in player2_move for num in combo):
            return "Player2 wins"

    if len(player1_move) + len(player2_move) == 9:
        return "It's a Tie"

    return "Game still running"

# Users input
def usersinput(Total_Numbers):
    player1_move = []
    player2_move = []

    while Total_Numbers:
        printAvailableNumbers(Total_Numbers)

        player1_input = input("Player1: Select a number from the available numbers: ")
        try:
            player1_input = int(player1_input)
            if player1_input not in Total_Numbers:
                print("Invalid entry. Please select from the available numbers.")
                continue
            else:
                player1_move.append(player1_input)
                Total_Numbers.remove(player1_input)

                result = checkWin(player1_move, player2_move)
                print(result)

                if result != "Game still running":
                    break

            if not Total_Numbers:
                print("It's a tie!")
                break

            printAvailableNumbers(Total_Numbers)

            player2_input = input("Player2: Select a number from the available numbers: ")
            try:
                player2_input = int(player2_input)
                if player2_input not in Total_Numbers:
                    print("Invalid entry. Please select from the available numbers.")
                    continue
                else:
                    player2_move.append(player2_input)
                    Total_Numbers.remove(player2_input)

                    result = checkWin(player1_move, player2_move)
                    print(result)

                    if result != "Game still running":
                        break

            except ValueError:
                print("Invalid entry. Please enter a number.")

        except ValueError:
            print("Invalid entry. Please enter a number.")

    print("Game over!")

# Run the game
usersinput(Total_Numbers)

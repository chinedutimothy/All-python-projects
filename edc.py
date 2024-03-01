import random
import time

# Function to print the board
def printBoard(board):
    for i in range(0, len(board), 3):
        print(" ".join(map(str, board[i:i+3])))

# Function to print available numbers
def printAvailablenumbers(possible_numbers):
    print("Available Numbers:")
    for i in range(0, len(possible_numbers), 3):
        print(" ".join(map(str, possible_numbers[i:i+3])))

# Function to check for win, tie, or continue game
def checkWin(player_moves, ai_moves):
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [3, 5, 7]              # Diagonals
    ]
    for combo in winning_combinations:
        if all(winnings in player_moves for winnings in combo):
            return "Player wins!"
        elif all(winnings in ai_moves for winnings in combo):
            return "AI wins!"
    if len(player_moves) + len(ai_moves) == 9:
        return "It's a tie!"
    return "Game still running"        

# Function for user input
def user_input():
    player_moves = []
    ai_moves = []
    while possible_numbers:
        printBoard(possible_numbers)
        player = input("Enter a number from the available numbers: ")

        try:
            player_input = int(player)
            if player_input not in possible_numbers:
                print("Invalid number. Please select from the available numbers")
            else:
                player_moves.append(player_input)
                possible_numbers.remove(player_input)

                # AI's move
                ai = random.choice(possible_numbers)
                print("AI is selecting...")
                time.sleep(1)
                print(f"AI selected {ai}")
                ai_moves.append(ai)
                possible_numbers.remove(ai)
                
                # Check for win, tie, or continue game
                result = checkWin(player_moves, ai_moves)
                print(result)
                
                # Break the loop if game is over
                if result != "Game still running":
                    break
                    
        except ValueError:
            print("Invalid entry")

# List of possible numbers
possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Call the user input function
user_input()

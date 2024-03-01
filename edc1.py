import random
import time

def print_board(board):
    for i in range(0, len(board), 3):
        print(" ".join(map(str, board[i:i+3])))

def print_available_numbers(possible_numbers):
    print("Available Numbers")
    print_board(possible_numbers)

def check_win(player_moves, ai_moves):
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [3, 5, 7]              # Diagonals
    ]
    for combo in winning_combinations:
        if all(num in player_moves for num in combo):
            return "Player wins!"
        elif all(num in ai_moves for num in combo):
            return "AI wins!"
    if len(player_moves) + len(ai_moves) == 9:
        return "It's a tie!"
    return "Game still running"

def user_input(possible_numbers):
    player_moves = []
    ai_moves = []
    print_available_numbers(possible_numbers)
    while possible_numbers:
        player = input("Enter a number from the available numbers: ")

        try:
            player_input = int(player)
            if player_input not in possible_numbers:
                print("Invalid number. Please select from the available numbers")
                continue
            player_moves.append(player_input)
            possible_numbers.remove(player_input)
        except ValueError:
            print("Invalid entry")
            continue

        if not possible_numbers:
            print("It's a tie")
            break 

        ai = random.choice(possible_numbers)
        print("AI is selecting...")
        time.sleep(1)
        print(f"AI selected {ai}")
        ai_moves.append(ai)
        possible_numbers.remove(ai)
        print_available_numbers(possible_numbers)

        result = check_win(player_moves, ai_moves)
        if result != "Game still running":
            print(result)
            break

possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
user_input(possible_numbers)

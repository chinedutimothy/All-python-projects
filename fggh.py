import random
import time

possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Print the board in a 3 by 3 matrix
def printBoard(possible_numbers):
    for i in range(0, len(possible_numbers), 3):
        print(" ".join(map(str, possible_numbers[i:i+3])))

# Print available numbers
def printAvailableNumbers(possible_numbers):
    print("Available Numbers")
    printBoard(possible_numbers)

# User input function
def user_input(possible_numbers):
    print("Available numbers")
    printBoard(possible_numbers)
    while possible_numbers:
        player = input(f"Enter a number from the available numbers: ")

        try:
            player_input = int(player)
            if player_input not in possible_numbers:
                print("Invalid number. Please select from the available numbers.")
            else:
                possible_numbers.remove(player_input)
                result = Checkwin(possible_numbers)
                print(result)
                if result != 'Game still running':
                    break
                ai = random.choice(possible_numbers)
                print("AI is selecting...")
                time.sleep(1)
                print(f"AI selected {ai}")
                possible_numbers.remove(ai)
                printAvailableNumbers(possible_numbers)

        except ValueError:
            print("Invalid entry. Please enter a valid number.")

# Check for win or game still running
def Checkwin(possible_numbers):
    # Check rows
    for i in range(0, len(possible_numbers), 3):
        print(f"Checking row starting at index {i}")
        print(f"Indices: {i}, {i+1}, {i+2}")
        print(f"Board values: {possible_numbers[i]}, {possible_numbers[i+1]}, {possible_numbers[i+2]}")
        if possible_numbers[i] == possible_numbers[i+1] == possible_numbers[i+2]:
            return f'Player {possible_numbers[i]} wins!'

    # Check columns
    for i in range(3):
        if possible_numbers[i] == possible_numbers[i+3] == possible_numbers[i+6]:
            return f'Player {possible_numbers[i]} wins!'

    # Check diagonals
    if possible_numbers[0] == possible_numbers[4] == possible_numbers[8]:
        return f'Player {possible_numbers[0]} wins!'
    elif possible_numbers[2] == possible_numbers[4] == possible_numbers[6]:
        return f'Player {possible_numbers[2]} wins!'

    # Check for tie
    if all(isinstance(num, int) for num in possible_numbers):
        return "It's a tie!"

    return 'Game still running'

user_input(possible_numbers)

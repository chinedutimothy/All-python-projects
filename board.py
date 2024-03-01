class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # 3by3 board 
        self.currentwinner = None  #keep track of winner

    def printboard(self):
        for row in [self.board[j*3:(j+1)*3] for j   in range(3)]:

        def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)



        import random
"""
possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while possible_numbers:
    player_input = input("Enter a number from 1 to 9: ")

    try:
        player_number = int(player_input)
    except ValueError:
        print("Please enter a valid number.")
        continue

    if player_number not in possible_numbers:
        print("Invalid number or number already chosen. Please try again.")
        continue

    possible_numbers.remove(player_number)
    print("Remaining numbers:", possible_numbers)

    if not possible_numbers:
        print("No more numbers left. It's a draw!")
        break

    ai_number = random.choice(possible_numbers)
    possible_numbers.remove(ai_number)
    print("AI selected:", ai_number)
    print("Remaining numbers:", possible_numbers)
    """
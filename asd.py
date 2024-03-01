print("Welcome to TicTacToe")

possible_numbers = [1,2,3,4,5,6,7,8,9]
current_game = True
starting_letter = "x"

#Welcome to TicTacToe
#guidelines 
#number of total games depending on player's input

#Print the board
def printBoard(possible_numbers):
    print(possible_numbers)
    
   
printBoard(possible_numbers)
#Collect Player's input 
def playerinput(possible_numbers):
    while True:
         player = input("Select numbers from 1-9")

playerinput(possible_numbers)


#Check for win and tie
def checkwin(possible_numbers):
    
    
#Switch Player 
#Check for win and tie
#Print the winner
#replay
#count scores
#Print the overall winner
   
        break

    ai_number = random.choice(possible_numbers)
    possible_numbers.remove(ai_number)
    print("AI selected:", ai_number)
    print("Remaining numbers:", possible_numbers)
 
    if not possible_numbers:
        print("No more numbers left. It's a draw!")

import random 

#Today's session we're creating a rock, paper, scissors game 

def you_play():
    player1 = input("Please input 'r' for rock, 's' for scissors and ''p' for paper")
    player2 = input("Please input 'r' for rock, 's' for scissors and ''p' for paper")


    if player1 == player2:
        return "It is a tie"
    if who_wins(player1, player2):
        return "Player1 wins"
    return "Player2 wins"    

#'r' beats 's' , 's' beats 'p' and 'p' beats 'r'
    

def who_wins(player1, player2):
    if (player1 == 'r' and player2 == 's') or (player1 == 's' and player2 == 'p')\
    or (player1 == 'p' and player2 == 'r'):
        return True
    


print(you_play())

#improvements would be on the scores count in the code 
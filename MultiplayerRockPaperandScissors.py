#Rock, Paper , Scissors using while loop
#Its a multi player game
#here is the link to the single player game
#https://github.com/chinedutimothy/All-python-projects/blob/main/SiingleplayerRockPaperandScisors.py


count = int(0)
player1point = 0
player2point = 0  
limit= int(input("Number of games to played"))



while limit > count:
    player1 = input("Select 'r' for rock, 's' for scissors and 'p' for paper")
    player2 = input("Select 'r' for rock, 's' for scissors and 'p' for paper")
    count += int(1)
   
      
    
 
    if (player1 == 'r' and player2 == 's') or (player1 == 's' and player2 == 'p')\
        or (player1 == 'p' and player2 == 'r'):
        print("Player 1 wins ")
        player1point += 1
    elif player1 == player2:
        print ("It's a tie")
    else:
        print("Player2 wins")
        player2point += 1

    

if player1point > player2point:   
    print(f"Player 1 wins this round with a score of {player1point} while Player2 got a score of {player2point}") 
elif player1point == player2point:
    print (f"It is a tie with a score of {player1point} and {player2point}")
else:
   print(f"Player 2 wins this round with a score of {player2point} while Player1 got a score of {player1point}") 
   
   
    


count = 0
player1point = 0
player2point = 0  
limit = 5

while limit > count:
    player1 = input("Select 'r' for rock, 's' for scissors and 'p' for paper")
    player2 = input("Select 'r' for rock, 's' for scissors and 'p' for paper")
    count +=1
   
      
    
    if player1 == player2:
        print("It is a tie")
    elif (player1 == 'r' and player2 == 's') or (player1 == 's' and player2 == 'p')\
        or (player1 == 'p' and player2 == 'r'):
        print("Player 1 wins ")
        player1point += 1
    else:
        print("Player2 wins")
        player2point += 1

        
    print(player1point)
    print(player2point)

   
   
    
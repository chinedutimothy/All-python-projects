#Rock, Paper , Scissors using while loop
#Its a single player game
#here is the link to the Multi player game 
#https://github.com/chinedutimothy/All-python-projects/blob/main/MultiplayerRockPaperandScissors.py

import random


count = int(0)
userpoint = 0
AIpoint = 0  
limit= int(input("Number of games to played"))



while limit > count:
    user = input("Select 'r' for rock, 's' for scissors and 'p' for paper")
    AI = random.choice("Select 'r' for rock, 's' for scissors and 'p' for paper")
    count += int(1)
   
      
    
 
    if (user == 'r' and AI == 's') or (user == 's' and AI == 'p')\
        or (user == 'p' and AI == 'r'):
        print("You win the battle")
        userpoint += 1
    elif user == AI:
        print ("It's a tie")
    else:
        print("AI wins the battle")
        AIpoint += 1

    

if userpoint > AIpoint:   
    print(f"You won this war with a score of {userpoint} while AI got a score of {AIpoint}") 
elif userpoint == AIpoint:
    print (f"It is a tie with a score of {userpoint} and {AIpoint}")
else:
   print(f"AI wins this war with a score of {AIpoint} while you got a score of {userpoint}") 
   
   
    

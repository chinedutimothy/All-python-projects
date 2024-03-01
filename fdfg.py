'''
import random 

print("Welcome to Guessing number game")

def guess(x):
    random_number = int(input(f"Input a number between 1 and {x} for the computer to guess"))
    guess = 0
    limit = int(input("Input the number of guesses you're allowed to: "))
    count = int(0)
    for i in range(limit):
        guess = random.randint(1, x)
        print(guess)
        count += int(1)
        if guess == random_number and count < limit:
            print("You guessed correctly")
        elif guess != random_number and count < limit: 
            print("You're wrong")

            
                    
    print("You're out of guesses")
        

    
       
        

guess(15)
'''

import random 
print ("Guessing numbers")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    random_number = input("Number to be guessed: ")
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} to high (H) or is guess too low (L)")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"You got the {guess} correctly")

computer_guess(10)



   
        

    

       
            
            

           

   
            

        
              


    


        


                



                    
                
           

            

        
            
        

 
    



    
    



import random 

print("Welcome to Guessing number game")

def guess(x):
    random_number = random.randint(1, x)
    print(random_number)
    guess = 0
    limit = int(input("Input the number of guesses you're allowed to: "))
    count = int(0)
    for i in range(limit):
        guess = int(input(f"Guess a number between 1 and {x}: "))
        count += int(1)
        if guess != random_number:
            if guess > random_number and count < limit:
                print("Your guess is high \n keep guessing")
            elif guess < random_number and count < limit:
                print("Your guess is low \n Keep guessing")
        elif guess == random_number and count < limit:
            print("You guessed correctly")
                    
    print("You're out of guesses")
        

    
       
        

guess(15)



        

    

       
            
            

           

   
            

        
              


    


        


                



                    
                
           

            

        
            
        

 
    



    
    


#Welcome to todays coding challenge
#Creating a guessing game with FOR loop and putting a limit of 3 
#we would also be using the if statement and break also
#enjoy

username = "Friday"
password = "Octopus"
limit = 3
#guess = False

for guess in range(limit):
    guess1 = input("Guess username: ")
    guess2 = input("Guess password: ")
    if (guess1 == username) and (guess2 ==password): #(guess2 == password):
        print("You're right")
        break #used to end the guesses if you get both guesses right 
    else:
        #guess = False
        print("Keep guessing")
       
else:
    print("You're out of guesses")


   

#The only problem we have in this code is for  the keep guessing not to show at the end guesses and show the out of guesses 
  # you can always remove the else statement in line 17   
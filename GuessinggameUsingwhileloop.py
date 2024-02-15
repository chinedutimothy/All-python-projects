#creating a guessing game using while loop
#we have variables 
user_name = "Friday"
pass_word = "Octopus"
username = ""
password = ""
bothcount = 0
bothlimit = 3
no_trial = False # this is inplace because 


while ((username != user_name) or (password != pass_word)) and not (no_trial) :
    if bothcount < bothlimit :
    
        username = input("Input Username: ")
        password = input("Input Password: ")
        bothcount += 1
    else:
        no_trial = True

if no_trial:
    print("Your account has been blocked")
else:
    print("Logged in succesful")


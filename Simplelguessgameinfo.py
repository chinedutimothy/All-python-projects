
user_name = "Friday"
pass_word = "Octopus"
username = ""
password = ""
bothcount = 0
bothlimit = 3
no_trial = False


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


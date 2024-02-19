import string
import random

def gen_password():
    letters = string.ascii_letters
    random_letter = random.choice(letters)
    random_num = random.randint(0,9)
    letter_or_num = ["letter","number"]
    char_num = int(input("How many characters do you want in your password?: "))
   
    password = []
    for i in range(char_num):
        random_var = random.choice(letter_or_num)
        if random_var == "letter":
            random_letter = random.choice(letters)
            # replace print with this:
            password.append(random_letter)  
         
        elif random_var == "number":
            random_num = random.randint(0,9)
            password.append(str(random_num))
    return "".join(password)

print(gen_password())
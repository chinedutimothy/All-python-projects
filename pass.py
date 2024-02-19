import string
import random



def gen_password():
    letters = string.ascii_letters
    random_letter = random.choice(letters)
    random_num = random.randint(0,9)
    letter_or_num = ["letter","number"]
    char_num = int(input("How many characters do you want in your password?: "))

    for i in range(char_num):
        random_var = random.choice(letter_or_num)
        if random_var == "letter":
            random_letter = random.choice(letters)
            print(random_letter, end="")
        elif random_var == "number":
             random_num = random.randint(0,9)
             print(random_num, end= "")
    print("")

gen_password()


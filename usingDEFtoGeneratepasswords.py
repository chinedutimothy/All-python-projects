import random
import string

print("Generating Passwords")



def gen_password():
    num_of_passwords = int(input("Enter number of passwords to be generated: "))
    len_of_passwords = int(input("Enter length of passswords to be generated: ")) 
    for i in range(num_of_passwords):
        passwords = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(len_of_passwords))
        print("Here is/are your password(s)")
        print(passwords)

gen_password()



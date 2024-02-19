import random
import secrets


def roll_dice(num):
    return random.randint(1,num)
"""
def gen_password():
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz"
    passwords = ''.join(random.choice(char) for i in range(5))
    print(passwords)
gen_password()
"""



def gen_password(num):
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz"
    num = int(input("Enter number of passwords to be generated: "))
    passwords = ''.join(random.choice(char) for i in range(num))
    print(passwords)
    return passwords
gen_password()


"""
import secrets
#import string
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) 
for i in range(20))  # for a 20-character passwor
print(password)

"""

#password = ''.join(random.choices(all_characters, k=length))
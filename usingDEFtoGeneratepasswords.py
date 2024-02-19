import random
import string





def gen_password():
    num = int(input("Enter number of passwords: "))
    len_of_passwords = int(input("Enter length of passswords: "))
    for i in range(num):
        passwords = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(len_of_passwords))
        print(passwords)

gen_password()



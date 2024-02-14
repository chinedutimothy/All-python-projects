#you have to import
import random 

char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&**()"

number = int(input("Number of Passwords: "))
length = int(input("length of Passwords: "))
print("Here are your passwords")

for pwd in range(number):
    passwords = ""
    for pwd in range(length):
        passwords = passwords + random.choice(char)
    print(passwords)
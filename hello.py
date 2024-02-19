import random

upper_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_char = upper_char.lower()
numbers = "0123456789"
strings = "!@#$%^&*()_=+"
num = int(input("Number of passwords: "))
length = int(input("Length of passwords: "))

for pwd in range(num):
    passwords = ""
    for pwd in range(length):
        passwords += random.choice(numbers + strings + lower_char + upper_char)
    print (passwords)



#I created a password generator and im trying to assign the first index to be a string. how do I do that 
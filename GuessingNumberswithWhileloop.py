import random 

print("Welcome to Guessing number game")

def guess(x):
    random_number = random.randint(1, x)
    # print(random_number)  # Commenting out to keep the random number hidden
    limit = int(input("Input the number of guesses you're allowed to: "))
    count = 0
    while count < limit:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        count += 1
        if guess == random_number:
            print("You guessed correctly")
            return
        elif count < limit:  # Only give hints if guesses are left
            if guess > random_number:
                print("Your guess is high!!!\nKeep guessing")
            else:
                print("Your guess is low!!!\nKeep guessing")
    print("Out of guesses")

guess(15)

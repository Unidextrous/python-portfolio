import random
secret_number = random.randint(1, 50)
#print(secret_number) #for debugging or if you don't want to guess
guess = input("Please guess a number between 1 and 50: ")
while True:
    if guess == "q":
        break
    elif guess.isdigit() == True:
        if int(guess) == secret_number:
            print("You won!")
            break
        elif int(guess) < 1 or int(guess) > 50:
            guess = input("Out of range. Please guess again or type q to quit: ")
        else:
            guess = input("Please guess again or type q to quit: ")
    else:
        guess = input("Please enter a number, or type q to quit: ")
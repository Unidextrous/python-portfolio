import random

# Generate a random number between 1 and 50
secret_number = random.randint(1, 50)

# Uncomment this line to reveal the secret number for testing
# print(secret_number)

# Prompt the user to guess the number
guess = input("Please guess a number between 1 and 50: ")

# Main game loop
while True:
    # Allow the user to quit
    if guess == "q":
        break

    # Check if the input is a number
    elif guess.isdigit() == True:
        # Convert guess to integer for comparison
        if int(guess) == secret_number:
            print("You won!")
            break

        # Handle numbers outside the allowed range
        elif int(guess) < 1 or int(guess) > 50:
            guess = input("Out of range. Please guess again or type q to quit: ")
        
        # Guess was incorrect but in range
        else:
            guess = input("Please guess again or type q to quit: ")
    
    # Input was not a number
    else:
        guess = input("Please enter a number, or type q to quit: ")
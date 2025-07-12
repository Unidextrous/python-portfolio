# Prompt the user to enter a number
user_input = input("Please enter a number: ")

# Loop to repeatedly check for even or odd numbers
while True:
    # If the input is a digit, convert it and check even/odd
    if user_input.isdigit() == True:
        number = int(user_input)
        if number % 2 == 0:
            print("Even")
        else:
            print("Odd")
        
        # Ask for another number or allow quitting
        user_input = input("Enter another number or type q to quit: ")
    
    # Allow the user to quit
    elif user_input == "q":
        break

    # Handle invalid input
    else:
        user_input = input("Invalid entry - please try again or type q to quit: ")
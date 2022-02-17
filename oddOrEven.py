user_input = input("Please enter a number: ")
while True:
    if user_input.isdigit() == True:
        number = int(user_input)
        if number % 2 == 0:
            print("Even")
        else:
            print("Odd")
        user_input = input("Enter another number or type q to quit: ")
    elif user_input == "q":
        break
    else:
        user_input = input("Invalid entry - please try again or type q to quit: ")
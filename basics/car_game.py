# Initialize the car's engine state (off by default)
car_on = False

# Start a loop to receive user input continuously
while True:
    player_input = input(">")

    # Show the list of available commands
    if player_input == "help":
        print("start: starts car")
        print("stop: stops car")
        print("quit: exits program")
    
    # Start the car if it's not already on
    elif player_input == "start":
        if car_on == False:
            car_on = True
            print("starting car")
        else:
            print("car is already on!")
    
    # Stop the car if it's not already off
    elif player_input == "stop":
        if car_on == True:
            car_on = False
            print("car stopped")
        else:
            print("car is already stopped!")
    
    # Exit the loop and end the program
    elif player_input == "quit":
        break

    # Handle unknown commands
    else:
        print("invalid input")
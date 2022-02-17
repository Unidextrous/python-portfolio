car_on = False
while True:
    player_input = input(">")
    if player_input == "help":
        print("start: starts car")
        print("stop: stops car")
        print("quit: exits program")
    elif player_input == "start":
        if car_on == False:
            car_on = True
            print("starting car")
        else:
            print("car is already on!")
    elif player_input == "stop":
        if car_on == True:
            car_on = False
            print("car stopped")
        else:
            print("car is already stopped!")
    elif player_input == "quit":
        break
    else:
        print("invalid input")
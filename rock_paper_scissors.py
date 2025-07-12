import random
ai_pick = random.randint(0, 2)
if ai_pick == 0:
    ai_pick = "rock"
elif ai_pick == 1:
    ai_pick = "paper"
else:
    ai_pick = "scissors"
#print(ai_pick) #for debugging or if you don't want to guess
player_pick = input("Rock, paper, or scissors? ")
player_pick = player_pick.lower()
if player_pick == ai_pick:
    print("Draw")
elif player_pick == "rock" and ai_pick == "scissors":
    print("You won!")
elif player_pick == "paper" and ai_pick == "rock":
    print("You won!")
elif player_pick == "scissors" and ai_pick == "paper":
    print("You won!")
elif player_pick == "rock" or player_pick == "paper" or player_pick == "scissors":
    print("You lost")
else:
    print("Invalid entry")
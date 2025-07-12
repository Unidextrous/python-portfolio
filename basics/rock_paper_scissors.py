import random

# Randomly select the AI's choice as rock, paper, or scissors
ai_pick = random.randint(0, 2)
if ai_pick == 0:
    ai_pick = "rock"
elif ai_pick == 1:
    ai_pick = "paper"
else:
    ai_pick = "scissors"

# Uncomment for testing: print the AI's choice
# print(ai_pick)

# Prompt the player for their choice and convert it to lowercase
player_pick = input("Rock, paper, or scissors? ")
player_pick = player_pick.lower()

# Compare player's choice to AI's and determine outcome
if player_pick == ai_pick:
    print("Draw")
elif player_pick == "rock" and ai_pick == "scissors":
    print("You won!")
elif player_pick == "paper" and ai_pick == "rock":
    print("You won!")
elif player_pick == "scissors" and ai_pick == "paper":
    print("You won!")

# If the input was valid but the player lost
elif player_pick == "rock" or player_pick == "paper" or player_pick == "scissors":
    print("You lost")

# Handle invalid input
else:
    print("Invalid entry")
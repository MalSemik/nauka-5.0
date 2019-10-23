import random

choices = {}
# choices["player1"] = random.choice(["rock", "paper", "scissors"])
choices[random.choice(["rock", "paper", "scissors"])] = "player1"
choices[random.choice(["rock", "paper", "scissors"])] = "player2"
# choices["player2"] = random.choice(["rock", "paper", "scissors"])
set_choices = (set(choices.keys()))
rock_wins = {"rock", "scissors"}
paper_wins = {"rock", "paper"}
scissors_wins = {"scissors", "paper"}
if len(set_choices) == 1:
    print("Tie")
elif set_choices == rock_wins:
    print(choices["rock"])
elif set_choices == paper_wins:
    print(choices["paper"])
else:
    print(choices["scissors"])
print(choices)
    
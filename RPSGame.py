# Its Rock Paper Scissor game!!!

import random

# get player choice
def getPlayersChoice():
    while (1):
        player_choice = input("Enter a choice (Rock, Paper, Scissors) : ")
        if validateChoice(player_choice) == "yes":
            break
        print("Enter valid choice")
    return player_choice

# validating player choice
def validateChoice(choice):
    options = ["Rock", "Paper", "Scissors"]
    if choice in options:
        return "yes"
    return "no"

# get the choices made by player and computer
def get_choices():
    player_choice = getPlayersChoice()

    # available options
    options = ["Rock", "Paper", "Scissors"]

    # get random choice for computer
    computer_choice = random.choice(options)

    # dictionary
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

# check the winner
def check_winner(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "Draw"
    elif player == "Rock":
        if computer == "Scissors":
            return "Player wins"
        else:
            return "Computer wins"
    elif player == "Paper":
        if computer == "Scissors":
            return "Computer wins"
        else:
            return "Player wins"
    elif player == "Scissors":
        if computer == "Rock":
            return "Computer wins"
        else:
            return "Player wins"


choices = get_choices()
print(check_winner(choices.get("player"), choices.get("computer")))

import random
def get_computer_choice():
    choices = ["rock","paper","scissors"]
    return random.choice(choices)

def get_player_choice():
    player = input("Enter Rock,Paper or scissors :")
    return player

def check_winner(player,computer):
    if player == computer:
        print("Match Draw")
    elif (player == "rock" and computer == "scissors"):

    elif (player == "paper" and computer == "rock"):
        
    elif (player == "scissors" and computer == "paper"):
        break
    else:
        print("computer wins")

def play_game():
    player = get_player_choice()
    computer =get_computer_choice() 
    print("player choice :",player)
    print("computer choice :",computer)

def main():
    play_game()

main()
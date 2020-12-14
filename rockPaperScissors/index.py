import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ").lower()
    computer = random.choice(["r", 'p', 's'])

    if user == computer:
        print("It's a tie")
        return True

    if(is_win(user,computer)):
        print(f"Player won, because the computer put {objectByInitial(computer)} and player put {objectByInitial(user)}")
    else:
        print(f"Computer won, because the player put {objectByInitial(user)} and computer put {objectByInitial(computer)}")


def is_win(player, opponent):
    # Return true if player wins
    if ((player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')):
        return True
    else:
        return False

def objectByInitial(initial):
    if(initial == 'r'):
        return 'rock'
    elif (initial == 'p'):
        return 'paper'
    elif (initial == 's'):
        return 'scissors'

play()

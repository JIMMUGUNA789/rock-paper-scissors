import random
from enum import IntEnum


class Action(IntEnum):
    rock = 0
    paper = 1
    scissor = 2
def get_user_action():
    user_choice = input("Enter your choice- 0 for Rock, 1 for Paper, 2 for  Scissors : ")
    user_choice = int(user_choice)
    user_choice = Action(user_choice)
    return user_choice
def get_computer_choice():
     # Computer choice
    possible_actions = [1,2,3]
    computer_choice = random.choice(possible_actions)
    action = Action(computer_choice)
    return action
def determine_winner(user_choice, computer_choice):

    # output
    print(f"\n You chose {user_choice} and the computer chose {computer_choice}")
    #determine winner
    if user_choice == computer_choice:
        print(f"Its a draw")
    elif user_choice == Action.rock:
        if computer_choice == Action.scissor:
            print (f"Rock smashes scissors...you won")
        else:
            print(f"Paper covers rock...You loose")
    elif user_choice == Action.paper:
        if computer_choice ==Action.scissor:
            print(f"Scissors cut paper...you loose")
        else:
            print(f"paper covers rock...you win")
    elif user_choice == Action.scissor:
        if computer_choice == Action.paper:
            print(f"Scissors cut paper...you win")
        else:
            print(f"Rock smashes scissors...you loose")



while True:
    user_choice = get_user_action()
    computer_choice = get_computer_choice()
    determine_winner(user_choice=user_choice, computer_choice=computer_choice)
    
    
   
    play_again = input(f"press y to play again or n to end game : ")
    if play_again.lower() != 'y':
        break

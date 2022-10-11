import random
rock_action = 0
paper_action = 1
scissor_action = 2
while True:
    user_choice = input("Enter your choice- 0 for Rock, 1 for Paper, 2 for  Scissors : ")
    user_choice = int(user_choice)
    # Computer choice
    possible_actions = [1,2,3]
    computer_choice = random.choice(possible_actions)
    # output
    print(f"\n You chose {user_choice} and the computer chose {computer_choice}")
    #determine winner
    if user_choice == computer_choice:
        print(f"Its a draw")
    elif user_choice == rock_action:
        if computer_choice == scissor_action:
            print (f"Rock smashes scissors...you won")
        else:
            print(f"Paper covers rock...You loose")
    elif user_choice == paper_action:
        if computer_choice ==scissor_action:
            print(f"Scissors cut paper...you loose")
        else:
            print(f"paper covers rock...you win")
    elif user_choice == scissor_action:
        if computer_choice == paper_action:
            print(f"Scissors cut paper...you win")
        else:
            print(f"Rock smashes scissors...you loose")
    play_again = input(f"press y to play again or n to end game : ")
    if play_again.lower() != 'y':
        break

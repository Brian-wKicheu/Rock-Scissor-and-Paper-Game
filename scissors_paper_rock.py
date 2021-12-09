import random
win = 0
while True:
    my_choice = input("Enter a choice (rock, paper, scissors) Type Exit to quit")
    possible_choice = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choice)
    if my_choice == computer_choice:
        print(f"Both players selected {my_choice}. It's a tie")
    elif my_choice == "rock":
        if computer_choice == "scissors":
            print("Rock Smashes scissors you win")
            win += 1
        else:
            print("Paper Covers Rock You Lose!")
    elif my_choice == "paper":
        if computer_choice == "rock":
            print("Paper Covers Rock you Lose!")
            win += 1
        else:
            print("Scissors cuts paper You lose!")
    elif my_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors Cuts Paper!")
            win += 1
        else:
            print("Rock Smashes Scissors You Lose!")
    elif my_choice == "Exit":
        print(win)
        break
    else:
        print("Invalid Input")

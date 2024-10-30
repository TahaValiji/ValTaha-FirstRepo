import random

def main():
    name = input("Enter your name to play: ").title()
    print("Hey",name+"!! Welcome to the Rock Paper Scissors game :)")

    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    wins = 0
    losses = 0
    ties = 0

    while True:
        player = input("rock, paper or scissors: ").lower()
        if player not in choices:
            continue
        
        if computer == player:
            print("player: ".title(), player)
            print("computer: ".title(), computer)
            print("tie".title())
            ties += 1
        elif player == "rock" and computer == "scissors" or player == "paper" and computer == "rock" or player == "scissors" and computer == "paper": 
            print("player: ".title(), player)
            print("computer: ".title(), computer)
            print("you win!".title())
            wins += 1
        else:
            print("player: ".title(), player)
            print("computer: ".title(), computer)
            print("you lose!".title())
            losses += 1
            
            play_again = input("do you want to play again (Yes or no) : ".title()).lower()
            if play_again != "yes":
                matches = wins + losses + ties
                print("You played {} matches".format(matches))
                print("You won {0} times\nlost {1} times\nand match tied {2} times".title().format(wins, losses, ties))
                quit()
            else:
                continue

while True:
    ask = input("Do you want to play (Yes or No): ").lower()
    if ask == "yes":
        main()
    elif ask == "no":
        quit()
    else:
        continue


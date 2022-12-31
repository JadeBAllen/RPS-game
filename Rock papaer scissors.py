from random import randint

#List of characters
t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
    player = input("Rock, Paper, Scissors?: ")
    if player == computer:
        print("Draw!")
    elif player == "Rock":
        if computer == "Paper":
            print("Loser!", computer, "covers", player)
        else:
            print("Winner!", player, "beats", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("Loser! Try again next time!", computer, "cuts", player)
        else:
            print("Let's go! Winner!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("What a loser! Try again, DORK!", computer, "smashes", player)
        else:
            print("There you go!! Lets go, NERD!!", player, "slashes", computer)
    else:
        print("That's invalid.")

    #player is false so the loop continues

    player = False
    computer = t[randint(0,2)]



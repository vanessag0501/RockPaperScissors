import random


while True:
    print("Welcome to Rock Paper Scissor\n")

    userInput = raw_input("Choose one: rock, paper, scissors\n")
    options=["rock", "paper", "scissors"]
    computerChoice = random.choice(options)

    print("You chose: " + userInput)

    print("Computer chose: " + computerChoice) 


    if userInput == computerChoice:
        print("It's a tie")

    elif userInput == "rock":
        if computerChoice == "scissors":
            print("Rock beats scissors. You win!")
        else:
            print("Paper covers rock. You lose.")

    elif userInput == "paper":
        if computerChoice == "rock":
            print("Paper covers rock. You win!")
        else:
            print("Scissors cuts paper. You lose")
            
    elif userInput == "scissors":
        if computerChoice == "paper":
            print("Scissors cuts paper. You win!")
        else:
            print("Rock beats scissor. You lose") 

    continuePlaying=raw_input("Do you want to play again? Y or N\n")

    if continuePlaying == 'n' or continuePlaying == 'N':
        break
    if continuePlaying == 'y' or continuePlaying == 'Y':
        continue
    



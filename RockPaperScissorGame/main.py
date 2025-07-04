import random
print("WELCOME\nRock, Paper, Scissors choose any one")

while True:
    
    computer = random.choice(["Rock", "Paper", "Scissors"])

    player = input("Your turns : ").lower()
    print(f"Computer turns : {computer}")

    computer = computer.lower()

    if player == computer:
        print("Tie")  

    elif (player == "rock") and (computer == "paper"):
        print("You Lose")

    elif (player == "paper") and (computer == "scissors"):
        print("You Lose")

    elif (player == "scissors") and (computer == "rock"):
        print("You Lose")
  
    else :
        print("You win")

    print()

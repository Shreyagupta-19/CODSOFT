import random
print("\n~~~ Welcome to Rock Paper Scissor Game ~~~\n")
computerscore = 0
playerscore = 0
noOfRounds = int(input("\nHow many rounds do you want to play?: "))
nor=1
lt = []
print("\nEnter 1 For Rock\nEnter 2 For Paper\nEnter 3 For Scissor\n")
while nor <= noOfRounds:
    computerValue= random.randint(1, 3)
    playerInput = int(input("Enter Your Choice: "))
    if computerValue == playerInput:
        lt.append(f"Round {nor} - TIES")
        print(f"\nYou Entered: {playerInput}\nComputer Played: {computerValue}\nRound {nor} - TIES.\n")

    elif computerValue == 1 and playerInput == 2:
        lt.append(f"Round {nor} - YOU WINS")
        playerscore += 1
        print(f"\nYou Entered: {playerInput}\nComputer Played: {computerValue}\nRound {nor} - YOU WINS.\n") 

    elif computerValue == 2 and playerInput == 1:
        lt.append(f"Round {nor} - COMPUTER WINS")
        computerscore += 1
        print(f"\nYou Entered: {playerInput}\nComputer Played: {computerValue}\nRound {nor} - COMPUTER WINS.\n")

    elif computerValue == 1 and playerInput == 3:
        lt.append(f"Round {nor} - COMPUTER WINS")
        computerscore += 1
        print(f"\nYou Entered: {playerInput}\nComputer Played: {computerValue}\nRound {nor} - COMPUTER WINS.\n")

    elif computerValue == 3 and playerInput == 1:
        lt.append(f"Round {nor} - YOU WINS")
        playerscore += 1
        print(f"\nYou Entered: {playerInput}\nComputer Played: {computerValue}\nRound {nor} - YOU WINS.\n")

    elif computerValue == 2 and playerInput == 3:
        lt.append(f"Round {nor} - YOU WINS")
        playerscore += 1
        print(f"\nYou Entered: {playerInput}\nComputer Played: {computerValue}\nRound {nor} - YOU WINS.\n")

    elif computerValue == 3 and playerInput == 2:
        lt.append(f"Round {nor} - COMPUTER WINS")
        computerscore += 1
        print(f"\nYou Entered: {playerInput}\nComputer Played: {computerValue}\nRound {nor} - COMPUTER WINS.\n")
        
    else:
        print("ERROR")
    nor +=1
    
print("\nComputer Score: ", computerscore)
print(f"\nYour Score: {playerscore}")
print("\nNumber of Rounds Played: ", noOfRounds)
[print(i) for i in lt]

if playerscore > computerscore:
    print(f"\nYOU WINS THE GAME!!!")

elif playerscore == computerscore:
    print(f"\nIt\'s a Tie. Try Again.!!!'")

else:
    print("\nCOMPUTER WINS THE GAME!!! BETTER LUCK NEXT TIME.")

print("\n\n~~~ THANK YOU FOR PLAYING ~~~\n\n")
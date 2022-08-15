import random

import time
st = time.time()

###########################

def game():
    elements = ["Rock","Paper","Scissor"]
    comp = elements[random.randint(0,2)]
    player = None 
    while player not in elements:
        player = input("Enter your selection: ")
        if player == "Rock" or player=="Paper" or player=="Scissor":
            if comp == "Rock" and player=="Paper":
                print(f'Player has {player} and comp has {comp}, so PLAYER won')
            elif comp == "Paper" and player=="Rock":
                print(f'Player has {player} and comp has {comp}, so COMP won')

            elif comp == "Paper" and player=="Scissor":
                print(f'Player has {player} and comp has {comp}, so PLAYER won')
            elif comp == "Scissor" and player=="Paper":
                print(f'Player has {player} and comp has {comp}, so COMP won')
                 
            elif comp == "Scissor" and player=="Rock":
                print(f'Player has {player} and comp has {comp}, so PLAYER won')
            elif comp == "Rock" and player=="Scissor":
                print(f'Player has {player} and comp has {comp}, so COMP won')
            elif comp == player:
                print(f'Player & comp both have {comp}, so It is a tie')
        else:
            player = input("Plase enter valid Element: ")
    

def playGame():
    game()
   

playAgain = True
while playAgain == True:
    playGame()
    playAgainAns = input("Press Enter to play or enter key to exit: ")
    if playAgainAns != "":
        print("Thank you for playing with me.")
        playAgain = False
        break
     

####################################

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

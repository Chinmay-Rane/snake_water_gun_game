''' 
1 is snake
-1 is water
0 is gun
'''

def play_again():

    again=input("Want to play again?: ")
    if(again=="yes"):
        main()
    elif(again=="no"):
        thx()
    
def thx():
    print("Thanks for playing")

def show_help():
    print("""
==================== Snake-Water-Gun Manual ====================

This is a 2-player game (You vs Computer). 
Each player chooses one of the three options:

    🐍  Snake   → Represented by 's'
    💧  Water   → Represented by 'w'
    🔫  Gun     → Represented by 'g'

Rules:
    1. Snake drinks Water   → Snake wins
    2. Water douses Gun     → Water wins
    3. Gun shoots Snake     → Gun wins
    4. Same choice          → It's a Draw

How to Play:
    - Type 's' for Snake
    - Type 'w' for Water
    - Type 'g' for Gun
    - After each round, you can choose to play again.
          
How to PLay-again:
    - Type 'yes' to play again
    - Type 'no' to exit

=================================================================
        
    """)


def main():
    import random
    #intro 
    print('''
          ==================== Snake-Water-Gun Manual ====================

          Welcome to snake water gun game!
          
          Type 's' for snake
          Type 'w' for water
          Type 'g' for gun
          
          Type 'help' to access the help menu

          =================================================================
          ''')
    #computer
    moves=(1,-1,0)
    computer=random.choice(moves)
    
    #playerinput
    youstr = input("Enter your choice: ")

    # check if user wants help
    if youstr.lower() == "help":
        show_help()

        return play_again()   # restart the game after showing help

    # dictionary for valid moves
    youDict = {"s": 1, "w": -1, "g": 0}

    # check if input is valid
    if youstr not in youDict:
        print("Invalid input! Try again.\n")
        return main()
    
    you = youDict[youstr]
    reversedict={1:"Snake",-1:"Water",0:"Gun"} #to convert int to text to give as an output for your and computer's move

    #print moves
    print(f"Computer: {reversedict[computer]} \nYou: {reversedict[you]}")
    #win/lose text
    def snake():
        print("Snake drank the water")
    def water():
        print("Water stopped the gun")
    def gun():
        print("Gun shot the snake")

    #conditons
    if(computer==you):
        print("Its a draw")
        play_again()
    # computer wins cases
    elif (computer == 1 and you == -1):   # Snake vs Water
        snake()
        print("Computer wins!")
        play_again()
    elif (computer == -1 and you == 0):   # Water vs Gun
        water()
        print("Computer wins!")
        play_again()
    elif (computer == 0 and you == 1):    # Gun vs Snake
        gun()
        print("Computer wins!")
        play_again()
    # you win cases
    elif (you == 1 and computer == -1):   # Snake vs Water
        snake()
        print("You win!")
        play_again()
    elif (you == -1 and computer == 0):   # Water vs Gun
        water()
        print("You win!")
        play_again()
    elif (you == 0 and computer == 1):    # Gun vs Snake
        gun()
        print("You win!")
        play_again()
    else:
        print("Something went wrong")
        play_again()
main()
        
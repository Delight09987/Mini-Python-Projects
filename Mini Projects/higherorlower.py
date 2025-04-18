import random
options = ("Higher","Lower") # # aim of the game
first_number = random.randrange(0,11) # the computer 
while True:
    print(first_number) # current number
    player = input("Higher or Lower ").capitalize() # inside a loop == more rounds for player
    if player not in options: 
        print("Must be Higher or Lower")
        continue # returns back to print statement above
    # there is not an elif bc they are not linked    
    next_number = random.randint(0, 11) # outside loops = generated once
    if player == "Higher" and next_number > first_number or \
    player == "Lower" and next_number < first_number:
        print("Well Done")
    elif next_number == first_number:
        print("Tie!")
    else:
        print("Wrong")
    next_number = first_number # next number after the guess becomes current number
    again = input("Do you want to play again? (yes/no):").lower()
    if again != "yes":
        print("Thanks for playing")
        break # breaks loop altogether
    # player has to guess if next number will be hghr or lower



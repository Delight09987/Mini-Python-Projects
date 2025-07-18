import random 

Choices = ("rock", "paper", "scissors")
user = input("Choose between rock,paper,scissors").lower()
bot = random.choice(Choices)

losses = {
    "rock":"paper",
    "paper":"scissors",
    "scissors":"rock"
}

def check_winner(Userchoice,Botchoice): # 1 for win, 2 is for tie, 3 is loss
    
    if user == bot: # tie
        result =  1
    elif bot == losses[user]:
        result = 2 # bot wins
    else:
        result = 3 # user wins
    return result

def main():
    Userscore = 100
    Botscore = 100
    
    while Userscore > 0 and Botscore > 0: # loops stops wehn dondtio is false
        if user not in Choices:
            print("Try Again")
            continue # keeps going back to the beginning
    
    print(f"You choose:{user},the Bot chosee: {bot}")

    result = check_winner(user,bot) # must define variable in functions

    if result == 1:
        print("Tie!")
        Userscore -= 10
        Botscore -= 10
    elif result == 2:
        print("User Wins")
        botscore -= 10
    else:
        Userscore -= 10
        print("Bot wins")

print("Game Over") # this is not indendented because I want it to run once.
main()

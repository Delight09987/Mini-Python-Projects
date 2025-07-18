import glossary # list of words the player has to guess(outside of the function)
import random 
# bot choooses the word at random from the list/tuple
#BOT = random.choice(glossary.arr) # arr is for array
failed_attempts = { 7 : "X_X",
            6: "+_+" ,
            5 : ":(",
            4: ":0",
            3:":-/",
            2: ":-P",
            1: "o_0"                    
            
}
choice = input("Choose between red,green or blue ").lower() # player chooses between three colours
# create underscores and multiplying it by len of the word
# 7 attempts because 7 is thE number of perfection
# keys representing the number of incorrect attempts

# display_answer(answer):


def choose_colour(choice): # choice variable goes here
    if choice == "red":
        return random.choice(glossary.Red_synonyms) # choosing the random colour
    elif choice == "green":
        return random.choice(glossary.Green_synonyms)
    elif choice == "blue":
        return random.choice(glossary.Blue_synonyms)
    else:
        print("Invalid choice")



answer = choose_colour(choice)

while choice != answer:
    answer_line = ["_"] # use a list because it is mutable
    hidden_word = answer_line * len(answer)
    guess = input("guess the letters ").lower() # guess is a letter

    if guess in answer:
        for i in range(len(answer)):
            if answer[i] == guess: # check if answer is the same 
                hidden_word[i].append(guess) # hidden word will be updated    
                print(hidden_word)
'''''
    for i in answer:
        if i in guess:
            answer_line += i
        else:
            answer_line += "_"
'''''
   

    
    
            # inside of function called 7 attempts failed 
# asking the player for a guess -- if letter is not in word then ask player to try again

# else continue and return an updated version of the hangman

# create a function for attempted tries # should return the updated version of the hangman

# create a different main function in a while loop allowing events to be ran

# while attempts are > 0

# print well done if the player has guessed the word/print want to try again after player has failed or word was revealed to h
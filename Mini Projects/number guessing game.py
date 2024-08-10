import random

limit = input("Type a number: ")
if limit.isdigit():  # Checking if it is a digit
    limit = int(limit)
    
    if limit <= 0:
        print('try something bigger')
        quit()
else:
    print('type a number next time')
    quit()

random_number = random.randint(0, limit)  # Corrected above_range to limit
#print(f"Random number to guess: {random_number}")  # Debug: Show the random number

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    print(f"User guess: {user_guess}")  # Debug: Show the user's guess

    if user_guess.isdigit():  # Checking if it is a digit
        user_guess = int(user_guess)
    else:
        print('type a number next time')
        continue  # Removed quit() to allow the loop to continue

    if user_guess == random_number:
        print('You got it')
        break
    else:
        print('You got it wrong')


print('You got', guesses , 'guesses') # don't concanate add commas
def ask_questions(prompt, correct_answer):
    global score
    while True:
        choice = input(prompt).strip().lower()  # Get user input and normalize it
        if choice == correct_answer.lower():   # Check if input matches the correct answer
            print('Correct')
            score += 1
            break  # Exit the loop if the answer is correct
        else:
            print('That is wrong. Try again.')  # Notify user of incorrect answer


print('M or F')

print('Just kidding')

score = 0

Question = input('Do you want to play (YES/NO) ').strip().lower()

if Question != 'yes':
    print('Go away')
    quit()

ask_questions("What is my favourite colour? ", 'black'  )
ask_questions("What is my favourite fruit? ", 'Orange' )

print('You have', score , 'points')
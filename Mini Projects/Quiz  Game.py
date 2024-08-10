print('Welcome to my game')

question = input('Do you want to play? ').lower() # prompt goes here

score = 0

if question != 'yes':
    quit() # the program stops here
    score += 1 # everytime the answer is correct the user gets a point

print("Good! Let's play :) ")

answer = input("What does CPU stand for? ")
try :
    answer == "Central Processing Unit"
    print('Correct')
    score += 1
except :
    print('Incorrect')


answer = input("What does RAM stand for? ")
try :
    answer == "Random Access Unit"
    print('Correct')
    score += 1
except :
    print('Incorrect')


answer = input("What does GPU stand for? ")
try :
    answer == "Graphics Processing Unit"
    print('Correct')
    score += 1
except :
    print('Incorrect')

print('You got' + str(score) + 'questions right')

print('You got' + str((score/3 ) * 100) + '%. ') #percentage
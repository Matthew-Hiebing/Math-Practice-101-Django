#-----------------------------------------------------------------------------#

def multiplication():
    num1 = random.randint(0, 12)
    num2 = random.randint(0, 12)
    problemResult = num1 * num2

    print(str(num1), '*', str(num2))
    userAnswer = int(input())

    if userAnswer == problemResult:
        print("\nCorrect!  Do you want to play again? Please enter yes or no.")
        userResponse = str(input())
        if userResponse.lower()[0] == 'y':
            random_func = choice([
                multiplication,
                division,
                subtraction,
                addition
                ])
            random_func()
        elif userResponse.lower()[0] == 'n':
            False
        else:
            print("You didn't answer yes or no")

    if userAnswer != problemResult:
        count = 0
        while count < 2:
            count += 1
            print("Sorry, that was not the correct answer.  Please try again.")
            print(str(num1), '*', str(num2))
            userAnswer = int(input())
            if userAnswer == problemResult:
                random_func = choice([
                    multiplication,
                    division,
                    subtraction,
                    addition
                    ])
                random_func()
        else:
            print("Sorry, you are out of guesses")

#-----------------------------------------------------------------------------#

def addition():
    num1 = random.randint(0, 12)
    num2 = random.randint(0, 12)
    problemResult = num1 + num2

    print(str(num1), '+', str(num2))
    userAnswer = int(input())

    if userAnswer == problemResult:
        print("\nCorrect!  Do you want to play again? Please enter yes or no.")
        userResponse = str(input())
        if userResponse.lower()[0] == 'y':
            random_func = choice([
                multiplication,
                division,
                subtraction,
                addition
                ])
            random_func()
        elif userResponse.lower()[0] == 'n':
            False
        else:
            print("You didn't answer yes or no")

    if userAnswer != problemResult:
        count = 0
        while count < 2:
            count += 1
            print("Sorry, that was not the correct answer.  Please try again.")
            print(str(num1), '+', str(num2))
            userAnswer = int(input())
            if userAnswer == problemResult:
                random_func = choice([
                    multiplication,
                    division,
                    subtraction,
                    addition
                    ])
                random_func()
        else:
            print("Sorry, you are out of guesses")

#-----------------------------------------------------------------------------#

def division():
    num1 = random.randint(0, 12)
    num2 = random.randint(1, 12)
    problemResult = (num2 * num1)/num2

    print(str(num2 * num1), '/', str(num2))
    userAnswer = int(input())

    if userAnswer == problemResult:
        print("\nCorrect!  Do you want to play again? Please enter yes or no.")
        userResponse = str(input())
        if userResponse.lower()[0] == 'y':
            random_func = choice([
                multiplication,
                division,
                subtraction,
                addition
                ])
            random_func()
        elif userResponse.lower()[0] == 'n':
            False
        else:
            print("You didn't answer yes or no")

    if userAnswer != problemResult:
        count = 0
        while count < 2:
            count += 1
            print("Sorry, that was not the correct answer.  Please try again.")
            print(str(num2 * num1), '/', str(num2))
            userAnswer = int(input())
            if userAnswer == problemResult:
                random_func = choice([
                    multiplication,
                    division,
                    subtraction,
                    addition
                    ])
                random_func()
        else:
            print("Sorry, you are out of guesses")

#-----------------------------------------------------------------------------#

def subtraction():
    num1,num2 =sorted((random.randint(0,12),random.randint(0,12)),reverse=True)
    problemResult = (num2 * num1) - num2

    print(str(num2 * num1), '-', str(num2))
    userAnswer = int(input())

    if userAnswer == problemResult:
        print("\nCorrect!  Do you want to play again? Please enter yes or no.")
        userResponse = str(input())
        if userResponse.lower()[0] == 'y':
            random_func = choice([
                multiplication,
                division,
                subtraction,
                addition
                ])
            random_func()
        elif userResponse.lower()[0] == 'n':
            False
        else:
            print("You didn't answer yes or no")

    if userAnswer != problemResult:
        count = 0
        while count < 2:
            count += 1
            print("Sorry, that was not the correct answer.  Please try again.")
            print(str(num2 * num1), '-', str(num2))
            userAnswer = int(input())
            if userAnswer == problemResult:
                random_func = choice([
                    multiplication,
                    division,
                    subtraction,
                    addition
                    ])
                random_func()
        else:
            print("Sorry, you are out of guesses")

#-------------------------------GAME START------------------------------------#

print("Hello brave student, welcome to Math 101. In this game you will be"
" presented a random math problem that you will need to solve.  It will be a"
" random choice of subtraction, addition, division, and multiplication. You"
" will have 2 guesses per problem, after that, GAMEOVER!")

import random
from random import choice

random_func = choice([
    multiplication,
    division,
    subtraction,
    addition
    ])

if input("\nAre you ready to start? ").lower()[0] == 'y':
    random_func()
else:
    pirnt("All right, another time then!")
    False




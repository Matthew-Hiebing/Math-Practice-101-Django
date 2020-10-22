#-----------------------------------------------------------------------------#
def multiplication():

    import random
    count = 0

    while True:
        num1 = random.randint(0, 12)
        num2 = random.randint(0, 12)
        problemResult = num1 * num2


        print(str(num1), '*', str(num2))
        userAnswer = int(input())

        if userAnswer == problemResult:
            print("\nCorrect!  Do you want to play again? Please enter yes or no.")
            userResponse = str(input())
            if userResponse.lower()[0] == 'n':
                break
            if userResponse.lower()[0] == 'y':
                random_operator()

        if userAnswer != problemResult:
            count += 1
            print("Sorry, that was not the correct answer.  Please try again.")
            print(str(num1), '*', str(num2))
            userAnswer = int(input())

            if count >= 2:
                print("Sorry, you are out of guesses")
                break


#-----------------------------------------------------------------------------#
def addition():

    import random
    count = 0

    while True:
        num1 = random.randint(0, 12)
        num2 = random.randint(0, 12)
        problemResult = num1 + num2


        print(str(num1), '+', str(num2))
        userAnswer = int(input())

        if userAnswer == problemResult:
            print("\nCorrect!  Do you want to play again? Please enter yes or no.")
            userResponse = str(input())
            if userResponse.lower()[0] == 'n':
                break
            if userResponse.lower()[0] == 'y':
                random_operator()

        if userAnswer != problemResult:
            count += 1
            print("Sorry, that was not the correct answer.  Please try again.")
            print(str(num1), '+', str(num2))
            userAnswer = int(input())

            if count >= 2:
                break


#-----------------------------------------------------------------------------#
def division():

    import random
    count = 0

    while True:
        num1 = random.randint(0, 12)
        num2 = random.randint(1, 12)
        problemResult = (num2 * num1)/num2


        print(str(num2 * num1), '/', str(num2))
        userAnswer = int(input())

        if userAnswer == problemResult:
            print("\nCorrect!  Do you want to play again? Please enter yes or no.")
            userResponse = str(input())
            if userResponse.lower()[0] == 'n':
                break
            if userResponse.lower()[0] == 'y':
                random_operator()

        if userAnswer != problemResult:
            count += 1
            print("Sorry, that was not the correct answer.  Please try again.")
            print(str(num1), '/', str(num2))
            userAnswer = int(input())

            if count >= 2:
                break


#-----------------------------------------------------------------------------#
def subtraction():

    import random
    count = 0

    while True:
        num1, num2 = sorted((random.randint(0, 12), random.randint(0, 12)), reverse=True)
        problemResult = num1 - num2


        print(str(num2 * num1), '-', str(num2))
        userAnswer = int(input())

        if userAnswer == problemResult:
            print("\nCorrect!  Do you want to play again? Please enter yes or no.")
            userResponse = str(input())
            if userResponse.lower()[0] == 'n':
                break
            if userResponse.lower()[0] == 'y':
                random_operator()

        if userAnswer != problemResult:
            count += 1
            print("Sorry, that was not the correct answer.  Please try again.")
            print(str(num1), '-', str(num2))
            userAnswer = int(input())

            if count >= 2:
                break


#-----------------------------------------------------------------------------#
import random

operators = [multiplication(), division(), subtraction(), division()]

print("Hello brave student, welcome to Math 101. In this game you will"
" be presented a random math problem that you will need to solve.  It"
" will be a random choice of addition, subtraction, multiplication, and"
" division. You will have 2 guesses for each problem, after that,"
" GAMEOVER!")

if input("\nAre you ready to start? ").lower()[0] == y:
    random_operator()
else:
    False



def random_operator():
    random.choice(operators)

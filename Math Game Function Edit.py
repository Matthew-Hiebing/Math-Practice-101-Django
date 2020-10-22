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
                continue

        if userAnswer != problemResult:
            count += 1
            print("Sorry, that was not the correct answer.  Please try again.")
            print(str(num1), '*', str(num2))
            userAnswer = int(input())

            if count >= 2:
                print("Sorry, you are out of guesses")
                break


#multiplication()

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
                continue

        if userAnswer != problemResult:
            count += 1
            print("Sorry, that was not the correct answer.  Please try again.")
            print(str(num1), '+', str(num2))
            userAnswer = int(input())

            if count >= 2:
                break


#addition()


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
                continue

        if userAnswer != problemResult:
            count += 1
            print("Sorry, that was not the correct answer.  Please try again.")
            print(str(num1), '/', str(num2))
            userAnswer = int(input())

            if count >= 2:
                break


division()

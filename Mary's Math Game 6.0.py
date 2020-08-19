#This is a multiplication game with two guesses and the opportunity to keep playing if you answer correctly.

import random #Imports the random module for generating random integers
import operator #Imports the operator module for using the operators:add, sub, truediv, mul

operatorChoices = {"+":operator.add, "-":operator.sub, "/":operator.truediv, "*":operator.mul}
op = random.choice(["+", "*", "/", "-"])
num1 = random.randint(0,12)
num2 = random.randint(1, 12)
result = operatorChoices[op](num1,num2)
guessesTaken = 0 #Program starts with 0 guesses, each time you get an incorrect answer it adds "1" to this count until you reach "2", then you're out of guesses and the program ends.

print("Hello brave Math soldier, welcome to Math121. In this game you will be presented a math problem that you will need to solve.")  
print("It will be a random choice of addition, and multiplication. You will have 2 guesses for each problem, after that, GAMEOVER!. Here's your first problem: ")

while guessesTaken <= 2: #The while loop will continue to work until guessesTaken is <2.
	if op == "+": #If the random op is "+" it runs through this if loop.
		print(str(num1), op, str(num2))
		answer = int(input())
		if answer == result: # If the user answers corectly it allows you to keep play.
			print("\nCorrect!  Do you want to play again? Please type Yes or No.")
			answer = str(input())
			if (answer == "No") or (answer == "no") or (answer == "N") or (answer == "n"): # If user says "no" the game will end.
				break
			if (answer == "Yes") or (answer == "yes") or (answer == "Y") or (answer == "y"): #If user answers correctly and wants to play again another random op is generated and another set of 4 if statements is presented.
				import random   #Re-importing random, operator, operator choices, and integers makes sure the user doesn't get the same integers if they answer correctly and want to play again.
				import operator #If you don't re-import these items the next question will use the same integers that you started with before the while loop began.
				operatorChoices = {"+":operator.add, "-":operator.sub, "/":operator.truediv, "*":operator.mul}
				op = random.choice(["+", "*", "/", "-"])
				num1 = random.randint(1,12)
				num2 = random.randint(1, 12)
				result = operatorChoices[op](num1,num2)
				if op == "+":
					print(str(num1), op, str(num2))
					answer = int(input())
					if answer == result:
						print("\nCorrect!  Do you want to play again? Please type Yes or No.")
						answer = str(input())
						if (answer == "No") or (answer == "no") or (answer == "N") or (answer == "n"):
							break
						if (answer == "Yes") or (answer == "yes") or (answer == "Y") or (answer == "y"): # If the user answers correctly and wants to play again it generates
																										 # a random op and integers and starts you back from the beginning.
							import random   # This last loop of re-importing random operators and integers ensures you don't get the same numbers when you go back to the beginning of the while loop.
							import operator 
							operatorChoices = {"+":operator.add, "-":operator.sub, "/":operator.truediv, "*":operator.mul}
							op = random.choice(["+", "*", "/", "-"])
							num1 = random.randint(1,12)
							num2 = random.randint(1, 12)
							result = operatorChoices[op](num1,num2)
							continue
				if op == "-":
					num1, num2 = sorted((random.randint(1,12), random.randint(1,12)), reverse=True)
					result = num1 - num2
					print(str(num1), op, str(num2))
					answer = int(input())
					if answer == result:
						print("\nCorrect!  Do you want to play again? Please type Yes or No.")
						answer = str(input())
						if (answer == "No") or (answer == "no") or (answer == "N") or (answer == "n"):
							break
						if (answer == "Yes") or (answer == "yes") or (answer == "Y") or (answer == "y"): #If user answers correctly and wants to play again they go through the code below.
							import random
							import operator
							operatorChoices = {"+":operator.add, "-":operator.sub, "/":operator.truediv, "*":operator.mul}
							op = random.choice(["+", "*", "/", "-"])
							num1 = random.randint(1,12)
							num2 = random.randint(1, 12)
							result = operatorChoices[op](num1,num2)
							continue
				if op == "*":
					print(str(num1), op, str(num2))
					answer = int(input())
					if answer == result:
						print("\nCorrect!  Do you want to play again? Please type Yes or No.")
						answer = str(input())
						if (answer == "No") or (answer == "no") or (answer == "N") or (answer == "n"):
							break
						if (answer == "Yes") or (answer == "yes") or (answer == "Y") or (answer == "y"): #If user answers correctly and wants to play again they go through the code below.
							import random
							import operator
							operatorChoices = {"+":operator.add, "-":operator.sub, "/":operator.truediv, "*":operator.mul}
							op = random.choice(["+", "*", "/", "-"])
							num1 = random.randint(1,12)
							num2 = random.randint(1, 12)
							result = operatorChoices[op](num1,num2)
							continue
				if op == "/":
					import random
					num1 = random.randint(0,12)
					num2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12])
					x = num2 * num1
					result = x/num2
					print(str(x), op, str(n
						um2))
					answer = int(input())
					if answer == result:
						print("\nCorrect!  Do you want to play again? Please type Yes or No.")
						answer = str(input())
						if (answer == "No") or (answer == "no") or (answer == "N") or (answer == "n"):
							break
						if (answer == "Yes") or (answer == "yes") or (answer == "Y") or (answer == "y"): #If user answers correctly and wants to play again they go through the code below.
							import random
							import operator
							operatorChoices = {"+":operator.add, "-":operator.sub, "/":operator.truediv, "*":operator.mul}
							op = random.choice(["+", "*", "/", "-"])
							num1 = random.randint(0,12)
							num2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12])
							result = operatorChoices[op](num1,num2)
							continue
		if answer != result: # If the user does not answer correctly it adds a guess to guessesTaken and returns you to the beginning.  
							 # If you don't aswer correctly it asks you to re-answer the same poroblem you got wrong, the script only re-generates new integers if you get the answer correct.
			guessesTaken += 1
			print("\nWrong, try again if you have guesses left.")

	if op == "-": #If the random op is "-" it runs through this if loop.
		num1, num2 = sorted((random.randint(1,12), random.randint(1,12)), reverse=True)
		result = num1 - num2
		print(str(num1), op, str(num2))
		answer = int(input())
		if answer == result:
			print("\nCorrect!  Do you want to play again? Please type Yes or No.")
			answer = str(input())
			if (answer == "No") or (answer == "no") or (answer == "N") or (answer == "n"):
				break
			if (answer == "Yes") or (answer == "yes") or (answer == "Y") or (answer == "y"):
				import random
				import operator
				operatorChoices = {"+":operator.add, "-":operator.sub, "/":operator.truediv, "*":operator.mul}
				op = random.choice(["+", "*", "/", "-"])
				num1 = random.randint(1,12)
				num2 = random.randint(1, 12)
				result = operatorChoices[op](num1,num2)
				if op == "+":
					print(str(num1), op, str(num2))
					answer = int(input())
					if answer == result:
						print("\nCorrect!  Do you want to play again? Please type Yes or No.")
						answer = str(input())
						if (answer == "No") or (answer == "no") or (answer == "N") or (answer == "n"):
							break
						if (answer == "Yes") or (answer == "yes") or (answer == "Y") or (answer == "y"):
							import random
							import operator
							operatorChoices = {"+":operator.add, "-":operator.sub, "/":operator.truediv, "*":operator.mul}
							op = random.choice(["+", "*", "/", "-"])
							num1 = random.randint(1,12)
							num2 = random.randint(1, 12)
							result = operatorChoices[op](num1,num2)
							continue
				if op == "-":
					num1, num2 = sorted((random.randint(1,12), random.randint(1,12)), reverse=True)
					result = num1 - num2
					print(str(num1), op, str(num2))
					answer = int(input())
					if answer == result:
						print("\nCorrect!  Do you want to play again? Please type Yes or No.")
						answer = str(input())
						if (answer == "No") or (answer == "no") or (answer == "N") or (answer == "n"):
							break
						if (answer == "Yes") or (answer == "yes") or (answer == "Y") or (answer == "y"):
							import random
							import operator
							operatorChoices = {"+":operator.add, "-":operator.sub, "/":operator.truediv, "*":operator.mul}
							op = random.choice(["+", "*", "/", "-"])
							num1 = random.randint(1,12)
							num2 = random.randint(1, 12)
							result = operatorChoices[op](num1,num2)
							continue
				if op == "*":
					print(str(num1), op, str(num2))
					answer = int(input())
					if answer == result:
						print("\nCorrect!  Do you want to play again? Please type Yes or No.")
						answer = str(input())
						if (answer == "No") or (answer == "no") or (answer == "N") or (answer == "n"):
							break
						if (answer == "Yes") or (answer == "yes") or (answer == "Y") or (answer == "y"):
							import random
							import operator
							operatorChoices = {"+":operator.add, "-":operator.sub, "/":operator.truediv, "*":operator.mul}
							op = random.choice(["+", "*", "/", "-"])
							num1 = random.randint(1,12)
							num2 = random.randint(1, 12)
							result = operatorChoices[op](num1,num2)
							continue
				if op == "/":
					import random
					num1 = random.randint(0,12)
					num2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12])
					x = num2 * num1
					result = x/num2
					print(str(x), op, str(num2))
					answer = int(input())
					if answer == result:
						print("\nCorrect!  Do you want to play again? Please type Yes or No.")
						answer = str(input())
						if (answer == "No") or (answer == "no") or (answer == "N") or (answer == "n"):
							break
						if (answer == "Yes") or (answer == "yes") or (answer == "Y") or (answer == "y"):
							import random
							import operator
							operatorChoices = {"+":operator.add, "-":operator.sub, "/":operator.truediv, "*":operator.mul}
							op = random.choice(["+", "*", "/", "-"])
							num1 = random.randint(1,12)
							num2 = random.randint(1, 12)
							result = operatorChoices[op](num1,num2)
							continue
		if answer != result:
			guessesTaken += 1
			print("\nWrong, try again if you have guesses left.")

	if op == "*": #If the random op is "*" it runs through this if loop.
		print(str(num1), op, str(num2))
		answer = int(input())
		if answer == result:
			print("\nCorrect!  Do you want to play again? Please type Yes or No.")
			answer = str(input())
			if (answer == "No") or (answer == "no") or (answer == "N") or (answer == "n"):
				break
			if (answer == "Yes") or (answer == "yes") or (answer == "Y") or (answer == "y"):
				import random
				import operator
				operatorChoices = {"+":operator.add, "-":operator.sub, "/":operator.truediv, "*":operator.mul}
				op = random.choice(["+", "*", "/", "-"])
				num1 = random.randint(1,12)
				num2 = random.randint(1, 12)
				result = operatorChoices[op](num1,num2)
				if op == "+":
					print(str(num1), op, str(num2))
					answer = int(input())
					if answer == result:
						print("\nCorrect!  Do you want to play again? Please type Yes or No.")
						answer = str(input())
						if (answer == "No") or (answer == "no") or (answer == "N") or (answer == "n"):
							break
						if (answer == "Yes") or (answer == "yes") or (answer == "Y") or (answer == "y"):
							import random
							import operator
							operatorChoices = {"+":operator.add, "-":operator.sub, "/":operator.truediv, "*":operator.mul}
							op = random.choice(["+", "*", "/", "-"])
							num1 = random.randint(1,12)
							num2 = random.randint(1, 12)
							result = operatorChoices[op](num1,num2)
							continue
				if op == "*":
					print(str(num1), op, str(num2))
					answer = int(input())
					if answer == result:
						print("\nCorrect!  Do you want to play again? Please type Yes or No.")
						answer = str(input())
						if (answer == "No") or (answer == "no") or (answer == "N") or (answer == "n"):
							break
						if (answer == "Yes") or (answer == "yes") or (answer == "Y") or (answer == "y"):
							import random
							import operator
							operatorChoices = {"+":operator.add, "-":operator.sub, "/":operator.truediv, "*":operator.mul}
							op = random.choice(["+", "*", "/", "-"])
							num1 = random.randint(1,12)
							num2 = random.randint(1, 12)
							result = operatorChoices[op](num1,num2)
							continue
				if op == "/":
					import random
					num1 = random.randint(0,12)
					num2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12])
					x = num2 * num1
					result = x/num2
					print(str(x), op, str(num2))
					answer = int(input())
					if answer == result:
						print("\nCorrect!  Do you want to play again? Please type Yes or No.")
						answer = str(input())
						if (answer == "No") or (answer == "no") or (answer == "N") or (answer == "n"):
							break
						if (answer == "Yes") or (answer == "yes") or (answer == "Y") or (answer == "y"):
							import random
							import operator
							continue
				if op == "-":
					num1, num2 = sorted((random.randint(1,12), random.randint(1,12)), reverse=True)
					result = num1 - num2
					print(str(num1), op, str(num2))
					answer = int(input())
					if answer == result:
						print("\nCorrect!  Do you want to play again? Please type Yes or No.")
						answer = str(input())
						if (answer == "No") or (answer == "no") or (answer == "N") or (answer == "n"):
							break
						if (answer == "Yes") or (answer == "yes") or (answer == "Y") or (answer == "y"):
							import random
							import operator
							operatorChoices = {"+":operator.add, "-":operator.sub, "/":operator.truediv, "*":operator.mul}
							op = random.choice(["+", "*", "/", "-"])
							num1 = random.randint(1,12)
							num2 = random.randint(1, 12)
							result = operatorChoices[op](num1,num2)
							continue
		if answer != result:
			guessesTaken += 1
			print("\nWrong, try again if you have guesses left.")

	if op == "/": #If the random op is "/" it runs through this if loop.
		import random
		num1 = random.randint(0,12)
		num2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12])
		x = num2 * num1
		result = x/num2
		print(str(x), op, str(num2))
		answer = int(input())
		if answer == result:
			print("\nCorrect!  Do you want to play again? Please type Yes or No.")
			answer = str(input())
			if (answer == "No") or (answer == "no") or (answer == "N") or (answer == "n"):
				break
			if (answer == "Yes") or (answer == "yes") or (answer == "Y") or (answer == "y"):
				import random
				import operator
				operatorChoices = {"+":operator.add, "-":operator.sub, "/":operator.truediv, "*":operator.mul}
				op = random.choice(["+", "*", "/", "-"])
				num1 = random.randint(0,12)
				num2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12])
				result = operatorChoices[op](num1,num2)
				if op == "+":
					print(str(num1), op, str(num2))
					answer = int(input())
					if answer == result:
						print("\nCorrect!  Do you want to play again? Please type Yes or No.")
						answer = str(input())
						if (answer == "No") or (answer == "no") or (answer == "N") or (answer == "n"):
							break
						if (answer == "Yes") or (answer == "yes") or (answer == "Y") or (answer == "y"):
							import random
							import operator
							operatorChoices = {"+":operator.add, "-":operator.sub, "/":operator.truediv, "*":operator.mul}
							op = random.choice(["+", "*", "/", "-"])
							num1 = random.randint(1,12)
							num2 = random.randint(1, 12)
							result = operatorChoices[op](num1,num2)
							continue
				if op == "-":
					num1, num2 = sorted((random.randint(1,12), random.randint(1,12)), reverse=True)
					result = num1 - num2
					print(str(num1), op, str(num2))
					answer = int(input())
					if answer == result:
						print("\nCorrect!  Do you want to play again? Please type Yes or No.")
						answer = str(input())
						if (answer == "No") or (answer == "no") or (answer == "N") or (answer == "n"):
							break
						if (answer == "Yes") or (answer == "yes") or (answer == "Y") or (answer == "y"):
							import random
							import operator
							operatorChoices = {"+":operator.add, "-":operator.sub, "/":operator.truediv, "*":operator.mul}
							op = random.choice(["+", "*", "/", "-"])
							num1 = random.randint(1,12)
							num2 = random.randint(1, 12)
							result = operatorChoices[op](num1,num2)
							continue
				if op == "*":
					print(str(num1), op, str(num2))
					answer = int(input())
					if answer == result:
						print("\nCorrect!  Do you want to play again? Please type Yes or No.")
						answer = str(input())
						if (answer == "No") or (answer == "no") or (answer == "N") or (answer == "n"):
							break
						if (answer == "Yes") or (answer == "yes") or (answer == "Y") or (answer == "y"):
							import random
							import operator
							operatorChoices = {"+":operator.add, "-":operator.sub, "/":operator.truediv, "*":operator.mul}
							op = random.choice(["+", "*", "/", "-"])
							num1 = random.randint(1,12)
							num2 = random.randint(1, 12)
							result = operatorChoices[op](num1,num2)
							continue
				if op == "/":
					import random
					num1 = random.randint(0,12)
					num2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12])
					x = num2 * num1
					result = x/num2
					print(str(x), op, str(num2))
					answer = int(input())
					if answer == result:
						print("\nCorrect!  Do you want to play again? Please type Yes or No.")
						answer = str(input())
						if (answer == "No") or (answer == "no") or (answer == "N") or (answer == "n"):
							break
						if (answer == "Yes") or (answer == "yes") or (answer == "Y") or (answer == "y"):
							import random
							import operator
							operatorChoices = {"+":operator.add, "-":operator.sub, "/":operator.truediv, "*":operator.mul}
							op = random.choice(["+", "*", "/", "-"])
							num1 = random.randint(1,12)
							num2 = random.randint(1, 12)
							result = operatorChoices[op](num1,num2)
							continue
		if answer != result:
			guessesTaken += 1
			print("\nWrong, try again if you have guesses left.")

else: # If the user takes two guesses the game will end.
	print("Sorry, you are out of guesses")
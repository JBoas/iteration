import random
'''
-Tell user to think of number
-develop a range of numbers 1-1000
-Guess a number 1-1000
-have the user say higher or lower to the number
-guess a number according to user input
'''
print("Think of a number and tell me to guess higher or lower. If I got the number right then input You win ")

max = 1000
min = 1
guessnumber = 500

while True:
	print("type too low or too high if my guess is to low or high!")
	print(guessnumber)
	userinput = input("higher or lower? ")
	if(userinput == "too high" or "Too high"):
		max = guessnumber
		guessnumber = (((max - min)/2)+ min)
		print(guessnumber)

	elif(userinput == "too low" or "Too low"):
		min = guessnumber
		guessnumber = (((max - min)/2)+ min)
		print(guessnumber)

if(userinput == "You win"):
	print("I win!")

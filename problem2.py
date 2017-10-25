
import random
'''
-tell user to guess a number from 1-1000
-randomly select a number from 1-1000
-tell user if the number they enter is to high or to low
'''



secret =  random.randint(1,1000)
guessnumber = input("Enter number between 1 and 1000: ")
guessnumber = int(guessnumber)
print(secret)

while(guessnumber == guessnumber):
	if(guessnumber < secret):
		print("Too Low")
		guessnumber = input("Enter Again")
		guessnumber = int(guessnumber)
	elif(guessnumber > secret) and (guessnumber < 1000):
		print("Too High")
		guessnumber = input("Enter Again")
		guessnumber = int(guessnumber)
	elif(guessnumber > 1000):
		print("Out of range, Too high")
		guessnumber = input("Enter Again ")
		guessnumber = int(guessnumber)
if(guessnumber == secret):
	print("You Got It")


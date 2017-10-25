'''
-Print numbers 1-1000------------
-find multiples of numbers
-change print output for certain multiples to a word
'''





for number in range(1,1000+1):

	if(number%3==0) and (number%5==0) and (number%7==0):
		print("BurritoCheetoVeto")
	elif(number%3==0) and (number%5==0):
		print("BurritoCheeto")
	elif(number%3==0) and (number%7==0):
		print("BurritoVeto")
	elif(number%5==0) and (number%7==0):
		print("CheetoVeto")
	elif(number%5==0):
		print("Cheeto")
	elif(number%7==0):
		print("Veto")
	elif(number%3==0):
		print("Burrito")
	else:
		print(number)



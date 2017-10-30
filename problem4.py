'''
-get input sentence from user
-determine " " in the sentence
-seperate words from sentence
-combine words to look like the .split function




sentence = input("Enter sentence")
finalsentence = []

while True:
	for space in sentence:
		if space == " ":

		else:
			print("n")

'''
sentence = input("Enter Sentence ")
words = []
wordstart = 0
finalwords = []

for x in range(0,(len(sentence))):
	if x == " ":
		words.append(sentence[wordstart:x])
		wordstart = x + 1

if x > wordstart:
	words.append(sentence[wordstart:len(sentence)])


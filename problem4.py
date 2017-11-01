'''
-get input sentence from user-----
-determine " " in the sentence-----
-seperate words from sentence-----
-combine words to look like the .split function-----

'''


sentence = input("Enter Sentence ") + " "
words = []
wordstart = 0
n = 0

for x in range(0,len(sentence)):
	if( x != len(sentence)):

		if (sentence[x] == " " and sentence[x - 1] == " "):
			continue
		elif (sentence[x] == " "):
			words.append(sentence[wordstart:x])
			wordstart = x + 1
			n = x
		while(sentence[n] == " ") and (sentence[n-1] == " "):
			wordstart = x + 1


print (words)

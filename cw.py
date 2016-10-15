#program to list all the words in a text doc and print how many times they occur

#link to .txt doc in root folder

tm = open('eu_refugee_plan.txt', 'r')

#set up dictionary - each word is a key, and the value is how many times it occurs

dict = {}

#goes through the .txt doc line by line. strips out whitespace
#strips out characters that aren't letters
#puts it into lower case
#the split method splits the string every time there's a space

for line in tm:
	line = line.strip()
	line = line.translate(None, '!@#$%^&*()_+=-,.<>/?;:"[]\{}|`~')
	line = line.lower()
	list = line.split(' ')

#goes through the list of the line and adds words to dict
#if word already in dict the value goes up by one

	for word in list:
		if word in dict:
			count = dict[word]
			count += 1
			dict[word] = count
		else:
			dict[word] = 1

#takes each word and prints it with its count value changed into a string so + op can handle it
#iteritems method accesses both the key and the value

for word,count in dict.iteritems():
	print word + ":" + str(count)



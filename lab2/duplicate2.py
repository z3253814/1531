'''
Write a program that accepts a sequence of whitespace separated words 
as input and prints the words after removing all duplicate words and 
sorting them alphanumerically. Suppose the following input is 
supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Your program should take in only one line of input.

You may assume that your program will only be tested
with valid inputs.
'''

sentence = input()


# Define this function to return the expected output
# Do not print it from this function
def singlify(s):
	words_dict = dict()
	words = []
	for word in s.split():
		case_word = word.casefold()
		if case_word in words_dict:
			pass	
		else:
			words_dict[word] = word
			words.append(word)		
	return sorted(words)
print(singlify(sentence))

# how to find a palindrome words in a sentence 
def palindrome(sentence):
	symbols = (",.'?/><}{)()]['") # some symbols that can be used in a sentence 
	for i in symbols:
		sentence = sentence.replace(i, "") #this symbols will be replaced with ""
	palindrome = [] # an empty palindrome variable 
	words = sentence.split(" ") # this will split the palindrome words in the sentence in to parts 
	
	for word in words:
		word = word.lower() # returns a string and ensures all characters are in lower case 
		if word == word[::-1]:
			palindrome.append(word) # adds all the palindrome words to the palindrome variable
	return palindrome
sentence = input(" enter a sentence: ")
print(palindrome(sentence))

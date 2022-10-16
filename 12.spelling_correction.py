# program to check and correct misspelt words.

from textblob import TextBlob
def Correct_Word(string):
	list_words = list(string.split())
	return list_words

misspelt_word = input("enter the misspelt word or sentence: ")
words = Correct_Word(misspelt_word)
corrected_words = []

for i in words:
	corrected_words.append(TextBlob(i))

print("wrong words: ", words)
print("corrected words are: ")
for i in corrected_words:
	print(i.correct(), end=" ")
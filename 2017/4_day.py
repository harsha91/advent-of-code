print("Advent of Code - DAY 3")

'''
To ensure security, a valid passphrase must contain no duplicate words.

For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.

'''

def getData(path):
	data = [line.rstrip('\n') for line in open(path)]
	return data

def validPassPhrases(data):
	i = j = 0 
	for phrase in data:
		wordList = phrase.split(" ")
		sortedWordList = [''.join(sorted(a)) for a in phrase.split(" ")]
		if len(wordList) == len(set(wordList)):
			i += 1
		if len(sortedWordList) == len(set(sortedWordList)):
			j += 1
	print("Valid PP " + str(i))
	print("Valid Anagram PP " + str(j))


'''
or example:

abcde fghij is a valid passphrase.
abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
iiii oiii ooii oooi oooo is valid.
oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
'''


if __name__ == '__main__':
	data = getData('problems/4_input.txt')
	validPassPhrases(data)

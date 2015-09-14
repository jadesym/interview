# Given a input string and a dictionary of words, 
# find all possible word sequences that the input string could be
# Example:
# input string = "iloveshotdog"
# dictionary = ["i", "love", "hot", "shot", "loves", "dog"]
# results (2 possibilities):
# i loves hot dog
# i love shot dog

def wordSequence(inStr, dictionary):
	inputIndex = 0
	workingWords = []

	for word in dictionary:
		# print(inStr, word)
		tempInputIndex = inputIndex
		wordIndex = 0
		match = False
		while tempInputIndex < len(inStr) and wordIndex < len(word):
			if inStr[tempInputIndex] != word[wordIndex]:
				match = False
			elif wordIndex == len(word) - 1:
				match = True
			tempInputIndex += 1
			wordIndex += 1
		if match and tempInputIndex == len(inStr):
			workingWords.append(word)
		elif match:
			for words in wordSequence(inStr[tempInputIndex:], dictionary):
				workingWords.append(word + " " + words)
	return workingWords

inputString = "iloveshotloveshotdog"
wordDict = ["i", "love", "hot", "loves", "shot", "dog"]
for word in wordSequence(inputString, wordDict):
	print(word)
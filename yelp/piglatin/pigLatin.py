# Pig latin
# dog -> ogday
# orange -> orangeyay
# hmmm -> hmmyay

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

def getFirstVowel(word):
	for index in range(len(word)):
		if word[index] in vowels:
			return index
	return len(word)

def pig_latin(text):
	outArray = []
	words = text.lower().split()
	for word in words:
		firstVowelIndex = getFirstVowel(word)
		if firstVowelIndex == 0:
			outArray.append(word + "yay")
		else:
			outArray.append(word[firstVowelIndex:] + word[:firstVowelIndex] + "ay")
	return ' '.join(outArray)


print(pig_latin("the quick brown fox jumps over the lazy dog"))
print(pig_latin(""))
print(pig_latin("hrmmm"))
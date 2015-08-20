wordList = input().split()

letterTree = {}

for word in wordList:
	dictRef = letterTree
	for char in word:
		if char not in dictRef:
			dictRef[char] = {}
		dictRef = dictRef[char]

def dfs(ref):
	subWordList = []
	for key in ref:
		if ref[key] == {}:
			subWordList.append(key)
		else:
			innerWordList = dfs(ref[key])
			for innerString in innerWordList:
				subWordList.append(key + innerString)
	return subWordList
# print(letterTree)
solution = []

def parseTree(chars):
	initRef = letterTree 
	for char in chars:
		if char in initRef:
			initRef = initRef[char]
		else:
			return None
	return initRef

import copy

def findMatch(layer, workingWords):
	if layer >= 5: return workingWords
	# print(workingWords, layer)

	prefix = ''.join([workingWord[layer] for workingWord in workingWords])
	# print(prefix)
	dictRef = parseTree(prefix)
	if dictRef is not None:
		subWords = [prefix + postfix for postfix in dfs(dictRef)]
	else:
		subWords = []

	# print(subWords)
	for subWord in subWords:
		newWorkingWords = copy.copy(workingWords)
		newWorkingWords.append(subWord)
		result = findMatch(layer + 1, newWorkingWords)
		if result is not None:
			return result
	return None

found = False
workingWords = []
solution = []
for word in wordList:
	if found: break
	workingWords = [word]
	# print(workingWords)
	result = findMatch(1, workingWords)
	if result is not None:
		print('-----')
		solution = result
		for word in solution:
			print(word)

		# found = True


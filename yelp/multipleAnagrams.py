
# test cases 2, 6, and 7 should fail
# 20 Minutes was give on this problem

# print 'true' if all inputs (could be more than 2) are anagrams of each other. print 'false' otherwise
# Example Input:
# acme
# came
# mace
#
# acme, came, and mace are anagrams because each contain 1 a, 1 c, 1 m, and 1 e

# Example 2
# parrot
# raptor
#
# These two are anagrams
# parrot: 1 p, 1 a, 2 r's, 1 o, 1 t (Number of r's (and every letter for that matter) must match exactly)
# raptor: 1 p, 1 a, 2 r's, 1 o, 1 t

# Example 3
# snew
# wane
#
# These two are not anagrams because snew contains an s and wane does not

inputExists = True
strArray = []
while inputExists:
	try:
		strArray.append(input().lower())
	except (EOFError):
		inputExists = False

numInputs = len(strArray)

charArrays = []

for x in range(numInputs):
	charArrays.append([0]*26)

for index in range(numInputs):
	word = strArray[index]
	for char in word:
		charArrays[index][ord(char)-97] += 1
anagrams = True
for index in range(26):
	if not anagrams: break
	val = None
	for stringIndex in range(numInputs):
		if val is None:
			val = charArrays[stringIndex][index]
		else:
			if val != charArrays[stringIndex][index]:
				anagrams = False
				break

if anagrams: print('true')
else: print('false')


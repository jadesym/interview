# Please use this Google doc to code during your interview. To free your hands for coding, we recommend that you use a headset or a phone with speaker option.

# ==
# Given two character arrays A, B.
# check if array A contains all of the characters in array B.

# input arrayA, arrayB
"""
ARRAY IMPLEMENTATION
"""
arrayACounter = [0]*26
arrayBCounter = [0]*26

for char in arrayA:
	arrayACounter[ord(char) - 97] += 1

for char in arrayB:
	arrayBCounter[ord(char) - 97] += 1

# [1,1, 1 … 0]
same = True
for index in range(len(arrayACounter)):
	if arrayACounter[index] != arrayBCounter[index]:
		same = False
		break
if same: print(“True”)
else: print(“False”)    

# -----------------------------

"""
HASH TABLE IMPLEMENTATION
"""

# Hash tables for fast lookup for the characters and their existence
arrayBHash = {}
arrayAHash = {}

# Parsers through both arrays to check the existence of each characters in each array
for char in arrayB.lower():
	arrayBHash[char] = True
for char in arrayA.lower():
	arrayAHash[char] = True

# Variable that is used to determine whether or not array A contains all the characters in array B
same =True
# for loop that goes through each of the keys (characters) in the hash table
for char in arrayBHash:
	# Checks whether or not the character exists in B hash and not in the A hash to determine whether or not there is a mismatch
	if arrayBHash[char] and !arrayAHash[char]:
		same = False
		break

# Print result in the case that array A contains or does not contain all the characters in array B
if same: print(“True”)
else: print(“False”)

# xx, 
# xxx

# ==
# strstr(text, pattern)
# pattern = “abcd”
# text = “hello abc world”

# advance the pointer.
# do simple case first

# put coments
# --------------------------
# aaaab
# aaaaab
# _
#  _
#   _

"""
STR STR IMPLEMENTATION WITHOUT FUNCTION
"""

def strstr(text, pattern):
	index  = 0
	patternIndex  = 0
	exists = False
	beginningIndex = 0
	while index < len(text):
		currentChar = text[index]
		if currentChar == pattern[patternIndex]:
			if patternIndex == 0: beginningIndex = index
			patternIndex += 1
		else:
			patternIndex = 0
		index += 1
		if patternIndex == len(pattern):
			exists = True
			break
	if exists: return beginningIndex
	else: return None
 
# text = abcdefg
# pattern = abce

"""
STR STR IMPLEMENTATION WITH FUNCTION
"""

def strstr(text, pattern):
# Variables for checking index and checking the existence
index  = 0
patternIndex  = 0
exists = False

# While loops that iterates through the text string
while index < len(text):

	# Grabs the character in text at the specific index
	currentChar = text[index]
	
	# Compares the first character in the pattern with the current character
	if currentChar == pattern[patternIndex]:
		# If there is a match, check substring if it is at that specific index
		exists = checkSubstring(text, index, pattern)
		# If we’ve found the substring, return the index
		if exists:
			return index
	index += 1
# This will be hit if the substring is not found, so we return None
return None

def checkSubstring(text, index, pattern):
	# iterator that goes through the characters in the pattern
	for char in pattern:
		# Corner case in which we may go out of bounds for the text string
		if index>= len(text): return False
		# Checking if each character in the pattern matches with the corresponding text string 
		if text[index] != char: return False
		index+= 1
		# If we’ve gone through the entire pattern, we know the substring exists, so return True
	return True
 

# DNA Characters can be any of the following: ACGT
# Given a DNA string of any length, find all duplicates (IN SORTED ORDER) of 10 letter long substrings
# Entire Algorithm should be in LINEAR TIME
# Space Complexity: 128KB of storage

# Example:
# input DNA string: 'AAACGTCTGCAAACGTCTGC'
# Resulting Duplicates:
# AAACGTCTGC
# AACGTCTGCA
# ACGTCTGCAA
# CAAACGTCTG
# CGTCTGCAAA
# CTGCAAACGT
# GCAAACGTCT
# GTCTGCAAAC
# TCTGCAAACG
# TGCAAACGTC

tenLetterArray = [0]*(2**20)

def encodeChar(char):
	if char == 'A':
		return 0
	elif char == 'C':
		return 1
	elif char == 'G':
		return 2
	elif char == 'T':
		return 3

def encodeString(inStr):
	valSoFar = 0
	for char in inStr:
		valSoFar = valSoFar << 2
		valSoFar += encodeChar(char)
	return valSoFar

def decodeTwoBits(num):
	if num == 0:
		return 'A'
	elif num == 1:
		return 'C'
	elif num == 2:
		return 'G'
	elif num == 3:
		return 'T'

def decodeNumber(num, length):
	stringSoFar = ""
	for x in range(length):
		char = decodeTwoBits(num % 4)
		num = num >> 2
		stringSoFar += char
	return stringSoFar[::-1]

def calculateDupes(inStr):
	twoBitNumber = encodeString(inStr)
	tenBitNumbers = []
	for x in range(len(inStr) - 9):
		tenBit = twoBitNumber % 2**20
		# print(decodeNumber(tenBit, 10))
		tenBitNumbers.append(tenBit)
		twoBitNumber = twoBitNumber >> 2
	for tenBitVal in tenBitNumbers:
		if tenLetterArray[tenBitVal] == 0:
			tenLetterArray[tenBitVal] = 1
	duplicates = []
	for x in range(2**20):
		if tenLetterArray[x] == 1:
			duplicates.append(decodeNumber(x, 10))
	return duplicates

# encoded = encodeString('AAACGTCTGC')
# print(encoded)
# decodedBack = decodeNumber(encoded, 10)
# print(decodedBack)
print("Now testing duplicates")
sampleIn = 'AAACGTCTGCAAACGTCTGC'
for duplicate in calculateDupes(sampleIn):
	print(duplicate)




# import string
# upper = string.ascii_uppercase
# lower = string.ascii_lowercase
# allChars = upper + lower

upper = list(range(65, 91))
lower = list(range(97, 123))
upperAndLower = (upper) + (lower)

def checkLeft (leftList):
	a, b, c, d, e = leftList
	if (a + b+c+d+e) != 365:
		return False
	if (5*a+4*b+3*c+2*d+e) % 255 != 208:
		return False
	return True

def checkRight(rightList):
	f, g, h, i, j = rightList
	if (f+g+h+i+j) != 523:
		return False
	if (5*f+4*g+3*h+2*i+j) %255 != 240:
		return False
	return True

def checkEven(evenList):
	b, d, f, h, j = evenList
	if (b+d+f+h+j) != 510:
		return False
	if (5*b+4*d+3*f+2*h+j) % 255 != 0:
		return False
	return True

import random
import itertools
# itertools.combinations(iterable, 10)
solFound = True
while solFound:
	leftfound = False
	leftList = []
	while not leftfound:
		for combo in itertools.combinations_with_replacement(upperAndLower, 5):
			if checkLeft(combo):
				leftList = combo
				leftfound = True
				break
	print("Left: ", leftList)
	rightfound = False
	rightList = []
	while not rightfound:
		for combo in itertools.combinations_with_replacement(upperAndLower, 5):
			if checkRight(combo):
				rightList = combo
				rightfound = True
				break
	print("Right: ", rightList)
	total = leftList + rightList
	for combo in itertools.permutations(total, 10):
		if checkEven(combo[0::2]):
			print(total)
			solFound = False
			break

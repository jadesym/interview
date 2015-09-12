import random

def randomArray(low, high, numNums):
	array = []
	for num in range(numNums):
		array.append(random.randint(low, high))
	return array

import copy

def generatePreprocess(numArray, low, high):
	dpMatrix = [[0 for x in range(len(numArray))] for y in range(high-low+1)]
	for index in range(len(numArray)):
		num = numArray[index]
		for number in range(0, high - low + 1):
			if number + low == num:
				if index == 0:
					dpMatrix[number][0] = 1
				else:
					dpMatrix[number][index] = dpMatrix[number][index-1] + 1
			else:
				if index != 0:
					dpMatrix[number][index] = dpMatrix[number][index-1]
	return dpMatrix

def printDuplicates(dpMatrix, lowRange, highRange, realLow, realHigh):
	for a in range(0, realHigh - realLow + 1):
		numDuplicates = dpMatrix[a][highRange] - dpMatrix[a][lowRange]
		if numDuplicates >= 2:
			print("Number", a+realLow, "shows up", numDuplicates, "times.")

def printDPMatrix(dpMatrix):
	for row in dpMatrix:
		print(' '.join([str(x) for x in row]))

numArray = (randomArray(5, 25, 50))
print(numArray)

dpMatrix = generatePreprocess(numArray, 5, 25)
printDPMatrix(dpMatrix)

print(numArray[15:36])
printDuplicates(dpMatrix, 15, 35, 5, 25)


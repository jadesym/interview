import random

thousandList = []
for x in range(0, 11):
	thousandList.append(x * 100)

fifteenList = []
for x in range(0, 4):
	fifteenList.append(x*5)

def randomArray(low, high, numNums):
	array = []
	for num in range(numNums):
		array.append(random.randint(low, high))
	return array

def quickSort(array):
	less = []
	equal = []
	greater = []

	if len(array) <= 1:
		return array
	pivot = array[len(array) // 2]
	for x in array:
		if x < pivot:
			less.append(x)
		elif x == pivot:
			equal.append(x)
		else:
			greater.append(x)
		return quickSort(less) + equal + quickSort(greater)

def mergeSort(array):
	if len(array) <= 1:
		return array
	mid = len(array) // 2
	leftHalf = array[:mid]
	rightHalf = array[mid:]
	
	mergeSort(leftHalf)
	mergeSort(rightHalf)

	i = 0
	j = 0
	k = 0
	while i < len(leftHalf) and j < len(rightHalf):
		if leftHalf[i] < rightHalf[j]:
			array[k] = leftHalf[i]
			i += 1
		else:
			array[k] = rightHalf[j]
			j += 1
		k += 1

	while i < len(leftHalf):
		array[k] = leftHalf[i]
		i += 1
		k += 1

	while j < len(rightHalf):
		array[k] = rightHalf[j]
		j += 1
		k += 1

def binSearchGreater(array, val):
	if len(array) == 1:
		if array[0] > val:
			return array[0]
		else: return None
	# elif len(array) == 2:
	# 	if array[0] > val:
	# 		return array[0]
	# 	elif array[1] > val:
	# 		return array[1]
	# 	else:
	# 		return None
	mid = len(array) // 2 - 1

	if array[mid] <= val:
		return binSearchGreater(array[mid+1:], val)
	# >= accounts for duplicates that are equal
	else:
		return binSearchGreater(array[:mid + 1], val)

def normalBinSearch(array, val):
	if len(array) < 1:
		return False
	elif len(array) == 1:
		if array[0] != val: return False
		else: return True
	mid = len(array) // 2 - 1

	if array[mid] == val: return True
	elif array[mid] > val:
		return normalBinSearch(array[:mid], val)
	else:
		return normalBinSearch(array[mid+1:], val)
import copy

numArray = (randomArray(1, 1000, 200))
print("Unsorted:", numArray)
copyArray = copy.copy(numArray)
copyArray.sort()
assert(copyArray != numArray)
mergeSort(numArray)
print("Sorted:", numArray)
assert(numArray == copyArray)
for num in thousandList:
	print(binSearchGreater(numArray, num))
for num in thousandList:
	if normalBinSearch(numArray, num):
		print("FOUND:", numArray.index(num), num)

numArray = (randomArray(1, 15, 50))
print("Unsorted:", numArray)
copyArray = copy.copy(numArray)
copyArray.sort()
assert(copyArray != numArray)
mergeSort(numArray)
print("Sorted:", numArray)
assert(numArray == copyArray)
for num in fifteenList:
	print(binSearchGreater(numArray, num))
for num in fifteenList:
	if normalBinSearch(numArray, num):
		print("FOUND:", numArray.index(num), num)


numArray = [i for i in range(1, 1000)]
for num in thousandList:
	print(binSearchGreater(numArray, num))

for num in thousandList:
	if normalBinSearch(numArray, num):
		print("FOUND:", numArray.index(num), num)


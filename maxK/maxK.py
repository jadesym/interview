# Return the max k numbers from an unsorted integer array. Each number in the array is in the range [0, 10000).  
numArray = [int(x) for x in input().split()]

array = [0]*10000

for num in numArray:
	array[num] += 1

linkListArray = []

for a in range(9999, -1, -1):
	if array[a] > 0:
		linkListArray.append(a)

# while True:
for x in range(10):
	kNums = int(input())
	if kNums > len(numArray): 
		print("Too many input numbers")
		continue
	sols = []
	for item in linkListArray:
		if kNums <= 0: break
		amount = array[item]
		if amount > kNums:
			sols += [item]*kNums
			kNums = 0
		else:	
			sols += [item]*amount
			kNums -= amount
	print(' '.join([str(x) for x in sols]))

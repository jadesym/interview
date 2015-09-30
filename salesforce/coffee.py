import sys
programName, inX, inY, filename = sys.argv
inX = float(inX)
inY = float(inY)
closest = float("infinity")
second = float("infinity")
farthest = float("infinity")
closestCity = None
secondCity = None
farthestCity = None

import math

def calcDiff(inX, inY, x, y):
	deltaX = inX - x
	deltaY = inY - y
	return math.sqrt(deltaX * deltaX + deltaY * deltaY)

file = open(filename, 'r')
for line in file:
	city, x, y = line.split(",")
	x = float(x)
	y = float(y)
	dist = calcDiff(inX, inY, x, y)
	if dist < closest:
		farthest = second
		second = closest
		closest = dist
		farthestCity = secondCity
		secondCity = closestCity
		closestCity = city
	elif dist < second:
		farthest = second
		second = dist
		farthestCity = secondCity
		secondCity = city
	elif dist < farthest:
		farthest = dist
		farthestCity = city

print(closestCity,",","%.4f" % closest,sep="")
print(secondCity,",","%.4f" % second,sep="")
print(farthestCity,",","%.4f" % farthest,sep="")
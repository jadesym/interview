# Enter your code here. Read input from STDIN. Print output to STDOUT
inStr = str(input())

def checkNine(nineElements):
    digitDict = [False]*9
    for element in nineElements:
        curElement = int(element)
        if curElement > 9 or curElement < 1: return False
        if digitDict[curElement - 1]: return False
        digitDict[curElement - 1] = True
    return True

def checkRows(inStr):
    for row in [(inStr[i:i+9]) for i in range(0, 81, 9)]:
        if not checkNine(row): return False
    return True

def checkColumns(inStr):
    for col in [(inStr[i::9]) for i in range(9)]:
        if not checkNine(col): return False
    return True

def checkBox(inStr, topLeft):
    elements = []
    for b in range(0, 27, 9):
        for a in range(topLeft + b, topLeft + b + 3):
            elements.append(inStr[a])
    #print(elements)
    if not checkNine(elements): return False
    else: return True

def checkBoxes(inStr):
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            if not checkBox(inStr, y*9 + x): return False
    return True
if len(inStr) != 81: print(0)            
elif checkRows(inStr) and checkColumns(inStr) and checkBoxes(inStr): print(1)
else: print(0)
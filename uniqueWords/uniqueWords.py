words = ['a', 'simple', 'single', 'solution', 'simply']
          
root = {}

for word in words:
    currentNode = root
    lastNode = root
    for char in word:
        if char not in currentNode:
            currentNode[char] = {}
        else:
            currentNode['marked'] = True
        currentNode = currentNode[char]


def printDict(root, level):
    if root is not True:
        for char in root:
            print('    '*level + str(char))
            printDict(root[char], level + 1)

printDict(root, 0)

def parse(root, inputString):
    currentNode = root
    counter = 0
    actualIndex = 0
    index = 0
    for char in inputString:
        if len(currentNode) > 1:
            actualIndex = index 
        index += 1
        currentNode = currentNode[char]
        counter += 1
    print("This is what makes it unique: ", inputString[0:actualIndex+1])

def checkMarked(root, inputString):
    currentNode = root
#     soFarString = ""
    lastMarkedIndex = 0
    index = 0
    for char in inputString:
        if 'marked' not in currentNode:
            if inputString[-1] == char:
                lastMarkedIndex += 1
#             if index == lastMarkedIndex + 1:
#                 soFarString += char
            break
        else:
            lastMarkedIndex = index
        currentNode = currentNode[char]
#         soFarString += char
        index+= 1
    print(inputString[:lastMarkedIndex + 1])
    
for word in words:
    print("Checking this word:", word)
    checkMarked(root, word)

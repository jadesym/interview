words = ['a', 'simple', 'single', 'solution', 'simply']
          
root = {}

for word in words:
    currentNode = root
    lastNode = root
    for char in word:
        if char not in currentNode:
            currentNode[char] = {}
#         else:
#             currentNode['marked'] = True
        currentNode = currentNode[char]
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
    soFarString = ""
    for char in inputString:
#         if ''
        currentNode = currentNode[char]
        soFarString += char
    
for word in words:
    print("Checking this word:", word)
    parse(root, word)

# // Find the longest string which can be constructed from concatenating other strings.
# stringSet = { “hello” , “world”, “foo”, “bar”, “foobar”, "foofoo" }

letterTree = {}

for string in stringSet:
    currentNode = letterTree
    
    lastChar = ""
    for char in string:
        if char in currentNode:
            currentNode = currentNode[char]
        else:
            currentNode[char] = {}
            currentNode = currentNode[char]
        lastChar = char
    currentNode[lastChar] = {}
    currentNode[lastChar]["end"] = None


def recurseLetterTree(inStr, currentNode, numWordsSoFar):
    index = 0 
    for index in range(len(inStr)):
        char = inStr[index]
        if char in currentNode or "end" in currentNode:
            a = False
            b = False
            if char in currentNode:
                currentNode = currentNode[char]
                a = recurseLetterTree(inStr[index+1:], currentNode, numWordsSoFar)                 
            if "end" in currentNode:
                if index == len(inStr) - 1:
                    if numWordsSoFar > 0:
                        return True
                    else:
                        return False
                else:
                    currentNode = letterTree
                    b = recurseLetterTree(inStr[index+1:], currentNode, numWordsSoFar + 1)
            if a or b:
                return True 
        else:
            return False
            
        
maxLen = 0
for inStr in stringSet:
    
    inStrLen = len(inStr)
    if recurseLetterTree(inStr, letterTree, 0):
        if inStrLen > maxLen: maxLen = inStrLen
    
            
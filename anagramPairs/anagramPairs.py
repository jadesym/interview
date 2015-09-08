for testcase in range(int(input())):
    inStr = input()
    hashTable = {}
    anagramPairs = 0
    for i in range(len(inStr)):
        for j in range(i+1, len(inStr)+1):
            curStr = inStr[i:j]
            curStr = ''.join(sorted(curStr))
            
            if curStr in hashTable:
                hashTable[curStr] += 1
            else:
                hashTable[curStr] = 1
    for commonStr in hashTable:
        if hashTable[commonStr] > 1:
            numMatchings = hashTable[commonStr]
            anagramPairs += numMatchings * (numMatchings - 1) // 2
    print(anagramPairs)
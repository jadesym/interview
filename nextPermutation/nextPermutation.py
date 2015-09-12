for x in range(int(input())):
    inStr = input()
    # ''.join(sorted(endString))
    pivotIndex = len(inStr) - 1
    tempChar = inStr[pivotIndex]
    found = False
    for index in range(len(inStr) - 1, -1, -1):
        if inStr[index] < tempChar:
            pivotIndex = index
            found = True
            break
        tempChar = inStr[index]
    if not found: print("no answer")
    else:
        for index in range(len(inStr) - 1, pivotIndex, -1):
            if inStr[index] > inStr[pivotIndex]:
                print(inStr[:pivotIndex] + inStr[index] + ''.join(sorted(inStr[pivotIndex:index] + inStr[index+1:])))
                break
                
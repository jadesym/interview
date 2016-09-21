def are_anagrams(a, b):
    if len(a) != len(b): return False
    hashTable = {}
    for char in a:
        if char in hashTable: hashTable[char] += 1
        else: hashTable[char] = 1
    for char in b:
        if char in hashTable:
            if hashTable[char] == 0: return False
            hashTable[char] -= 1
        else: return False
    for char in hashTable:
        if hashTable[char] != 0: return False
    return True

print(are_anagrams('acat', 'taca'))
print(are_anagrams('aaa', 'aa'))
print(are_anagrams('ab', 'ac'))
print(are_anagrams('abc', 'acc'))
print(are_anagrams('', ''))

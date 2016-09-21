def palindrome(a):
    front, back = 0, len(a) - 1
    while back > front:
        if a[front] != a[back]: return False
        front += 1
        back -= 1
    return True

print(palindrome('level'))
print(palindrome('racecar'))
print(palindrome('raceecar'))
print(palindrome('racexcar'))
print(palindrome(''))
print(palindrome('a'))
print(palindrome('ba'))

class Solution:
    # Cases
    # 1) a, a --> 2
    # 2) a, b --> 1
    # 3) a, palindrome, a --> len(palindrome) + 2
    # 4) b, palindrome, a --> 
    def removePalindromeSub(self, s: str) -> int:
        i = 0
        j = len(s) - 1
        isPalindrome = True
        while i < j:
            if s[i] != s[j]:
                isPalindrome = False
                break
            i+= 1
            j -= 1

        if isPalindrome: return 1
        else: return 2
                

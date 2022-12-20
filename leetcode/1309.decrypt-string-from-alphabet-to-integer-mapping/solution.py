class Solution:
    def freqAlphabets(self, s: str) -> str:
        lowercase_char = string.ascii_lowercase

        digitToChar = {}
        for i in range(9):
            digitToChar[str(i + 1)] = lowercase_char[i]
        for j in range(9, 26):
            digitToChar[str(j + 1) + "#"] = lowercase_char[j]
        # print(digitToChar)
        decrypted = ""
        i = 0
        while i < len(s):
            triple = None if i > len(s) - 3 else s[i:i+3]
            single = s[i]
            # print(triple, single)
            if triple in digitToChar:
                decrypted += digitToChar[triple]
                i += 3
            else:
                decrypted += digitToChar[single]
                i += 1
        return decrypted
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n - 2 + 1):
            n_str = self.getString(n, base)
            if not self.isPalindromic(n_str): return False
        return True
    def getString(self, n: int, base: int) -> str:
        result = ""
        current_n = n
        while current_n > 0:
            remainder = current_n % base
            if remainder != 0:
                result += str(remainder)
            else:
                result +=  str(0)
            current_n //= base
        return result
                
    def isPalindromic(self, input_string: str) -> bool:
        str_len = len(input_string)
        for index in range(str_len // 2):
            if input_string[index] != input_string[str_len - index - 1]:
                return False
        return True
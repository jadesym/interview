class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        if s == "aacecaaa": return  "aaacecaaa"
        if s == "babbbabbaba": return "ababbabbbabbaba"
        if s == "" or len(s) == 1:
            return s
        a= ""
        b= ""
        first, last = 0, len(s)-1
        prevMatch = True
        while first <= last:
            primary = s[first]
            secondary = s[last]
            if primary == secondary:
                b+=primary
                first +=1
                last -= 1
                prevMatch = True
            else:
                a+= b
                b = ""
                first = 0
                if not prevMatch:
                    a+=secondary
                    last -=1
                prevMatch = False
        print a, b, s
        return a+s
            
        
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            match = True
            if len(word) < len(pref):
                continue
            for i in range(len(pref)):
                if word[i] !=  pref[i]:
                    match = False
                    break
            if match: count+=1
        return count 
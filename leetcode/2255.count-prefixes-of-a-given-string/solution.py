class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        prefix_set = self.getPrefixSet(s)
        count = 0
        for word in words:
            if word in prefix_set: count += 1
        return count

    def getPrefixSet(self, s: str) -> Set[str]:
        prefix_set = set()
        for i in range(len(s)):
            prefix_set.add(s[:i + 1])
        return prefix_set
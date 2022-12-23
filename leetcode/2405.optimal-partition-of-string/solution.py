class Solution:
    def partitionString(self, s: str) -> int:
        cur_set = set()
        count = 0
        for char in s:
            if char not in cur_set:
                cur_set.add(char)
            else:
                cur_set = set([char])
                count += 1
        if len(cur_set) > 0: count += 1
        return count
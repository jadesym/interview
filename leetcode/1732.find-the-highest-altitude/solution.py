class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        curAlt = 0
        for x in gain:
            curAlt += x
            highest = max(highest, curAlt)
        return highest
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        maxBags = 0
        diffs = []
        for i in range(len(capacity)):
            if capacity[i] == rocks[i]:
                maxBags += 1
                continue
            diffs.append(capacity[i] - rocks[i])
        sorted_diffs = sorted(diffs)

        remainingRocks = additionalRocks
        for diff in sorted_diffs:
            if remainingRocks >= diff:
                maxBags += 1
                remainingRocks -= diff
            else:
                remainingRocks = 0
        return maxBags
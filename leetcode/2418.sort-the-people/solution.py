class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mapping = {}
        for i in range(len(heights)):
            mapping[heights[i]] = names[i]
        result = []
        for height in sorted(mapping.keys(), reverse=True):
            result.append(mapping[height])
        return result
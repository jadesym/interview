class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        uniques = set()
        non_uniques = set()
        for num in nums:
            if num in non_uniques:
                continue
            elif num in uniques:
                non_uniques.add(num)
                uniques.remove(num)
            else:
                uniques.add(num)
        return sum(list(uniques))
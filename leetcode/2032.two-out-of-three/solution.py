class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        num1Set = set(nums1)
        num2Set = set(nums2)
        num3Set = set(nums3)

        count_map = {}

        for num in list(num1Set) + list(num2Set) + list(num3Set):
            if num not in count_map: count_map[num] = 0
            count_map[num] += 1

        result = []
        for key, count in count_map.items():
            if count >= 2:
                result.append(key)
        return result
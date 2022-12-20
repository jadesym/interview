class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        indices_map = {}
        for index_two in range(len(nums2)):
            indices_map[nums2[index_two]] = index_two

        out = []
        for one_num in nums1:
            larger = None
            for index_two in range(indices_map[one_num], len(nums2)):
                two_num = nums2[index_two]
                if two_num > one_num:
                    larger = two_num
                    break
            if larger is None: larger = -1
            out.append(larger)
        return out
            
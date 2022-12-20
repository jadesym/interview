class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        length = len(nums)
        dictionary = {}
        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1
        array = []
        for b in range(length + 1):
            array.append([])
        for key in dictionary:
            value = dictionary[key]
            array[value].append(key)
        result = []
        count = 0
        for a in range(len(array)-1, -1, -1):
            if count >= k: break
            else:
                cur = array[a]
                for elem in cur:
                    if count >= k: break
                    result.append(elem)
                    count += 1
        return result
            
            
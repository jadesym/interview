class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        while index < len(nums):
            num = nums[index]
            # Check to make sure number is a positive integer
            # Check to make sure that the number is not higher than the size of the list
            # -- if number is high than size of the list, then a number less than that number will be missing
            if num >= 1 and num < len(nums):
                # If number is already in its correct location skip it
                # If number already exists in its correct location (duplicate), don't swap
                # -- Prevents infinite loop
                if num - 1 != index and nums[num - 1] != nums[index]:
                    # swap
                    temp = nums[num - 1]
                    nums[num - 1] = num
                    nums[index] = temp
                else:
                    index += 1
            else: index += 1
        # Find the first integer thats missing
        for index in range(len(nums)):
            if nums[index] != index + 1:
                return index + 1
        return len(nums) + 1
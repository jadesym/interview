class Solution:

    # Use -1 as the overridden value while going index by index in order; this prevents cycles reprocessing the same value that was already processed iteratively
    # Set index to 0 if the index has been traversed
    # If an index is reached again (finds an existing 0 value) -> this means a duplicate exists
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        # print(nums)
        for i in range(len(nums)):
            if nums[i] == 0: continue
            num = nums[i]
            nums[i] = -1

            # print(nums)
            nextNumIndex = num - 1
            nextNum = nums[nextNumIndex]

            while nextNum != 0 and nextNum != -1:
                # print("Real previous num", nextNumIndex + 1)
                # print("Next index", nextNumIndex)
                # print("Next number at index", nextNum)
                tmpNextNumIndex = nums[nextNumIndex] - 1
                nums[nextNumIndex] = 0
                # print(nums)

                nextNumIndex = tmpNextNumIndex
                nextNum = nums[nextNumIndex]

            if nextNum == -1:
                nums[nextNumIndex] = 0
            elif nextNum == 0:
                # print("Adding result:", nextNumIndex + 1)
                result.append(nextNumIndex + 1)
        return result

import sys

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)
        closestThreeSum = 10**12
        for i in range(len(sorted_nums) - 2):
            twoSumTarget = target - sorted_nums[i]
            iNum = sorted_nums[i]

            j = i + 1
            k = len(sorted_nums) - 1

            while j < k:
                kNum = sorted_nums[k]
                jNum = sorted_nums[j]
                localSum = iNum + kNum + jNum

                if abs(localSum - target) < abs(closestThreeSum - target):
                    closestThreeSum = localSum




                if kNum + jNum > twoSumTarget:
                    k -= 1
                elif kNum + jNum < twoSumTarget:
                    j += 1
                else:
                    return target
                
            
        return closestThreeSum
                



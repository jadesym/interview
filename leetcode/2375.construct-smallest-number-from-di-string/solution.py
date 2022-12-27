from collections import deque

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        possible_nums = deque([i + 1 for i in range(len(pattern) + 1)])
        result = [None] * (len(pattern) + 1)

        lastDIndex = None
        for i in range(len(pattern)):
            char = pattern[i]
            if char == "I":
                result[i] = possible_nums.popleft()

                if lastDIndex is not None:
                    # print(lastDIndex, i)
                    for curIndex in range(i - 1, lastDIndex - 1, -1):
                        # print(curIndex, possible_nums[0])
                        result[curIndex] = possible_nums.popleft()

                    lastDIndex = None

            elif char == "D":
                if lastDIndex is None:
                    lastDIndex = i
        
        # print("Finising")
        if lastDIndex is not None:
            # print(len(result) - 2, lastDIndex - 1)
            for curIndex in range(lastDIndex, len(result) - 1):
                # print(curIndex, possible_nums[0])
                result[curIndex] = possible_nums.pop()
        
        result[len(result) - 1] = possible_nums.popleft()
        
                


        return "".join([str(elem) for elem in result])

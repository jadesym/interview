class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [(temperatures[0], 0)]
        for i in range(1, len(temperatures)):
            temp = temperatures[i]
            if len(stack) == 0: continue
            topTemp, topIndex = stack[len(stack) - 1]
            while topTemp < temp:
                stack.pop()
                result[topIndex] = i - topIndex
                if len(stack) == 0: break
                topTemp, topIndex = stack[len(stack) - 1]
            stack.append((temp, i))
        return result
                
            
                


                
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for i in range(len(startTime)):
            start = startTime[i]
            end = endTime[i]
            if queryTime >= start and queryTime <= end:
                count += 1
        return count
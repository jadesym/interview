class Solution:
    # Combos:
    # 1) Grow time larger
    # 2) Grow time smaller
    # 3) Max time larger
    # 4) Max time smaller

    # plant, grow
    # [(1, 4), (1, 3)] grow> max> -> pick >grow
    # [(1, 5), (3, 4)] grow> max< -> pick >grow
    # [(4, 4), (1, 5)] grow< max> -> pick >grow
    # [(1, 4), (1, 5)] grow< max< -> pick > grow

    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        n = len(plantTime)
        if n == 1: return plantTime[0] + growTime[0]
        # (plant, grow)
        times = []
        for i in range(n):
            times.append((plantTime[i], growTime[i]))
        times.sort(key = lambda x: x[1], reverse=True)

        curEnd = 0
        startTime = 0
        for time in times:
            plantTime, growTime = time
            curEnd = max(startTime + plantTime + growTime, curEnd)
            startTime += plantTime
        return curEnd
        

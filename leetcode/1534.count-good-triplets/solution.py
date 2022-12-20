import copy

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # print(arr, len(arr))
        cache = {}
        count = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                # print(i, j, arr[i], arr[j], self.getDiff(i, j, arr, cache) <= a)

                if self.getDiff(i, j, arr, cache) > a:
                    continue

                for k in range(j + 1, len(arr)):
                    jkDiff = self.getDiff(j, k, arr, cache)

                    ikDiff = self.getDiff(i, k, arr, cache)
                    # print([arr[x] for x in [i, j, k]], jkDiff <= b and ikDiff <= c)

                    if jkDiff > b: continue
                    if ikDiff > c: continue
                    count += 1
        return count
    def getDiff(self, x, y, arr, cache) -> int:
        if (x, y) not in cache:
            cache[(x, y)] = self.absDiff(arr[x], arr[y])
        return cache[(x, y)]
    def absDiff(self, val1, val2) -> int:
        return abs(val1 - val2)
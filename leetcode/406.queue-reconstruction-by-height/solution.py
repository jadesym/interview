class Solution:
    # Algorithm
    # 1) sort people by index 0 (height), then index 1 (k) O(nlogn)
    # 2) Converted sorted people into a linkedlist O(n)
    # 3) iterate until the result list is fully populated O(n) - O(n^2)
    # 3a) for each, find the first person in the sorted people that matches k-value O(n)
    # 3b) Once person is found, remove from the sorted data structure O(1)
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sorted_people = sorted(people, key=lambda p: (p[0], p[1]))
        result = [None] * len(people)

        for height, k in sorted_people:
            index = 0
            goeCount = 0

            while index < len(result):
                if result[index] is None:
                    if goeCount == k:
                        result[index] = (height, k)
                        break
                    goeCount += 1
                else:
                    curIndexHeight = result[index][0]
                    if curIndexHeight >= height:
                        goeCount += 1
                index += 1
            # print(result)
        return result
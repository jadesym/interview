class Solution:
    def countPoints(self, rings: str) -> int:
        rodRings = {}
        for i in range(10):
            rodRings[i] = {
                'R': 0,
                'G': 0,
                'B': 0
            }
        stringPairs = [rings[i:i+2] for i in range(0, len(rings), 2)]
        ringPairs = [(pair[0], int(pair[1])) for pair in stringPairs]
        for ringPair in ringPairs:
            color, ringNum = ringPair
            rodRings[ringNum][color] += 1
        count = 0
        for value in rodRings.values():
            if value['R'] > 0 and value['G'] > 0 and value['B'] > 0:
                count += 1
        return count
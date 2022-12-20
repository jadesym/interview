class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        scores = []
        for op in ops:
            if op == '+':
                scores.append(scores[len(scores) - 1] + scores[len(scores) - 2])
            elif op == 'D':
                scores.append(scores[len(scores) - 1] * 2)
            elif op == 'C':
                scores.pop()
            else:
                scores.append(int(op))

        return sum(scores)
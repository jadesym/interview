class Solution:
    def sumZero(self, n: int) -> List[int]:
        unique_positives = n // 2

        array = [num for num in range(1, unique_positives + 1)] + [-num for num in range(1, unique_positives + 1)]

        if n % 2 == 1:
            array.append(0)
        return array            
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odds = [x for x in A if x % 2 == 1]
        evens = [y for y in A if y % 2 == 0]
        odd_index = 0
        even_index = 0
        result_array = [0] * len(A)
        for index in range(len(result_array)):
            if index % 2 == 0:
                result_array[index] = evens[even_index]
                even_index += 1
            else:
                result_array[index] = odds[odd_index]
                odd_index += 1
        return result_array
        
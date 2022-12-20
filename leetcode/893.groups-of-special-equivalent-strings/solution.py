class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        lookup = set()
        for a in A:
            odd_set = []
            even_set = []
            for index in range(len(a)):
                if index % 2 == 0:
                    even_set.append(a[index])
                else:
                    odd_set.append(a[index])
            odd_string = "".join(sorted(odd_set))
            even_string = "".join(sorted(even_set))
            unique_tuple = tuple([odd_string, even_string])
            lookup.add(unique_tuple)
        return len(lookup)
                    
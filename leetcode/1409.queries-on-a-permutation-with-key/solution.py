class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        array = [x for x in range(1,m+1)]
        
        result = []
        for query in queries:
            for i in range(len(array)):
                item = array[i]
                if item == query:
                    result.append(i)
                    del array[i]
                    array = [query] + array
        return result
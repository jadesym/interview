class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None for i in range(n)]
        self.pointer = 0

    def insert(self, id: int, value: str) -> List[str]:
        self.stream[id - 1] = value
        result = []
        for index in range(self.pointer, len(self.stream)):
            elem = self.stream[index]
            if elem is None:
                self.pointer = index
                return result
            else: result.append(elem)
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
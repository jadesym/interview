from typing import Generic, TypeVar
import heapq

T = TypeVar("T")

class PriorityQueue(Generic[T]):
    def __init__(self):
        self._elements: Dict[T, int] = {}
        self._index: List[Tuple[int, T]] = []
        self._count: Dict[T, int] = {}

    # Time Complexity: O(1)
    def is_empty(self) -> bool:
        return len(self._index) == 0

    # Time Complexity: O(log n)
    def put(self, item: T, priority: int) -> None:
        if item in self._count:
            self._count[item] += 1
        else:
            self._count[item] = 1
            self._elements[item] = priority
        heapq.heappush(self._index, (priority, item))

    # Time Complexity: O(log n)
    def pop(self) -> Tuple[int, T]:
        priority, item = heapq.heappop(self._index)
        self._count[item] -= 1
        if self._count[item] == 0:
            del self._elements[item]
            del self._count[item]
        return (item, priority)

    # Time Complexity: O(k log n)
    def pop_k(self, k: int) -> List[T]:
        top_k = []
        for _ in range(k):
            if self.is_empty():
                break
            top_k.append(self.pop()[0])
        return top_k

    # Time Complexity: O(1)
    def peek(self) -> Tuple[int, T]:
        if self.is_empty(): return None
        return self._index[0]

    # Time Complexity: O(n)
    def elements(self) -> List[T]:
        result = []

        for element in self._elements.keys():
            result.extend([element] * self._count[element])

        return result

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        pqueue = PriorityQueue[int]()
        for i in range(len(mat)):
            numOnes = 0
            for val in mat[i]:
                if val == 1: numOnes += 1
                else: break
            pqueue.put(i, numOnes)
        return pqueue.pop_k(k)

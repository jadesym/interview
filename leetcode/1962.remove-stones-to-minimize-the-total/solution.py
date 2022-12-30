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
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pqueue = PriorityQueue[int]()

        for pile in piles:
            pqueue.put(pile, -pile)
 
        for i in range(k):
            popped_pile = pqueue.pop()[0]
            new_pile = popped_pile - popped_pile // 2
            pqueue.put(new_pile, -new_pile)
            # elements = sorted(pqueue.elements(), reverse=True)
            # print(popped_pile, new_pile, "-", elements)

        return sum(pqueue.elements())


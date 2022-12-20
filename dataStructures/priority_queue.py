from typing import Generic, TypeVar
import heapq

T = TypeVar("T")

class PriorityQueue(Generic[T]):
    def __init__(self):
        self._elements: Dict[T, int] = {}
        self._index: List[int, T] = []

    # Time Complexity: O(1)
    def is_empty(self) -> bool:
        return len(self._index) == 0

    # Time Complexity: O(log(n))
    def put(self, item: T, priority: int) -> None:
        self._elements[item] = priority
        heapq.heappush(self._index, (priority, item))

    # Time Complexity: O(log(n))
    def pop(self) -> tuple[int, T]:
        priority, item = heapq.heappop(self._index)
        del self._elements[item]
        return (priority, item)

    # Time Complexity: O(1)
    def peek(self) -> tuple[int, T]:
        if self.is_empty(): return None
        return self._index[0]

if __name__ == "__main__":
    pqueue = PriorityQueue[int]()
    assert pqueue.is_empty()
    pqueue.put(1, 2)

    # Peek for item
    peeked_item = pqueue.peek()
    # Check priority, then item value
    assert peeked_item[0] == 2
    assert peeked_item[1] == 1
    assert not pqueue.is_empty()
    # Pop the top item
    popped_item = pqueue.pop()
    # Check priority, then item value
    assert popped_item[0] == 2
    assert popped_item[1] == 1
    assert pqueue.is_empty()

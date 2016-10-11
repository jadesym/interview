"""
Given a sorted array with duplicates and a number, find the range in the
form of (startIndex, endIndex) of that number. For example,
find_range({0 2 3 3 3 10 10},  3) should return (2,4).
find_range({0 2 3 3 3 10 10},  6) should return (-1,-1).
The array and the number of duplicates can be large.
"""

test_cases = [
    ((0, ), 0, 0, 0),
    ((0, ), -1, -1, -1),
    ((0, ), 1, -1, -1),
    ((0, 2, 3, 3, 3, 10, 10), 3, 2, 4),
    ((0, 2, 3, 3, 3, 10, 10), 0, 0, 0),
    ((0, 2, 3, 3, 3, 10, 10), 2, 1, 1),
    ((0, 2, 3, 3, 3, 10, 10), 10, 5, 6),
    ((0, 2, 3, 3, 3, 10, 10), 6, -1, -1),
    ((3, 3, 3, 3), 3, 0, 3),
    ((3, 3, 3, 3), 2, -1, -1),
    ((3, 3, 3, 3), 4, -1, -1)
]

def findFirstOrLast(array, val, low, high, firstOrLast):
    if low > high: return -1
    mid = (low + high) // 2
    if array[mid] > val:
        return findFirstOrLast(array, val, low, mid - 1, firstOrLast)
    elif array[mid] < val:
        return findFirstOrLast(array, val, mid + 1, high, firstOrLast)
    else:
        if firstOrLast:
            if mid == low or array[mid - 1] < array[mid]:
                return mid
            else:
                return findFirstOrLast(array, val, low, mid - 1, firstOrLast)
        else:
            if mid == high or array[mid + 1] > array[mid]:
                return mid
            else:
                return findFirstOrLast(array, val, mid + 1, high, firstOrLast)


def elem_range(array, val):
    first = findFirstOrLast(array, val, 0, len(array) - 1, True)
    if first == -1:
        return -1, -1
    last = findFirstOrLast(array, val, first, len(array) - 1, False)
    return first, last

for test_case in test_cases:
    array, val, first, second = test_case
    firstRes, secondRes = elem_range(array, val)
    assert firstRes == first and secondRes == second
print("Test Cases Passed!")

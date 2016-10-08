"""
Given an array of integers, find the least number of steps to convert the
array so that all integers in the array are equal.

A step is defined as incrementing n - 1 elements of the array by 1. n is the
number of elements in the array. The n - 1 elements that are incremented
can differ each time.

Two Solutions:
O(n*log(n)) where n is the number of elements
O(m) where m is the difference between the maximum and minimum value in the array
* Note: Second Solution should be prefaced with how can we make it faster if
we have a large array but the range of the values is not that large.
"""

test_cases = {
    (5, 6, 8, 8, 5): 7,
    (1, 2, 3, 4): 6,
    (-1, -1, -1): 0,
    (-1, -1, -1, -1, 0): 1,
    (-1, 0, 0, 0, 0): 4
}

def increment_using_sort(array):
    counts = {}
    for val in array:
        if val in counts: counts[val] += 1
        else: counts[val] = 1
    sortedVals = sorted(counts.keys())
    lastVal = None
    lastCount = 0
    increments = 0
    for index in range(len(sortedVals) - 1, -1, -1):
        curVal = sortedVals[index]
        curCount = counts[curVal]
        if lastVal is not None:
            increments += lastCount * (lastVal - curVal)
        lastVal = curVal
        lastCount += curCount
    return increments

def increment_linear(array):
    counts = {}
    maxVal = float("-inf")
    minVal = float("inf")
    for val in array:
        if val in counts: counts[val] += 1
        else: counts[val] = 1
        if val > maxVal:
            maxVal = val
        if val < minVal:
            minVal = val
    curVal = maxVal
    increments = 0
    curCount = 0
    while curVal > minVal:
        if curVal in counts:
            curCount += counts[curVal]
        curVal -= 1
        increments += curCount
    return increments

for test_case in test_cases:
    assert increment_using_sort(test_case) == test_cases[test_case]
    assert increment_linear(test_case) == test_cases[test_case]

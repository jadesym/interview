"""
You are given an array of integers, max N elements, range -R to +R.
Rearrange the array such that
 - After rearrangement the array has all -ve numbers together, followed by all zeros, followed by all +ve numbers.
Please note that, you should not change the relative arrangement among the -ve and +ve numbers.

Input: [9,-6,5,-3,0,10,-1,0]

Output: [-6, -3, -1, 0, 0, 9, 5, 10]


Not that all 3 -ve numbers are to in the first 3 spots, and they are in the same order they are in the array.
"""

def moveZeroesToEnd(array):
    i, j = 0, 1
    while i < len(array) and j < len(array):
        if array[i] != 0: i += 1
        elif array[j] == 0 or j <= i: j += 1
        else: array[i], array[j] = array[j], array[i]
    return array

def moveZeroesToMiddle(array, minus, zeroes, plus):
    for x in range(len(array) - 1, minus + zeroes - 1, -1):
        array[x] = array[x - zeroes]
    for x in range(minus, minus + zeroes):
        array[x] = 0
    return array

def rotate(array, i, j, k):
    # print(array[i:j], k)
    count = 0
    start = i
    while count < j - i:
        do = True
        current = start
        prev = array[start]
        while current != start or do:
            if do: do = False
            next = (current + k - i) % (j - i) + i
            temp = array[next]
            array[next] = prev
            prev = temp
            current = next
            count += 1
        start += 1
    # print(array)

def mergeSort(array, low, high):
    if high - low <= 1: return
    mid = (high + low) // 2
    mergeSort(array, low, mid)
    mergeSort(array, mid, high)
    i = low
    j = high - 1
    while array[i] < 0 and i < mid + 1: i += 1
    while array[j] > 0 and j >= mid: j -= 1
    rotate(array, i, j + 1, j - mid + 1)

def swapMinusPlus(array, minus, plus):
    mergeSort(array, 0, minus + plus)
    return array

def rearrange(array):
    zeroes = array.count(0)
    minus = sum(1 if x < 0 else 0 for x in array)
    plus = sum(1 if x > 0 else 0 for x in array)
    print(minus, zeroes, plus)
    print(array)
    array = moveZeroesToEnd(array)
    # print(array)
    array = swapMinusPlus(array, minus, plus)
    # print(array)
    array = moveZeroesToMiddle(array, minus, zeroes, plus)
    print(array)

rearrange([9,-6,5,-3,0,10,-1,0])
rearrange([-3,0,5,9,0,-1,10,-6,0])
rearrange([0,0,0,1,1,1,-1,-1,-1])
rearrange([0,0,0,-1,-1,-1,1,1,1])
rearrange([-1,-1,-1,0,0,0,1,1,1])
rearrange([-1,-1,-1,1,1,1,0,0,0])
rearrange([1,1,1,-1,-1,-1,0,0,0])
rearrange([1,1,1,0,0,0,-1,-1,-1])

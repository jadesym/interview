"""
Given a sorted array that has been transposed (that is, a portion has been removed from one end and attached to the other), write a function to determine if a given number is present in the array.
Examples:
[6 7 1 2 3 4 5] 1
[6 7 1 2 3 4 5] 4
[9 13 32 54 1 2 5] 1
[9 13 32 54 1 2 5] 8
[2,3,4,4,4,4] 3
[4,4,4,2,3,4] 3
[2, 1, 1, 1, 1, 2, 2] 2
[4, 2, 3, 4, 4, 4, 4] 2
"""

test_cases = {
    'no_dup': [
        ([6, 7, 1, 2, 3, 4, 5], 1, True),
        ([6, 7, 1, 2, 3, 4, 5], 4, True),
        ([6, 7, 1, 2, 3, 4, 5], 8, False),
        ([6, 7, 1, 2, 3, 4, 5], 0, False),

        ([9, 13, 32, 54, 1, 2, 5], 1, True),
        ([9, 13, 32, 54, 1, 2, 5], 13, True),
        ([9, 13, 32, 54, 1, 2, 5], 8, False),
        ([9, 13, 32, 54, 1, 2, 5], 33, False)
    ],
    'dup': [
        ([2,3,4,4,4,4], 3, True),
        ([2,3,4,4,4,4], 1, False),
        ([2,3,4,4,4,4], 5, False),

        ([4,3,4,4,4,4], 3, True),
        ([4,3,4,4,4,4], 2, False),
        ([4,3,4,4,4,4], 5, False),

        ([4,4,4,2,3,4], 3, True),
        ([4,4,4,2,3,4], 1, False),
        ([4,4,4,2,3,4], 5, False),

        ([4,4,4,4,3,4], 3, True),
        ([4,4,4,4,3,4], 2, False),
        ([4,4,4,4,3,4], 5, False),

        ([2, 1, 1, 1, 1, 2, 2], 2, True),
        ([2, 1, 1, 1, 1, 2, 2], 0, False),
        ([2, 1, 1, 1, 1, 2, 2], 3, False),

        ([4, 2, 3, 4, 4, 4, 4], 2, True),
        ([4, 2, 3, 4, 4, 4, 4], 1, False),
        ([4, 2, 3, 4, 4, 4, 4], 5, False)
    ]
}

def transposed_no_dupl_recurse(array, val, low, high):
    if low > high: return False
    mid = (low + high) // 2
    lowVal, midVal, highVal = array[low], array[mid], array[high]
    if midVal == val: return True
    if midVal > lowVal:
        if val < lowVal or val > midVal:
            return transposed_no_dupl_recurse(array, val, mid + 1, high)
        else:
            return transposed_no_dupl_recurse(array, val, low, mid - 1)
    else:
        if val < midVal or val > highVal:
            return transposed_no_dupl_recurse(array, val, low, mid - 1)
        else:
            return transposed_no_dupl_recurse(array, val, mid + 1, high)

def transposed_search_no_dupl(array, val):
    return transposed_no_dupl_recurse(array, val, 0, len(array) - 1)

def transposed_dupl_recurse(array, val, low, high):
    if low > high: return False
    mid = (low + high) // 2
    lowVal, midVal, highVal = array[low], array[mid], array[high]
    if midVal == val: return True
    if midVal > lowVal:
        if val < lowVal or val > midVal:
            return transposed_no_dupl_recurse(array, val, mid + 1, high)
        else:
            return transposed_no_dupl_recurse(array, val, low, mid - 1)
    elif midVal == lowVal:
        return transposed_dupl_recurse(array, val, low + 1, high)
    else:
        if val < midVal or val > highVal:
            return transposed_no_dupl_recurse(array, val, low, mid - 1)
        else:
            return transposed_no_dupl_recurse(array, val, mid + 1, high)

def transposed_search_dupl(array, val):
    return transposed_dupl_recurse(array, val, 0, len(array) - 1)

for test_case in test_cases['no_dup']:
    array, num, result = test_case
    assert transposed_search_no_dupl(array, num) is result
    assert transposed_search_dupl(array, num) is result

for test_case in test_cases['dup']:
    array, num, result = test_case
    assert transposed_search_dupl(array, num) is result

print("All Test Cases Pass!")

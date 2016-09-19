"""
Given an array nums, write a function to move all 0's to the end
of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your
function, nums should be [1, 3, 12, 0, 0].
"""

def moveZeroes(array):
    i,j = 0, 1
    while j < len(array) and i < len(array):
        if array[j] == 0 or j <= i: j += 1
        elif array[i] != 0: i += 1
        else: array[i], array[j] = array[j], array[i]
    return array

print(moveZeroes([0,1,0,3,12]))
print(moveZeroes([0,0,1,2,3]))
print(moveZeroes([0,0,0,0,0]))
print(moveZeroes([1,2,3,4,5]))
print(moveZeroes([1,2,3,0,0]))

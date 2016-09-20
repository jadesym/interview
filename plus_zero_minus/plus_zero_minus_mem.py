"""
You are given an array of integers, max N elements, range -R to +R.
Rearrange the array such that
 - After rearrangement the array has all -ve numbers together, followed by all zeros, followed by all +ve numbers.
Please note that, you should not change the relative arrangement among the -ve and +ve numbers.

Input: [9,-6,5,-3,0,10,-1,0]

Output: [-6, -3, -1, 0, 0, 9, 5, 10]


Not that all 3 -ve numbers are to in the first 3 spots, and they are in the same order they are in the array.
"""

# Solution that uses extra space
def rearrangeMem(array):
    minus, zero, plus = [], [], []
    for num in array:
        if num < 0: minus.append(num)
        elif num == 0: zero.append(num)
        else: plus.append(num)
    return minus + zero + plus

print(rearrangeMem([9,-6,5,-3,0,10,-1,0]))
print(rearrangeMem([9, -6, 5 , -3,  10, -1, 0, 0, 0]))

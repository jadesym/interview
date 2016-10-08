"""
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die. Given a flowerbed (represented as an array containing booleans), return if a given number of new flowers can be planted in it without violating the no-adjacent-flowers rule.
"""

test_cases = {
((1,0,0,0,0,0,1,0,0), 3): True,
((1,0,0,0,0,0,1,0,0), 4): False,
((1,0,0,1,0,0,1,0,0), 1): True,
((1,0,0,1,0,0,1,0,0), 2): False,
((0,), 1): True,
((0,), 2): False
}

def can_plant_modify_orig(bools, k):
    if bools is None or len(bools) < k: return False
    for index in range(len(bools)):
        if bools[index] == 0 and (index == 0 or bools[index - 1] == 0) and (index == len(bools) - 1 or bools[index + 1] == 0):
            k -= 1
            bools[index] = 1
    return k <= 0

def can_plant_without_modify_orig(bools, k):
    if bools is None or len(bools) < k: return False
    lastPlot = False
    for index in range(len(bools)):
        if bools[index] == 0 and not lastPlot and (index == len(bools) - 1 or bools[index + 1] == 0):
            lastPlot = True
            k -= 1
        elif bools[index] == 1:
            lastPlot = True
        else:
            lastPlot = False
    return k <= 0

for case in test_cases:
    test_case, k = case
    assert can_plant_modify_orig(list(test_case), k) is test_cases[(test_case, k)]
    assert can_plant_without_modify_orig(test_case, k) is test_cases[(test_case, k)]
print("Done")

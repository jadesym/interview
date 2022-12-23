from typing import TypeVar

T = TypeVar("T")

def generate_permutations(initial_list: List[T], is_unique: bool) -> List[List[T]]:
    if len(initial_list) == 0: return []
    elif len(initial_list) == 1: return [[initial_list[0]]]

    new_perms = []

    for i in range(len(initial_list)):
        cur_element = initial_list[i]
        other_elems = None
        if is_unique:
            other_elems = initial_list[i + 1:]
        else:
            other_elems = initial_list[:i] + initial_list[i + 1:]

        nested_perms = generate_permutations(other_elems, is_unique)
        for nested_perm in nested_perms:
            new_perms.append([cur_element] + nested_perm)
        new_perms.append([cur_element])

    return new_perms

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = 0
        numMax = 0
        perms = generate_permutations(nums, True)

        for perm in perms:
            curOr = 0
            for elem in perm:
                # print(elem)
                curOr |= elem
            if maxOr < curOr:
                maxOr = curOr
                numMax = 1
            elif maxOr == curOr:
                numMax += 1

        return numMax

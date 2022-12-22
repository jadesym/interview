from typing import TypeVar, List

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

perm_test_cases = [
    ([], []),
    ([1], [[1]]),
    ([1, 2], [[1], [2], [1, 2], [2, 1]]),
    ([1, 2, 3], \
        [[1], [2], [3], \
        [1, 2], [1, 3], \
        [2, 1], [2, 3], \
        [3, 1], [3, 2], \
        [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
]

unique_perm_test_cases = [
    ([], []),
    ([1], [[1]]),
    ([1, 2], [[1], [2], [1, 2]]),
    ([1, 2, 3], \
        [[1], [2], [3], \
        [1, 2], [1, 3], \
        [2, 3], \
        [1, 2, 3]])
]

def run_non_unique_perm_test_cases():
    for input, expected_result in perm_test_cases:
        actual_result = generate_permutations(input, False)

        actual_set = set()
        for actual_perm in actual_result:
            actual_set.add(tuple(actual_perm))
        actual_processed = [list(perm) for perm in actual_set]

        # print("Expected", sorted(expected_result))
        # print("Actual", sorted(actual_processed))

        assert len(expected_result) == len(actual_processed)
        for expected_perm_index in range(len(expected_result)):
            expected_perm = expected_result[expected_perm_index]
            actual_perm = expected_result[expected_perm_index]
            # print(actual_perm, expected_perm)
            assert len(expected_perm) == len(actual_perm)

            for expected_perm_element_index in range(len(expected_perm)):
                assert expected_perm[expected_perm_element_index] == actual_perm[expected_perm_element_index]

def run_unique_perm_test_cases():
    for input, expected_result in unique_perm_test_cases:
        actual_result = generate_permutations(input, True)

        # print("Expected", sorted(expected_result))
        # print("Actual", sorted(actual_result))

        assert len(expected_result) == len(actual_result)
        for expected_perm_index in range(len(expected_result)):
            expected_perm = expected_result[expected_perm_index]
            actual_perm = expected_result[expected_perm_index]
            # print(actual_perm, expected_perm)
            assert len(expected_perm) == len(actual_perm)

            for expected_perm_element_index in range(len(expected_perm)):
                assert expected_perm[expected_perm_element_index] == actual_perm[expected_perm_element_index]


if __name__ == "__main__":
    run_non_unique_perm_test_cases()
    run_unique_perm_test_cases()

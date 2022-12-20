import string

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        first_row = s[0]
        first_col = int(s[1])
        last_row = s[3]
        last_col = int(s[4])

        result = []
        # print(first_row, first_col, last_row, last_col)
        is_in_range = False
        for upper_case_letter in string.ascii_uppercase:
            if upper_case_letter == first_row: is_in_range = True

            if is_in_range:
                for i in range(first_col, last_col + 1):
                    result.append(upper_case_letter + str(i))
            
            if is_in_range and upper_case_letter == last_row:
                is_in_range = False
            # print(upper_case_letter, result)

        return result
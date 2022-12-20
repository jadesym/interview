import string

class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        letter_array = string.ascii_lowercase
        letter_widths = {letter_array[i] : widths[i] for i in range(len(letter_array))}
        lines_so_far = 0
        current_line_len = 0
        for letter in S:
            letter_len = letter_widths[letter]
            if letter_len + current_line_len > 100:
                lines_so_far += 1
                current_line_len = letter_len
            else:
                current_line_len = letter_len + current_line_len
        return [lines_so_far + 1, current_line_len]
        
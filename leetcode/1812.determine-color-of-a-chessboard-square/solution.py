class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        lower_chars = string.ascii_lowercase
        char_to_index = {lower_chars[i]: i for i in range(len(lower_chars))}
        # print(char_to_index)
        char, num = coordinates
        return (char_to_index[char] + int(num)) % 2 == 0
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_char_count = {}
        t_char_count = {}
        for s_char in s:
            if s_char not in s_char_count:
                s_char_count[s_char] = 0
            s_char_count[s_char] += 1
        for t_char in t:
            if t_char not in t_char_count:
                t_char_count[t_char] = 0
            t_char_count[t_char] += 1
        # print(s_char_count, t_char_count)
        steps = 0
        for t_char, count in t_char_count.items():
            if t_char not in s_char_count:
                steps += count
            elif count > s_char_count[t_char]:
                steps += count - s_char_count[t_char]
        return steps

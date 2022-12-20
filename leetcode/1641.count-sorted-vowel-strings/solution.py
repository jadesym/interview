class Solution:
    # a: [a, aa, aaa] 1-1-1
    # e: [e, ae|ee, aae|aee|eee] 1-2-3-4
    # i: [i, ai|ei|ii, aii|aei|eei|aii|eii|iii] 1-3-6
    # o: [o, ao|eo|io|oo, aao|aeo|eeo|aio|eio|iio|aoo|eoo|ioo|ooo] 1-4-10-20
    # u: [u, au|eu|iu|ou|uu] 1-5
    def countVowelStrings(self, n: int) -> int:
        end_a = 1
        end_e = n
        end_i = n * (n + 1) // 2
        end_o = n * (n + 1) * (n + 2) // 6
        end_u = n * (n + 1) * (n + 2) * (n + 3) // 24
        return end_a + end_e + end_i + end_o + end_u





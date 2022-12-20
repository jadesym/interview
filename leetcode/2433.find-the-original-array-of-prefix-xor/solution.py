class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        running_xor = pref[0]
        xor_array = [running_xor]
        for i in range(1, len(pref)):
            xor_array.append(pref[i] ^ pref[i - 1])

        return xor_array
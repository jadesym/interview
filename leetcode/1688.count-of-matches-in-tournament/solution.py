class Solution:
    def numberOfMatches(self, n: int) -> int:
        totalMatches = 0
        curTeams = n
        while curTeams > 1:
            totalMatches += curTeams // 2
            if curTeams % 2 == 1:
                curTeams -= curTeams // 2
            else:
                curTeams //= 2
        return totalMatches
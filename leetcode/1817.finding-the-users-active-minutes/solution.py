class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        userTimeSets = {}
        for [user, time] in logs:
            if user not in userTimeSets:
                userTimeSets[user] = set()
            userTimeSets[user].add(time)
        uams = [0] * k
        for key, value in userTimeSets.items():
            uams[len(value) - 1] += 1
        return uams
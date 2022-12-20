class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupSizeToIndex = {}
        for index in range(len(groupSizes)):
            groupSize = groupSizes[index]
            if groupSize in groupSizeToIndex:
                groupSizeToIndex[groupSize].append(index)
            else:
                groupSizeToIndex[groupSize] = [index]
        
        result = []
        for groupSize, people in groupSizeToIndex.items():
            result += [people[index:index+groupSize] for index in range(0,len(people),groupSize)]
        return result
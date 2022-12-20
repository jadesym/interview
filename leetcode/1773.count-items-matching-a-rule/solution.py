class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        itemIndex = 0 if ruleKey ==  "type" else 1 if ruleKey == "color" else 2
        counter = 0
        for item in items:
            if item[itemIndex] == ruleValue: counter += 1
                
        return counter
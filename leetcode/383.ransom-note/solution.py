class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomHash = {}
        magazineHash = {}
        for letter in ransomNote:
            if letter in ransomHash:
                ransomHash[letter] += 1
            else:
                ransomHash[letter] = 1
        for secondLetter in magazine:
            if secondLetter in magazineHash:
                magazineHash[secondLetter] += 1
            else:
                magazineHash[secondLetter] = 1
        for key in ransomHash:
            if key not in magazineHash:
                return False
            if ransomHash[key] > magazineHash[key]:
                return False
        return True
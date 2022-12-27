class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        letters = string.ascii_lowercase
        lower_case_map = {letters[i]: str(i) for i in range(len(letters))}

        fwVal  = self.getValue(firstWord, lower_case_map)
        swVal = self.getValue(secondWord, lower_case_map)
        twVal = self.getValue(targetWord, lower_case_map)
        return fwVal + swVal == twVal
    
    def getValue(self, word: str, lower_case_map: Dict[str, str]) -> int:
        result = []
        for char in word:
            result.append(lower_case_map[char])
        
        resultString = "".join(result)
        return int(resultString)

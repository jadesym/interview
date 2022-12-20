class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = True
        resultArray = [0]*len(digits)
        for index in range(len(digits) - 1, -1, -1):
            if digits[index] == 9 and carry:
                carry = True
                resultArray[index] = 0
            else:
                if carry:
                    resultArray[index] = digits[index] + 1
                else:
                    resultArray[index] = digits[index]
                carry = False
        if carry:
            resultArray.insert(0, 1)
        return resultArray
            
            
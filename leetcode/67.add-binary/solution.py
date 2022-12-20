class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a[::-1]
        b = b[::-1]
        index = 0
        carry = False
        result = []
        while index < len(a) or index < len(b):

            if index >= len(a):
                # print(b[index])
                if carry and b[index] == "1":
                    result.append("0")
                    carry = True
                elif carry and b[index] == "0" or not carry and b[index] == "1":
                    result.append("1")
                    carry = False
                else:
                    result.append(b[index])
            elif index >= len(b):
                # print(a[index])
                if carry and a[index] == "1":
                    result.append("0")
                    carry = True
                elif carry and a[index] == "0" or not carry and a[index] == "1":
                    result.append("1")
                    carry = False
                else: result.append(a[index])
            else:
                aVal = a[index]
                bVal = b[index]
                # print(aVal, bVal)
                if aVal == "1" and bVal == "1":
                    if carry == True: result.append("1")
                    else: 
                        result.append("0")
                        carry = True
                elif aVal == "1" and bVal == "0":
                    if carry == True: result.append("0")
                    else: 
                        result.append("1")
                        carry = False
                elif aVal == "0" and bVal == "1":
                    if carry == True: result.append("0")
                    else: 
                        result.append("1")
                        carry = False
                else:
                    if carry == True: 
                        result.append("1")
                        carry = False
                    else:
                        result.append("0")
            index += 1
        if carry: result.append("1")
        return ''.join(result[::-1])
                    

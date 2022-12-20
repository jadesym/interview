import functools

class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digits = []
        words = []
        for log in logs:
            if self.isDigitLog(log):
                digits.append(log)
            else:
                words.append(log)
                
        return sorted(words, key=functools.cmp_to_key(self.compare)) + digits
    def isDigitLog(self, log):
        strings = log.split()
        word = strings[1]
        try: 
            int(word)
            return True
        except ValueError:
            return False
    def compare(self, x, y):
        x_id, x_contents = x.split(" ", 1)
        y_id, y_contents = y.split(" ", 1)
        if x_contents < y_contents: return -1
        elif x_contents > y_contents: return 1
        else:
            if x_id < y_id: return -1
            elif x_id > y_id: return 1
            else: return 0
        
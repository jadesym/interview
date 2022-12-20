class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.isInt(token):
                stack.append(int(token))
            elif token == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second))
            elif token == "*":
                second = stack.pop()
                first = stack.pop()
                stack.append(first * second)
            elif token == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)
            elif token == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            else:
                raise BaseException("{} is an invalid token.".format(token))
            # print(stack, token)
        return stack[0]
    def isInt(self, numString: str):
        try:
            int(numString)
            return True
        except:
            return False
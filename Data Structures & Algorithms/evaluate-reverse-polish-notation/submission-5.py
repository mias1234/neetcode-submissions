class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = 0

        n = len(tokens)

        stack = []

        for i in range(n):

            try:
                stack.append(float(tokens[i]))
            except:
                pass

            if tokens[i] == '+':
                res = float(stack[-1]) + float(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(res)

            elif tokens[i] == '-':
                res = float(stack[-2]) - float(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(res)

            elif tokens[i] == '*':
                res = float(stack[-2]) * float(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(res)

            elif tokens[i] == '/':
                res = abs(float(stack[-2])) // abs(float(stack[-1]))
                if (float(stack[-2]) < 0) != (float(stack[-1]) < 0):
                    res = -res
                stack.pop()
                stack.pop()
                stack.append(res)
            
        return int(stack[-1])
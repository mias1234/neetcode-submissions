class Solution:
    def isValid(self, s: str) -> bool:
        para = {')': '(', '}': '{', ']': '['}

        stack = []

        if len(s) <= 1:
            return False

        for char in s:
            if char in ['(','{','[']:
                stack.append(char)

            else:
                if stack:
                    if stack[-1] == para[char]:
                        stack.pop()
                    else:
                        return False

                else:
                    return False

        return True if not stack else False
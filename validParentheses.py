# https://leetcode.com/problems/valid-parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack[-1] != mapping[c]:
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        return True


if __name__ == "__main__":
    obj = Solution()
    print(obj.isValid("([{}])"))

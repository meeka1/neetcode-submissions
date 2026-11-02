class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            # keys (opening): values (closing)
            "[": "]",
            "{": "}",
            "(": ")",
        }
        stack = []
        for ch in s:
            if ch in brackets.keys():
                stack.append(brackets[ch])
            else:
                if not stack or stack.pop() != ch:
                    return False
        return not stack
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
            if ch in brackets:                 # открывающая
                stack.append(brackets[ch])     # запоминаем, какую закрывающую ждём
            else:                              # закрывающая
                if not stack or stack.pop() != ch:
                    return False
        return not stack 

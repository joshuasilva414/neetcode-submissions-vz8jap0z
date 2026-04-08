class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(',']':'[','}':'{'}
        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            elif not stack or pairs[ch]!=stack.pop():
                    return False
        if stack:
            return False
        return True
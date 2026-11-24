class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {")":"(","}":"{","]":"["}
        for c in s:
            if c not in hm:
                stack.append(c)
            else:
                if not stack or stack[-1] != hm[c]:
                    return False
                stack.pop()

        if not stack:return True
        return False
        
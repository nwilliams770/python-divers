class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {")":"(", "]":"[", "}":"{"}

        for char in s:
#           If opening paren, add to stack
            if char in lookup.values():
                stack.append(char)
#           Else if we have a closing paren AND we have values in the stack
#           (covers cases where there's just a single closing paren), pop the stack
            elif len(stack) > 0 and lookup[char] == stack[-1]:
                stack.pop()
#         Otherwise, we've gone out of order or have a single closing paren
            else:
                return False
#       Covers cases of a single open paren
        return len(stack) == 0
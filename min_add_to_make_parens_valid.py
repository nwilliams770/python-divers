class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        open_parens = 0
        min_parens = 0

        for char in S:
            if char == "(":
                open_parens += 1
            elif char == ")":
                if not open_parens:
                    min_parens += 1
                else:
                    open_parens -= 1

        if open_parens > 0:
            min_parens += open_parens

        return min_parens
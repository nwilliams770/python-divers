import string

class Solution:
    def generateTheString(self, n: int) -> str:
        result = ''
        if n % 2 == 0:
            result += 'a' + 'b' * (n - 1)
        else:
            result += 'a' * n

        return result
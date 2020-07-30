class Solution:
    def numSplits(self, s: str) -> int:
        good_splitsies = 0

        for i in range(len(s)//2, 0, -1):
            equal, less_than = self.count(i, s)
            if equal:
                good_splitsies += 1
            elif less_than:
                break

        for i in range(len(s)//2 + 1, len(s)):
            equal, less_than = self.count(i, s)
            if equal:
                good_splitsies += 1
            elif not less_than:
                break

        return good_splitsies

    def count(self, i, s):
        first_half = len(set(s[:i]))
        second_half = len(set(s[i:]))
        if first_half == second_half:
            return True, False
        return False, (first_half < second_half)
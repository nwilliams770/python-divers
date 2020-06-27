class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = self._count_letters(s)
        t_count = self._count_letters(t)

        for k in s_count:
            if k in t_count:
                s_count[k] = 0 if t_count[k] > s_count[k] else s_count[k] - t_count[k]

        return sum(s_count.values())

    def _count_letters(self, s):
        count = {}
        for letter in s:
            count[letter] = count.get(letter, 0) + 1

        return count
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        k -= 1  # stupid

        strs = []
        for i in range(self._max_strings(n)):
            s = self._generate_abc_str(i, n)
            if self._is_happy(s):
                strs.append(s)

        if k < len(strs):
            return strs[k]
        return ''

    def _generate_abc_str(self, i: int, n: int) -> str:
        # Converts an int to a abc str
        s = ['a'] * n
        place = n-1
        while i:
            d = i % 3
            s[place] = 'a' if d == 0 else ('b' if d == 1 else 'c')
            i //= 3
            place -= 1

        return ''.join(s)  # TODO

    def _is_happy(self, s: str) -> bool:
        prev_char = ""
        for char in s:
            if prev_char == char:
                return False

            prev_char = char

        return True


    def _max_strings(self, n: int) -> int:
        return 3**n
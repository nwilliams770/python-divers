import string

class Solution:
    def freqAlphabets(self, s: str) -> str:
        code_map = self.generate_code_map()
        decoded = ""

        while True:
            temp = s[0]

            if len(s) >= 3 and s[2] == "#":
                decoded += code_map[s[0:3]]
                s = s[3:]
            else:
                decoded += code_map[temp]
                s = s[1:]

            if len(s) == 0:
                break

        return decoded

    def generate_code_map(self):
        alphabet = list(string.ascii_lowercase)
        code_map = {}

        for i in range(0, 26):
            if i < 9:
                code = str(i + 1)
                code_map[code] = alphabet[i]
            else:
                code = str(i + 1) + "#"
                code_map[code] = alphabet[i]

        return code_map
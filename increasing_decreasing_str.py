import string

class Solution:
    def sortString(self, s: str) -> str:
        alphabet = list(string.ascii_lowercase)
        frequency_map = self._generate_frequency_map(s)
        result = ''

        while True:
            result += self._pull_letters_a_to_z(frequency_map, alphabet)
            result += self._pull_letters_z_to_a(frequency_map, alphabet)

            if sum(frequency_map.values()) == 0:
                break
#       create frequency map of s
#       until there are no more chars
#           iterate a to z, if there is a char to grab, grab it and append to result
#           iterate z to a, if there is char to grab, grab it and append to result
        return result

    def _pull_letters_a_to_z(self, frequency_map: dict, alphabet: List[str]) -> str:
        result = ''
        for letter in alphabet:
            if letter in frequency_map and frequency_map[letter] > 0:
                result += letter
                frequency_map[letter] = frequency_map.get(letter) - 1
        return result

    def _pull_letters_z_to_a(self, frequency_map: dict, alphabet: List[str]) -> str:
        result = ''
        for letter in reversed(alphabet):
            if letter in frequency_map and frequency_map[letter] > 0:
                result += letter
                frequency_map[letter] = frequency_map.get(letter) - 1
        return result

    def _generate_frequency_map(self, s: str) -> dict:
        frequency_map = {}
        for letter in s:
            frequency_map[letter] = frequency_map.get(letter, 0) + 1
        return frequency_map
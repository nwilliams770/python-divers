class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
#     code pattern
#     for each word, check if coded word pattern matches pattern provided
        pattern_matches = []
        coded_pattern = self._generate_pattern(pattern)

        for word in words:
            if self._generate_pattern(word) == coded_pattern:
                pattern_matches.append(word)

        return pattern_matches

    def _generate_pattern(self, word: str):
        coded_pattern = []

        char_map = {}
        current_code = 0

        for char in word:
            if char in char_map:
                coded_pattern.append(char_map[char])
            else:
                char_map[char] = current_code
                coded_pattern.append(current_code)
                current_code += 1

        return coded_pattern
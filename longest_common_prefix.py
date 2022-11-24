class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if (len(strs) == 0):
            return ""

        longest_prefix = strs[0]

        for string in strs:
            for index in range(0, len(longest_prefix)):
                if (index >= len(string) or longest_prefix[index] != string[index]):
                    longest_prefix = longest_prefix[0:index]
                    break

        return longest_prefix
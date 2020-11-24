class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substr_len = 0

        for i in range(0, len(s)):
            for j in range(i, len(s)):
                sub_s = s[i:j + 1]
                if not sub_s:
                    continue
                sub_s_list = set(sub_s)

                if len(sub_s) != len(sub_s_list):
                    break
                else:
                    longest_substr_len = len(sub_s) if len(sub_s) > longest_substr_len else longest_substr_len

        return longest_substr_len

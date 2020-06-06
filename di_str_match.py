class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        result = []
        low = 0
        high = len(S)

#       Maintain highest and lowest numbers added so far
        for char in S:
#           If next el must be decreasing val, we must append the HIGHEST num we have
            if char == "D":
                result.append(high)
                high -= 1
#           If next el must be increasing val, append LOWEST num we have
            else:
                result.append(low)
                low += 1
#       Append last remaining num, we can append either high or low, they are equal
        result.append(high)

        return result
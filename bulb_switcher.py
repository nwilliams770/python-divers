class Solution:
    def minFlips(self, target: str) -> int:
        flips = 0
#       If flipped_bulbs True, all subsequent bulbs are 1's
#       If False, all subsequent bulbs are 0's
        flipped_bulbs = False

        for i in range(0, len(target)):
            if target[i] == "1" and not flipped_bulbs:
                flipped_bulbs = True
                flips += 1
            elif target[i] == "0" and flipped_bulbs:
                flipped_bulbs = False
                flips += 1

        return flips
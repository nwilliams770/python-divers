class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        negs, zeroes, pos = [], [], []
        result = set()

        for num in nums:
            if num > 0:
                pos.append(num)
            elif num < 0:
                negs.append(num)
            else:
                zeroes.append(num)

        negs_unique, pos_unique = set(negs), set(pos)

#       If 0, create instances with each number and its complement
        if len(zeroes) > 0:
            for num in pos_unique:
                if num*-1 in negs_unique:
                    result.add((num*-1, 0, num))

#         If 3 zeroes, add them
        if len(zeroes) >= 3:
            result.add((0, 0, 0))

#       For all negs, attempt to get positive complement
        for i in range(len(negs)):
            for j in range(i+1, len(negs)):
                target = -1 * (negs[i] + negs[j])
                if target in pos_unique:
                    result.add(tuple(sorted([target, negs[i], negs[j]])))

#       For all pos, attempt to get negative complement
        for i in range(len(pos)):
            for j in range(i+1, len(pos)):
                target = -1 * (pos[i] + pos[j])
                if target in negs_unique:
                    result.add(tuple(sorted([target, pos[i], pos[j]])))

        return result
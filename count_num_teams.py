class Solution:
    def numTeams(self, rating: List[int]) -> int:
        c = 0
        l = len(rating)

        for i in range(0, l - 2):
            for j in range(i + 1, l - 1):
                for k in range(j + 1, l):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        c += 1

        return c
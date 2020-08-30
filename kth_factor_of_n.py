class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = self._generate_factors(n)

        if k > len(factors):
            return - 1
        else:
            return factors[k - 1]


    def _generate_factors(self, n):
        factors = []

        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)

        return factors
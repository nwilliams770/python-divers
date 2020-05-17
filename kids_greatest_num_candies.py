def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    solution = []
    maximum = max(candies)
    for candy in candies:
        if candy + extraCandies >= maximum:
            solution.append(True)
        else:
            solution.append(False)
    return solution


# Brute-force:
# - For each kid, add extraCandies and check if sum
# is greater than all other kids' candies;
# - Two for loops, O(n ^ 2)

# Lower time-complexity solution:
# - Get max candy in candies. Iterate through list checking if
# given candy + extraCandies more/less than max
# - Requires one pass of iteration, O(n)

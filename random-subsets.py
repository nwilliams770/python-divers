import random
from typing import List
# Given a positive int n, and size k; generate a subset size k with els up to n-1 of
# equal probability; ordering of els in subset are also of random probability

def random_subsets(n: int, k: int) -> List[int]:
    subset = set()

    while len(subset) < k:
        random_num = random.randrange(0, n)
        subset.add(random_num)

    return list(subset)

def random_subsets_rebirth(n: int, k: int) -> List[int]:
    nums = list(range(n))
    result = [None] * k

    for _ in range(k):
        random_index = random.randrange(0, len(nums))
        num = nums.pop(random_index)
        result.append(num)

    return result

def random_subsets_with_hash(n: int, k: int) -> List[int]:
    pass


def test():
    with open('a.csv', 'w') as f:
        n = 100
        k = 20
        for i in range(1000):
            l = random_subsets_rebirth(n, k)
            for e in l:
                f.write(str(e) + ',')
            f.write('\n')


if __name__ == "__main__":
    test()
    # print(random_subsets(10, 5))





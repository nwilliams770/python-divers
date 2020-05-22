from typing import List

class Solution:

    # Space O(n) // Time O(n ** 2)
    # Not necessary to use a dict, we can just use arrays here
    def destCity(self, paths: List[List[str]]) -> str:
        city_paths = {}

        for path in paths:
            city_paths[path[0]] = path[1]

        return [el for el in city_paths.values() if el not in city_paths.keys()][0]


#   Space O(n) // Time O(n)
#   Best in terms of space and time complexities
#   Also good leverage of sets, which have O(1) on average operations
    def destCity3(self, paths: List[List[str]]) -> str:
        starts = set()
        ends = set()

        for path in paths:
            starts.add(path[0])
            ends.add(path[1])

        # return [el for el in ends if el not in starts][0]
        return (ends - starts).pop()


    def destCity2(self, paths: List[List[str]]) -> str:
#       Space O(1) // Time O(n ** 2)
        for path in paths:
            dest = path[1]
            found = False
            for other_path in paths:
                other_start = other_path[0]
                if other_start == dest:
                    found = True
                    break
            if not found:
                return dest
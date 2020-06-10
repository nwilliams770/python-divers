from collections import deque
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        result = []
        shifted_nums = deque()

        for query in queries:
#           If our query has already been queried before e.g. added to our shifted_nums
            if query in shifted_nums:
#               Get the idx of that num, since they are in the beginning of [0...m], the index will be faithful
                queried = shifted_nums.index(query)

                result.append(queried)
#               remove it and move it back to the front of shifted_nums
                shifted_nums.remove(query)
                shifted_nums.appendleft(query)
            else:
                shift = self._calc_magnitude_shift(shifted_nums, query)
                print("query:", query, "shift", shift)
                queried = query + shift
                result.append(queried)
                shifted_nums.appendleft(query)

        return result

    def _calc_magnitude_shift(self, d, q):
        magnitude_shift = -1
        greater_mag_shift = len(list(filter(lambda x: x > q, d)))

        if greater_mag_shift or lower_mag_shift:
            magnitude_shift += greater_mag_shift

        return magnitude_shift
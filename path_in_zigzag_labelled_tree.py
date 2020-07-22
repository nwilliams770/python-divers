import math

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        return self._derive_parents(label, [])


    def _derive_parents(self, label: int, parent_path: List[int]):
        parent_path = [label] + parent_path

        if label == 1:
            print("parent_path, we made it to the base case sucka", parent_path)
            return parent_path

        parent_label = self._calc_parent(label)

        return self._derive_parents(parent_label, parent_path)

    def _calc_parent(self, label: int) -> int:
        level = self._get_level(label)
        min_label, max_label = self._calc_min_max_labels(level)
        parent_min, parent_max = self._calc_min_max_labels(level - 1)

        grouping = (label - min_label) // 2
        parent_label = parent_max - grouping

        return int(parent_label)

    def _calc_min_max_labels(self, level: int) -> (int, int):
        min_label = 2 ** (level - 1)
        num_nodes_at_level = min_label
        max_label = min_label + num_nodes_at_level - 1

        return min_label, max_label

    def _get_level(self, label: int) -> int:
        return int(math.floor(math.log(label, 2)) + 1)



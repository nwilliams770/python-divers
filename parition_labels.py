class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        partitions = []
        letters = list(S)
        last_occurences = self._generate_last_occurence_idx_map(letters)
        i = 0
        j = 0


        while True:
            letter = letters[i]

#           + 1 since slice is not inclusive of outer bound
            possible_partition = letters[j:last_occurences[letter] + 1]

            if self.possible_partition_valid(possible_partition, j, last_occurences):
                partitions.append(len(possible_partition))
                j += len(possible_partition)
                i = j
            else:
                i += 1

            if i > len(letters) - 1:
                break

        return partitions


    def possible_partition_valid(self, p, j, last_occurences):
        letters = set(p)

        for letter in letters:
            if last_occurences[letter] > j + len(p) - 1:
                return False

        return True


    def _generate_last_occurence_idx_map(self, l):
        last_occurences = {}

        for i in reversed(range(0, len(l))):
            if l[i] not in last_occurences:
                last_occurences[l[i]] = i

        return last_occurences
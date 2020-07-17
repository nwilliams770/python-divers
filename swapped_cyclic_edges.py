from typing import List
import collections

# input [[1, 2] [3, 2] [5, 1] [4, 5] [4, 3]]
# output [1, 2, 3, 4, 5] or [5, 4, 3, 2, 1]

# 1 - 2 - 3 - 4 - 5 (cyclic)


# 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> (cyclic)

def swapped_cyclic_edges_linked_list(edges: List[List[int]]) -> List[int]:
    connections = collections.defaultdict(set())
    for (start, end) in edges:
        connections[start].add(end)
        connections[end].add(start)

    """
    1: {5, 2}
    2: {1, 3}
    3: {2, 4}
    4: {3, 5}
    5: {1, 4}
    """

    chain = []
    start = edges[0][0]
    prev = None
    while len(chain) < len(edges):
        chain.append(start)
        next_a, next_b = connections[start]
        if next_a == prev:
            prev = start
            start = next_b
        else:
            prev = start
            start = next_a

    return chain


def swapped_cyclic_edges(edges: List[List[int]]) -> List[int]:
    result = []
    num_nodes = len(edges)

    # let's just take the first edge and start with that, solution is agnostic to order
    # so it shouldn't matter if it's swapped or not
    result.extend(edges.pop(0))
    node = result[-1]

    while True:
        for i, edge in enumerate(edges):
            # edge not swapped
            if edge[0] == node:
                result.append(edge[1])
                node = edge[1]
                edges.pop(i)
                break

            # edge swapped
            if edge[1] == node:
                result.append(edge[0])
                node = edge[0]
                edges.pop(i)
                break

        if len(result) == num_nodes:
            break

    return result

if __name__ == "__main__":
    print(swapped_cyclic_edges([[1, 2], [3, 2], [5, 1], [4, 5], [4, 3]]))



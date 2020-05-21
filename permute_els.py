from typing import List
# Given Array A of n elements, apply permutation P to A
# A: [a, b, c, d, e], P: [2, 0, 1, 4, 3] => [c, a, b, e, d]



# Solution #1 -- O(n) time/space
def permute_array(arr: List[int], permute: List[int]) -> List[int]:
    permutated = [None] * len(arr)

    for i in range(len(arr)):
        permutated[permute[i]] = arr[i]

    return permutated

# Solution 2 -- O(n) time // O(1) space
# 0:
# Get index from permute // 2
# Get the el from arr // a
# Get the el at permute index // c
# Put a in new index location // a => 2
# Get new index for c by using index from permute // 1
def permute_array_swaps(arr: List[int], permute: List[int]) -> List[int]:
    for i in range(len(arr)):
        # Get index from permute[i] and el at arr[permute[i]]
        p_idx = permute[i]
        el_to_swap = arr[i]

        entered = False
        while permute[p_idx] is not None:
            entered = True

            # Grab el to be replaced
            el_to_be_replaced = arr[p_idx]
            # Replace el
            arr[p_idx] = el_to_swap

            # Update p_idx with permute[p_idx] e.g. the new index of el_to_be_replaced
            p_idx = permute[p_idx]
            permute[p_idx] = None
            el_to_swap = el_to_be_replaced

        if entered:
            arr[p_idx] = el_to_swap

    return arr

"""
result = [1, 3, 2]
i = 0
    p_idx = 0
    el2swap = 1
    do nothing
i = 1
    p_idex = 2
    el2swap = 2
    2 != 1
        repl = 3
        result[2] = 2
        p_idx = 1
        permute[i] = None
        el2swap = 3
    result[1] = 3
    1 == 1
i = 2
    p_idx = 1
"""


def test_permute_array_swaps():
    expected = [1, 3, 2]
    actual = permute_array_swaps([1, 2, 3], [0, 2, 1])
    if expected != actual:
        print("\nFailed!")
        print(f"\tExpected: {expected}")
        print(f"\tResult: {actual}\n")

if __name__ == "__main__":
    test_permute_array_swaps()







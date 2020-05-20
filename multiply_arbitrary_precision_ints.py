from typing import List

# Input: two arrays representing integers
# Output: array representing product: [1, 0], [-1, 0] => [-1, 0, 0]


# [1, 0, 0] * [1, 2, 5, 6, 7]

def multiply_arbitrary_precision(a: List[int], b: List[int]) -> List[int]:
    print("Multiplying:")
    print(f"\t{a} x")
    print(f"\t{b}")

    # First we must determine the sign
    sign = get_sign(a[0], b[0])

    product = [0] * max_product_digits(a, b)
    # Then determine size of array of product, this would be ideal to determine in advance
        # Why? Constantly appending to the array is more costly as it will constantly need to resize
    # From BACK to front, iterate over both, making sure to carry over anything
        # Is indexing important here?
    for j in range(len(b)):
        digit_b = abs(b[len(b) - 1 - j])
        for i in range(len(a)):
            digit_a = abs(a[len(a) - 1 - i])

            p = digit_a * digit_b
            carryover = p // 10
            leftover = p % 10

            p_index = len(product) - 1 - i - j
            product[p_index] += leftover
            if product[p_index] > 9:
                carryover += product[p_index] // 10
                product[p_index] = product[p_index] % 10

            product[p_index - 1] += carryover

    # Trim zeros (make sure to ensure that if we have a list of ALL 0's, we keep at least one)
    while product[0] == 0 and len(product) > 1:
        product.pop(0)
    # multiply first num by sign
    product[0] *= sign
    print("Result:")
    print(f"\t{product}\n\n")
    return product

# Why so many helpers? you can test each one!
# Or just pseudo-code one if you don't know how to do it yet!
def get_sign(a, b):
    # to do, given two ints, determine if sign of their product is pos or neg
    # return (a * b) / abs(a * b)
    return -1 if (a * b) < 0 else 1

def max_product_digits(a: List[int], b: List[int]) -> int:
    # given two lists of ints, return list of 0's of length of max digits of their product
    return (len(a) + len(b))


# *********** TESTS ***********
def int_to_list(a: int) -> List[int]:
    if a == 0:
        return [0]

    sign = -1 if a < 0 else 1
    a = abs(a)
    l = []
    while a > 0:
        d = a % 10
        l = [d] + l
        a //= 10
    l[0] *= sign
    return l

def list_to_int(a: List[int]) -> int:
    val = 0
    sign = 1 if a[0] > 0 else -1
    while len(a):
        d = abs(a.pop(0))
        val = 10 * val + d
    return val * sign

def multiply_ints(a: int, b: int) -> int:
    a_list = int_to_list(a)
    b_list = int_to_list(b)
    p_list = multiply_arbitrary_precision(a_list, b_list)
    return list_to_int(p_list)

def test_multiply_arbitrary_precision():
    assert int_to_list(123) == [1,2,3]
    assert int_to_list(-123) == [-1,2,3]
    assert multiply_ints(8, 3) == (8 * 3)
    assert multiply_ints(812, 334) == (812 * 334)

    assert multiply_ints(-1, 2) == (-1 * 2)

    for i in range(-100000, 10000):
        for j in range(-100000, 10000):
            assert_multiply_equals(i, j)


def assert_multiply_equals(a, b):
    if multiply_ints(a, b) != (a * b):
        print("Math, bro! You f'd up")
        print(f"\t a: {a} b: {b})")
        print(f"\tmultiply_ints: {multiply_ints(a, b)}, a * b: {a * b}")
        assert False


if __name__ == "__main__":
    test_multiply_arbitrary_precision()
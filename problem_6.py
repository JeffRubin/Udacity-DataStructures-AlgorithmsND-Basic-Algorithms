def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if len(ints) == 0:
        return None, None

    min_val = ints[0]
    max_val = ints[0]

    for v in ints:
        if v < min_val:
            min_val = v
        elif v > max_val:
            max_val = v

    return min_val, max_val

# Test Cases
#
# Test Case 1: All positive integers
print(get_min_max([2, 3, 1, 4, 5]))
# Expected Output: (1, 5))
#
# Test Case 2: All negative integers
print(get_min_max([-2, -3, -1, -4, -5]))
# Expected Output: (-5, -1))
#
# Test Case 3: Mix of positive and negative integers
print(get_min_max([-2, 3, 1, 4, -5]))
# Expected Output: (-5, 4))
#
# Test Case 4: Edge Case: Empty input
print(get_min_max([]))
# Expected Output: (None, None))
#
# Test Case 5: Edge Case: One input
print(get_min_max([8675309]))
# Expected Output: (8675309, 8675309))
#
# Test Case 6: Edge Case: All inputs are the same
print(get_min_max([125, 125, 125, 125, 125]))
# Expected Output: (125, 125))

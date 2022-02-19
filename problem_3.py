def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    Notes:
        You can assume that all array elements are in the range [0, 9]
    """
    if len(input_list) == 0:
        return None, None
    elif len(input_list) == 1:
        return input_list[0], None

    sorted_input_list = merge_sort(input_list)

    first_num = 0
    second_num = 0
    ten_pow = 0
    is_odd_index = True

    # This extracts the sorted digits from lowest to highest in value and uses these to form the output numbers
    # by placing the lowest values in the least significance in the output numbers and the highest values
    # in the greatest significance in the output numbers.  The sorted digits are interleaved for the two output numbers
    # to maximize their sum by always placing the highest value numbers at the greatest significance.
    for d in sorted_input_list:
        # violates the assumption that all values are [0, 9]
        if d < 0 or d > 9:
            return None, None

        if is_odd_index:
            first_num += d * pow(10, ten_pow)
            # only increment ten_pow after even indices since even indices are calculated after odd indices
            is_odd_index = False
        else:
            second_num += d * pow(10, ten_pow)
            ten_pow += 1
            is_odd_index = True

    # always output the larger number as the first number (for ease of test case verification)
    if second_num > first_num:
        first_num, second_num = second_num, first_num

    return first_num, second_num


def merge_sort(input_list):
    # base case
    if len(input_list) <= 1:
        return input_list

    mid = len(input_list)//2

    left = merge_sort(input_list[:mid])
    right = merge_sort(input_list[mid:])

    return merge(left, right)


def merge(left, right):
    left_idx = 0
    right_idx = 0
    merged = []

    while left_idx < len(left) and right_idx < len(right):
        left_val = left[left_idx]
        right_val = right[right_idx]
        if left_val <= right_val:
            merged.append(left_val)
            left_idx += 1
        else:
            merged.append(right_val)
            right_idx += 1

    # merge left over elements not sorted in the while loop
    merged += left[left_idx:]
    merged += right[right_idx:]

    return merged


# Test Cases
#
# Test Case 1: Already sorted
print(rearrange_digits([1, 2, 3, 4, 5]))
# Expected Output: (531, 42)
#
# Test Case 2: Not sorted
print(rearrange_digits([4, 6, 2, 5, 9, 8]))
# Expected Output: (964, 852)
#
# Test Case 3: Only two elements
print(rearrange_digits([2, 1]))
# Expected Output: (2, 1)
#
# Test Case 4: All elements are the same
print(rearrange_digits([1, 1, 1, 1]))
# Expected Output: (11, 11)
#
# Test Case 5: Edge case: [0,9] range assumption is violated
print(rearrange_digits([4, 6, 2, 5, 9, -8]))
# Expected Output: (None, None)
#
# Test Case 6: Edge case: Empty input
print(rearrange_digits([]))
# Expected Output: (None, None)
#
# Test Case 7: Edge case: Only one element
print(rearrange_digits([1]))
# Expected Output: (1, None)

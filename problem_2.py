def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    Notes:
       You can assume there are no duplicates in the array
    """
    if len(input_list) == 0:
        return -1

    last_idx = len(input_list) - 1

    # find the rotation pivot then binary search for the specified number in the ordered list that either:
    # starts at the pivot or
    # ends right before the pivot
    pivot = find_pivot(input_list, 0, last_idx)
    if pivot == None:
        return binary_search(input_list, number, 0, last_idx)
    else:
        if number > input_list[-1]:  # last element is the biggest value in the ordered list starting at the pivot
            return binary_search(input_list, number, 0, pivot - 1)
        else:
            return binary_search(input_list, number, pivot, last_idx)


def find_pivot(input_list, start_idx, end_idx):
    # Used help from: https://knowledge.udacity.com/questions/770441
    # Specifically, I needed help to determine the base case.  I was able to figure out the recursion on my own
    # to search for the pivot using a binary search but I didn't see how to end the recursion, which is simply to check
    # if the current middle value or the value after that is the pivot by comparing if these values are less than the
    # previous values in the list.
    if start_idx > end_idx:
        return None

    mid_idx = (start_idx + end_idx) // 2
    mid_val = input_list[mid_idx]

    if (mid_idx > start_idx) and (mid_val < input_list[mid_idx - 1]):
        return mid_idx
    elif (mid_idx < end_idx) and (input_list[mid_idx + 1] < mid_val):
        return mid_idx + 1
    elif mid_val > input_list[start_idx]:  # pivot is after current mid_idx
        return find_pivot(input_list, mid_idx + 1, end_idx)
    else:  # mid_val <= input_list[start_idx]; pivot is before the current mid_idx (or at the current mid_idx if the input_list only has 1 element)
        return find_pivot(input_list, start_idx, mid_idx - 1)


def binary_search(input_list, target, start_idx, end_idx):
    if start_idx > end_idx:
        return -1

    mid_idx = (start_idx + end_idx) // 2
    mid_val = input_list[mid_idx]

    if target == mid_val:
        return mid_idx
    elif target > mid_val:
        return binary_search(input_list, target, mid_idx + 1, end_idx)
    else:  # target < mid_val
        return binary_search(input_list, target, start_idx, mid_idx - 1)


# Test Cases
#
# Test Case 1: Number found: Before the pivot
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6))
# Expected Output: 0
#
# Test Case 2: Number found: After the pivot
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 4))
# Expected Output: 8
#
# Test Case 3: Number found: At the pivot
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1))
# Expected Output: 5
#
# Test Case 4: Edge case: Number not found
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 0))
# Expected Output: -1
#
# Test Case 5: Edge case: No pivot
print(rotated_array_search([6, 7, 8, 9, 10], 9))
# Expected Output: 3
#
# Test Case 6: Edge case: Empty input array
print(rotated_array_search([], 0))
# Expected Output: -1
#
# Test Case 7: Edge case: Input array has one value which matches the target
print(rotated_array_search([1], 1))
# Expected Output: 0
#
# Test Case 8: Edge case: Input array has one value which does not match the target
print(rotated_array_search([1], 0))
# Expected Output: -1

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    next_0_idx = 0
    next_2_idx = len(input_list)-1
    cur_idx = 0

    while cur_idx <= next_2_idx:
        cur_val = input_list[cur_idx]

        if cur_val == 0:
            # swap
            input_list[cur_idx], input_list[next_0_idx] = input_list[next_0_idx], input_list[cur_idx]
            next_0_idx += 1
            cur_idx += 1
        elif cur_val == 1:
            cur_idx += 1
        else: # cur_val == 2
            # swap
            input_list[cur_idx], input_list[next_2_idx] = input_list[next_2_idx], input_list[cur_idx]
            next_2_idx -= 1
            # do not increment cur_idx since may have swapped a value to cur_idx that needs further sorting

    return input_list


# Test Cases
#
# Test Case 1: Sorting Needed 1
print(sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))
# Expected Output: [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
#
# Test Case 2: Sorting Needed 2
print(sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]))
# Expected Output: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0. 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
#
# Test Case 3: Already Sorted
print(sort_012([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]))
# Expected Output: [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
#
# Test Case 4: Reverse Sorted
print(sort_012([2, 2, 2, 2, 1, 1, 0, 0, 0]))
# Expected Output: [0, 0, 0, 1, 1, 2, 2, 2, 2]
#
# Test Case 5: Edge Case: Empty input
print(sort_012([]))
# Expected Output: []
#
# Test Case 6: Edge Case: All 0s
print(sort_012(5*[0]))
# Expected Output: [0, 0, 0, 0, 0]
#
# Test Case 7: Edge Case: All 1s
print(sort_012(5*[1]))
# Expected Output: [1, 1, 1, 1, 1]
#
# Test Case 8: Edge Case: All 2s
print(sort_012(5*[2]))
# Expected Output: [2, 2, 2, 2, 2]

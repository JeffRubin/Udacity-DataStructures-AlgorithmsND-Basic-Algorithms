def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number >= 0:
        return square_root_recur(number, 0, number)
    else:  # negative, only imaginary part (no real part)
        return complex(0, square_root_recur(-1 * number, 0, -1 * number))


def square_root_recur(num, low, high):
    # special case (since 1//2 = 0)
    if num == 1:
        return 1

    mid = (low + high) // 2

    # base case
    if mid == low or mid == high:
        return mid

    sqrt_approx = mid * mid

    # binary search
    if sqrt_approx == num:
        return mid
    elif sqrt_approx > num:
        return square_root_recur(num, low, mid)
    else:  # sqrt_approx < num
        return square_root_recur(num, mid, high)


# Test Cases
#
# Test Case 1: Perfect square root: Odd
print(sqrt(9))
# Expected Output: 3
#
# Test Case 2: Perfect square root: Even
print(sqrt(16))
# Expected Output: 4
#
# Test Case 3: Not perfect square root: Odd
print(sqrt(27))
# Expected Output: 5
#
# Test Case 4: Not perfect square root: Even
print(sqrt(28))
# Expected Output: 5
#
# Test Case 5: Edge case: 0
print(sqrt(0))
# Expected Output: 0
#
# Test Case 6: Edge case: 1
print(sqrt(1))
# Expected Output: 1
#
# Test Case 7: Edge case: Very large number
print(sqrt(123456789))
# Expected Output: 11111
#
# Test Case 8: Edge case: Negative
print(sqrt(-1))
# Expected Output: 1j
#
# Test Case 9: Edge case: Negative
print(sqrt(-27))
# Expected Output: 5j

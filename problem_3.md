# Problem 3: Rearrange Array Digits

## Description
The approach was to sort the input list and then extract the sorted digits from lowest to highest in value and use these
to form the output numbers by placing the lowest values in the least significance in the output numbers and the
highest values in the greatest significance in the output numbers.  The sorted digits are interleaved for the two
output numbers to maximize their sum by always placing the highest value numbers at the greatest significance.

## Complexity: Time
O(n log n) since this is the complexity of the mergesort function used to sort the input list.
Forming the output numbers is a single pass through the sorted list, which is O(n) which is not a significant
contribution to the overall time complexity.

## Complexity: Space
O(n) since this is the space complexity of mergesort to store all the parts of the array being sorted; mergesort
does not sort in place.  Other local variables, e.g. first_num, ten_pow do not have a significant contribution to the
overall space complexity.
